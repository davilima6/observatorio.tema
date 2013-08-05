# -*- coding: utf-8 -*-

from collective.cover.tiles.collection import ICollectionTile
from collective.cover.tiles.collection import CollectionTile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IEventosTile(ICollectionTile):
    """
    """


class EventosTile(CollectionTile):
    index = ViewPageTemplateFile("templates/eventos.pt")
