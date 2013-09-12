# -*- coding: utf-8 -*-

from plone.batching.batch import Batch
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
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class IBibliotecaTile(IListTile):
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


class BibliotecaTile(ListTile):
    index = ViewPageTemplateFile("templates/biblioteca.pt")
    is_editable = True
    limit = 12

    def results(self):
        """ Return the list of objects stored in the tile.
        """
        self.set_limit()
        uuids = self.data.get('uuids', None)
        results = []
        if uuids:
            uuids = [uuids] if type(uuids) == str else uuids
            for uid in uuids:
                obj = uuidToObject(uid)
                if obj:
                    results.append(obj)
                else:
                    self.remove_item(uid)

        final_result = []
        batch = Batch.fromPagenumber(items=results, pagesize=4, pagenumber=1)
        for num in batch.navlist:
            batch.pagenumber = num
            final_result.append(list(batch))
        return final_result

    def populate_with_object(self, obj):
        if not obj.portal_type == 'Publicacao':
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

    def get_area(self, area):
        context = self.context
        factory = getUtility(IVocabularyFactory, 'observatorio.conteudo.areas_tematicas')
        vocabulary = factory(context)

        termo = vocabulary.getTerm(area)

        return termo.title