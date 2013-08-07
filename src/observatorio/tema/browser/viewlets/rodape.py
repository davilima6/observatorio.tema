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

    def site_actions(self):
        context_state = getMultiAdapter((self.context, self.request),
            name=u'plone_context_state')
        return context_state.actions('site_actions')

    def rodape_actions(self):
        context_state = getMultiAdapter((self.context, self.request),
            name=u'plone_context_state')
        return context_state.actions('site_sections')

