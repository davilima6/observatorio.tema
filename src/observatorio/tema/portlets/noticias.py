# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from zope import schema
from zope.interface import implements
from zope.formlib import form

from plone.memoize.instance import memoize
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from observatorio.tema import _


class IUltimasNoticias(IPortletDataProvider):
    """A portlet
    """

    noticias = schema.Choice(
        title=_(u"Colecao com as noticias"),
        description=_(u"Informe a colecao das noticias."),
        required=False,
        source=SearchableTextSourceBinder({'portal_type': 'Collection'}, default_query='path:'))

    eventos = schema.Choice(
        title=_(u"Colecao com os eventos"),
        description=_(u"Informe a colecao dos eventos."),
        required=False,
        source=SearchableTextSourceBinder({'portal_type': 'Collection'}, default_query='path:'))


class Assignment(base.Assignment):
    """Portlet assignment.
    """

    implements(IUltimasNoticias)

    root = None

    def __init__(self, noticias=None, eventos=None):
        self.noticias = noticias
        self.eventos = eventos

    @property
    def title(self):
        """
        """
        return _(u'Noticias e Eventos')


class Renderer(base.Renderer):
    """Portlet renderer.
    """

    render = ViewPageTemplateFile('templates/noticias.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

        self.catalog = getToolByName(context, 'portal_catalog')
        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    @property
    def available(self):
        if self.noticias() or self.eventos():
            return True

    @memoize
    def noticias(self):
        path = self.data.noticias
        lista = path.split('/')
        id = lista[len(lista)-1]

        colecao = self.catalog(id = id, portal_type='Collection', path='/'.join(self.portal.getPhysicalPath()) + path)[0].getObject()
        return colecao

    @memoize
    def eventos(self):
        path = self.data.eventos
        lista = path.split('/')
        id = lista[len(lista)-1]

        colecao = self.catalog(id = id, portal_type='Collection', path='/'.join(self.portal.getPhysicalPath()) + path)[0].getObject()
        return colecao


class AddForm(base.AddForm):
    form_fields = form.Fields(IUltimasNoticias)
    form_fields['noticias'].custom_widget = UberSelectionWidget
    form_fields['eventos'].custom_widget = UberSelectionWidget
    label = _(u"Adicionar o Portlet de Noticias e Eventos")
    description = _(u"")

    def create(self, data):
        return Assignment(
            noticias=data.get('noticias', ''),
            eventos=data.get('eventos', ''),
        )


class EditForm(base.EditForm):
    form_fields = form.Fields(IUltimasNoticias)
    form_fields['noticias'].custom_widget = UberSelectionWidget
    form_fields['eventos'].custom_widget = UberSelectionWidget
    label = _(u"Editar o Portlet de Noticias e Eventos")
    description = _(u"")
