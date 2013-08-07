# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from observatorio.tema import _


class IEixosAtuacao(IPortletDataProvider):
    """A portlet
    """


class Assignment(base.Assignment):
    """Portlet assignment.
    """

    implements(IEixosAtuacao)

    root = None

    def __init__(self, root=None):
        self.root = root

    @property
    def title(self):
        """
        """
        return _(u'Eixos de Atuação')


class Renderer(base.Renderer):
    """Portlet renderer.
    """

    render = ViewPageTemplateFile('templates/eixos.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    @property
    def available(self):
        if self.get_eixos():
            return True

#    @memoize
    def get_eixos(self):
        areas = getattr(self.portal, 'eixos-de-atuacao')
        if areas:
            return [area for area in areas.objectValues() if not area.getExcludeFromNav()]


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
