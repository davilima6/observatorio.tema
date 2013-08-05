# -*- coding: utf-8 -*-

from observatorio.tema import _
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from plone.app.uuid.utils import uuidToObject
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema


class INoticiasHomeTile(IListTile):
    """
    """

    form.widget(uuids=TextLinesSortableFieldWidget)
    uuids = schema.List(
        title=_(u'Elements'),
        value_type=schema.TextLine(),
        required=False,
        readonly=False,
    )


class NoticiasHomeTile(ListTile):
    index = ViewPageTemplateFile("templates/noticias_home.pt")
    is_configurable = False
    is_editable = True
    limit = 3

    def populate_with_object(self, obj):
        if obj.portal_type in self.accepted_ct():
            self.set_limit()
            uuid = IUUID(obj, None)
            data_mgr = ITileDataManager(self)

            old_data = data_mgr.get()
            if data_mgr.get()['uuids']:
                uuids = data_mgr.get()['uuids']
                if type(uuids) != list:
                    uuids = [uuid]
                elif uuid not in uuids:
                    uuids.append(uuid)

                old_data['uuids'] = uuids[:self.limit]
            else:
                old_data['uuids'] = [uuid]
            data_mgr.set(old_data)

    def accepted_ct(self):
        return ['Collection']

    def get_uid(self, obj):
        return IUUID(obj)
