# -*- coding: utf-8 -*-

from collective.cover.tiles.base import IPersistentCoverTile, PersistentCoverTile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.PythonScripts.standard import url_quote
from zope import schema
from zope.interface import implements


class ISocialTile(IPersistentCoverTile):

    facebook_page = schema.TextLine(
        title=u'Facebook Page URL',
        required=False,
    )


class SocialTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/social.pt")
    implements(IPersistentCoverTile)
    is_droppable = False


    def facebook_available(self):
        return self.data['facebook_page']
