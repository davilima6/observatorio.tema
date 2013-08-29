# -*- coding: utf-8 -*-

from observatorio.tema import _
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema


class IDavizTile(IListTile):
    """
    """

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    autoplay = schema.Bool(
        title=_(u'Auto play'),
        required=False,
        default=True,
    )

    form.widget(uuids=TextLinesSortableFieldWidget)
    uuids = schema.List(
        title=_(u'Elements'),
        value_type=schema.TextLine(),
        required=False,
        readonly=False,
    )


class DavizTile(ListTile):
    index = ViewPageTemplateFile("templates/daviz.pt")
    is_configurable = False
    is_editable = True

    def populate_with_object(self, obj):
        try:
            image = obj.restrictedTraverse('chart_1.png')
        except:
            image = None
        if not image:
            return
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

    def autoplay(self):
        if self.data['autoplay'] is None:
            return True  # default value

        return self.data['autoplay']

    def get_uid(self, obj):
        return IUUID(obj)
