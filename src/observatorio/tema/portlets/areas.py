# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from zope.interface import implements

from plone.memoize.instance import memoize
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from observatorio.tema import _


class IAreasTematicas(IPortletDataProvider):
    """A portlet
    """


class Assignment(base.Assignment):
    """Portlet assignment.
    """

    implements(IAreasTematicas)

    root = None

    def __init__(self, root=None):
        self.root = root

    @property
    def title(self):
        """
        """
        return _(u'Áreas temáticas')


class Renderer(base.Renderer):
    """Portlet renderer.
    """

    render = ViewPageTemplateFile('templates/areas.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    @property
    def available(self):
        if self.get_areas():
            return True

    @memoize
    def get_areas(self):
        areas = getattr(self.portal, 'areas-tematicas')
        if areas:
            return [area for area in areas.objectValues() if area.portal_type == 'Folder' and not area.getExcludeFromNav()]


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
