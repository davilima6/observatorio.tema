# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.interface import Interface
from five import grok

from Products.CMFCore.utils import getToolByName

from plone.app.layout.viewlets.interfaces import IPortalFooter

from observatorio.conteudo.interfaces import IBanner
from observatorio.tema.interfaces import IObservatorioTemaLayer

grok.context(Interface)
grok.templatedir("templates")


class BannersViewlet(grok.Viewlet):
    """ Viewlet que exibira os banners
    """

    grok.viewletmanager(IPortalFooter)
    grok.layer(IObservatorioTemaLayer)

    def get_banners(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        banners = catalog(object_provides = IBanner.__identifier__, review_state='published')
        if banners:
            return banners
        else:
            return None

    def available(self):
        if self.get_banners():
            return True


