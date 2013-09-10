# -*- coding: utf-8 -*-

from collective.cover.tiles.base import IPersistentCoverTile, PersistentCoverTile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.EasyNewsletter.portlets.subscriber import INewsletterSubscriberPortlet
from zope import schema
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from plone.app.uuid.utils import uuidToObject

from zope.component import getUtility, getMultiAdapter, queryMultiAdapter
from plone.portlets.interfaces import IPortletRetriever, IPortletManager, IPortletRenderer


class IBoletimTile(IPersistentCoverTile):

    title = schema.TextLine(
        title = u"Título",
        default = u"Boletim",
        required = True,
    )

    description = schema.Text(
        title = u"Descrição",
        description = u"Cadastre-se em nosso boletim.",
        default = u"",
        required = False)


class BoletimTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/boletim.pt")

    is_configurable = True
    is_editable = True
    is_droppable = False

    def results(self):
        uuid = self.data.get('uuid', None)
        if uuid is not None:
            obj = uuidToObject(uuid)
            return obj

    def populate_with_object(self, obj):
        super(BoletimTile, self).populate_with_object(obj)
        uuid = IUUID(obj, None)
        data_mgr = ITileDataManager(self)
        data_mgr.set({'uuid': uuid})

    def get_newsletter(self):

        column = "plone.leftcolumn"
        portal = getToolByName(self.context, "portal_url").getPortalObject()
        manager = getUtility(IPortletManager, name=column)
        retriever = getMultiAdapter((portal, manager), IPortletRetriever)
        portlets = retriever.getPortlets()
        interface = INewsletterSubscriberPortlet
        assignment = None

        for portlet in portlets:

            if interface.providedBy(portlet["assignment"]):
                assignment = portlet["assignment"]
                break

        newsletter = assignment.newsletter

        if newsletter:
            return newsletter
