# -*- coding: utf-8 -*-

from five import grok
from collective.cover.content import View as OriginalCoverView
from observatorio.tema.interfaces import IObservatorioTemaLayer
from zope.component import getMultiAdapter

grok.templatedir("templates")


class CoverView(OriginalCoverView):
    grok.layer(IObservatorioTemaLayer)


    def canonical_object(self):

        context_helper = getMultiAdapter((self.context, self.request), name="plone_context_state")
        canonical = context_helper.canonical_object()
        return canonical.absolute_url()