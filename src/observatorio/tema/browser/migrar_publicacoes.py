# -*- coding: utf-8 -*-

from five import grok
from zope.event import notify
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName

from observatorio.conteudo.eventos import cria_capa_publicacao_edicao


class MigrarPublicacoesView(grok.View):
    grok.name('migracao')
    grok.permissions("Zope2.View")
    grok.context(Interface)


    def update(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        resultado = catalog(portal_type = 'Publicacao')
        for i in resultado:
            obj = i.getObject()
            cria_capa_publicacao_edicao(obj, self.context.REQUEST)

    def render(self, **kwargs):
        return 'ok'

