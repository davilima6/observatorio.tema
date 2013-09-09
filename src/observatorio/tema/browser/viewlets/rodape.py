# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.interface import Interface
from five import grok

from zope.component import getMultiAdapter

from plone.app.layout.viewlets.interfaces import IPortalFooter

from observatorio.tema.interfaces import IObservatorioTemaLayer

grok.context(Interface)
grok.templatedir("templates")


class RodapeViewlet(grok.Viewlet):
    """ Viewlet que eixibira o rodape
    """

    grok.viewletmanager(IPortalFooter)
    grok.layer(IObservatorioTemaLayer)
    
    def update(self):
        self.context_state = getMultiAdapter((self.context, self.request),
            name=u'plone_context_state')

    def site_actions(self):
        return self.context_state.actions('site_actions')

    def site_sections(self):
        return self.context_state.actions('site_sections')

