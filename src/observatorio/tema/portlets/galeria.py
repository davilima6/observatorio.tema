# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from zope.formlib import form

from plone.memoize.instance import memoize
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from observatorio.tema import _


class IGaleria(IPortletDataProvider):
    """A portlet
    """

    root = schema.Choice(
        title=_(u"Pasta com as fotos"),
        description=_(u"Informe o local onde estao as fotos que serao exibidas."),
        required=False,
        source=SearchableTextSourceBinder({'is_folderish': True}, default_query='path:'))


class Assignment(base.Assignment):
    """Portlet assignment.
    """

    implements(IGaleria)

    root = None

    def __init__(self, root=None):
        self.root = root

    @property
    def title(self):
        """
        """
        return _(u'Galeria de Fotos')


class Renderer(base.Renderer):
    """Portlet renderer.
    """

    render = ViewPageTemplateFile('templates/galeria.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

        self.catalog = getToolByName(context, 'portal_catalog')
        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    @property
    def available(self):
        if self.get_imagens():
            return True

    @memoize
    def get_imagens(self):
        path = '/'.join(self.portal.getPhysicalPath()) + self.data.root
        resultado = self.catalog(portal_type='Image', path=path, sort_limit=12)[:12]
        if resultado:
            for r in resultado:
                r.parentURL = '/'.join(r.split('/')[:-1])
            return resultado


class AddForm(base.AddForm):
    form_fields = form.Fields(IGaleria)
    form_fields['root'].custom_widget = UberSelectionWidget
    label = _(u"Adicionar o Portlet de Galeria")
    description = _(u"")

    def create(self, data):
        return Assignment(root=data.get('root', ""))


class EditForm(base.EditForm):
    form_fields = form.Fields(IGaleria)
    form_fields['root'].custom_widget = UberSelectionWidget
    label = _(u"Editar o Portlet de Galeria")
    description = _(u"")
