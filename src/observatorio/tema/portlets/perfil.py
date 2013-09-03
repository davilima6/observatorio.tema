# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from zope.formlib import form

from plone.memoize.instance import memoize
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from observatorio.tema import _


class IPerfil(IPortletDataProvider):
    """A portlet
    """

    sumario = schema.Text(
        title=_(u"Sumário"),
        description=_(u""),
        required=False,
    )

    perfil_1 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=True,
    )

    perfil_1_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=True,
    )

    perfil_1_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=True,
    )

    perfil_1_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=True,
    )

    perfil_1_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=True,
    )

    perfil_1_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_1_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_1_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_1_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_2 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_2_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_2_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_2_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_2_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_2_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_2_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_2_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_2_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_3 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_3_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_3_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_3_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_3_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_3_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_3_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_3_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_3_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_4 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_4_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_4_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_4_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_4_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_4_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_4_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_4_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_4_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_5 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_5_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_5_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_5_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_5_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_5_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_5_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_5_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_5_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_6 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_6_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_6_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_6_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_6_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_6_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_6_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_6_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_6_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_7 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_7_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_7_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_7_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_7_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_7_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_7_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_7_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_7_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_8 = schema.TextLine(
        title=_(u"Título do perfil"),
        description=_(u"Informe o nome do perfil do público alvo."),
        required=False,
    )

    perfil_8_link01_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_8_link01_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_8_link02_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_8_link02_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_8_link03_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_8_link03_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )

    perfil_8_link04_titulo = schema.TextLine(
        title=_(u"Título do link"),
        description=_(u"Informe o título da URL."),
        required=False,
    )

    perfil_8_link04_url = schema.URI(
        title=_(u"URL"),
        description=_(u"Informe a URL."),
        required=False,
    )


class Assignment(base.Assignment):
    """Portlet assignment.
    """

    implements(IPerfil)

    root = None

    def __init__(self,
                 sumario=None,
                 perfil_1=None,
                 perfil_1_link01_titulo=None,
                 perfil_1_link01_url=None,
                 perfil_1_link02_titulo=None,
                 perfil_1_link02_url=None,
                 perfil_1_link03_titulo=None,
                 perfil_1_link03_url=None,
                 perfil_1_link04_titulo=None,
                 perfil_1_link04_url=None,
                 perfil_2=None,
                 perfil_2_link01_titulo=None,
                 perfil_2_link01_url=None,
                 perfil_2_link02_titulo=None,
                 perfil_2_link02_url=None,
                 perfil_2_link03_titulo=None,
                 perfil_2_link03_url=None,
                 perfil_2_link04_titulo=None,
                 perfil_2_link04_url=None,
                 perfil_3=None,
                 perfil_3_link01_titulo=None,
                 perfil_3_link01_url=None,
                 perfil_3_link02_titulo=None,
                 perfil_3_link02_url=None,
                 perfil_3_link03_titulo=None,
                 perfil_3_link03_url=None,
                 perfil_3_link04_titulo=None,
                 perfil_3_link04_url=None,
                 perfil_4=None,
                 perfil_4_link01_titulo=None,
                 perfil_4_link01_url=None,
                 perfil_4_link02_titulo=None,
                 perfil_4_link02_url=None,
                 perfil_4_link03_titulo=None,
                 perfil_4_link03_url=None,
                 perfil_4_link04_titulo=None,
                 perfil_4_link04_url=None,
                 perfil_5=None,
                 perfil_5_link01_titulo=None,
                 perfil_5_link01_url=None,
                 perfil_5_link02_titulo=None,
                 perfil_5_link02_url=None,
                 perfil_5_link03_titulo=None,
                 perfil_5_link03_url=None,
                 perfil_5_link04_titulo=None,
                 perfil_5_link04_url=None,
                 perfil_6=None,
                 perfil_6_link01_titulo=None,
                 perfil_6_link01_url=None,
                 perfil_6_link02_titulo=None,
                 perfil_6_link02_url=None,
                 perfil_6_link03_titulo=None,
                 perfil_6_link03_url=None,
                 perfil_6_link04_titulo=None,
                 perfil_6_link04_url=None,
                 perfil_7=None,
                 perfil_7_link01_titulo=None,
                 perfil_7_link01_url=None,
                 perfil_7_link02_titulo=None,
                 perfil_7_link02_url=None,
                 perfil_7_link03_titulo=None,
                 perfil_7_link03_url=None,
                 perfil_7_link04_titulo=None,
                 perfil_7_link04_url=None,
                 perfil_8=None,
                 perfil_8_link01_titulo=None,
                 perfil_8_link01_url=None,
                 perfil_8_link02_titulo=None,
                 perfil_8_link02_url=None,
                 perfil_8_link03_titulo=None,
                 perfil_8_link03_url=None,
                 perfil_8_link04_titulo=None,
                 perfil_8_link04_url=None):

        self.sumario = sumario
        self.perfil_1 = perfil_1
        self.perfil_1_link01_titulo = perfil_1_link01_titulo
        self.perfil_1_link01_url = perfil_1_link01_url
        self.perfil_1_link02_titulo = perfil_1_link02_titulo
        self.perfil_1_link02_url = perfil_1_link02_url
        self.perfil_1_link03_titulo = perfil_1_link03_titulo
        self.perfil_1_link03_url =  perfil_1_link03_url
        self.perfil_1_link04_titulo = perfil_1_link04_titulo
        self.perfil_1_link04_url = perfil_1_link04_url
        self.perfil_2 = perfil_2
        self.perfil_2_link01_titulo = perfil_2_link01_titulo
        self.perfil_2_link01_url = perfil_2_link01_url
        self.perfil_2_link02_titulo = perfil_2_link02_titulo
        self.perfil_2_link02_url = perfil_2_link02_url
        self.perfil_2_link03_titulo = perfil_2_link03_titulo
        self.perfil_2_link03_url = perfil_2_link03_url
        self.perfil_2_link04_titulo = perfil_2_link04_titulo
        self.perfil_2_link04_url = perfil_2_link04_url
        self.perfil_3 = perfil_3
        self.perfil_3_link01_titulo = perfil_3_link01_titulo
        self.perfil_3_link01_url = perfil_3_link01_url
        self.perfil_3_link02_titulo = perfil_3_link02_titulo
        self.perfil_3_link02_url = perfil_3_link02_url
        self.perfil_3_link03_titulo = perfil_3_link03_titulo
        self.perfil_3_link03_url = perfil_3_link03_url
        self.perfil_3_link04_titulo = perfil_3_link04_titulo
        self.perfil_3_link04_url = perfil_3_link04_url
        self.perfil_4 = perfil_4
        self.perfil_4_link01_titulo = perfil_4_link01_titulo
        self.perfil_4_link01_url = perfil_4_link01_url
        self.perfil_4_link02_titulo = perfil_4_link02_titulo
        self.perfil_4_link02_url = perfil_4_link02_url
        self.perfil_4_link03_titulo = perfil_4_link03_titulo
        self.perfil_4_link03_url = perfil_4_link03_url
        self.perfil_4_link04_titulo = perfil_4_link04_titulo
        self.perfil_4_link04_url = perfil_4_link04_url
        self.perfil_5 = perfil_5
        self.perfil_5_link01_titulo = perfil_5_link01_titulo
        self.perfil_5_link01_url = perfil_5_link01_url
        self.perfil_5_link02_titulo = perfil_5_link02_titulo
        self.perfil_5_link02_url = perfil_5_link02_url
        self.perfil_5_link03_titulo = perfil_5_link03_titulo
        self.perfil_5_link03_url = perfil_5_link03_url
        self.perfil_5_link04_titulo = perfil_5_link04_titulo
        self.perfil_5_link04_url = perfil_5_link04_url
        self.perfil_6 = perfil_6
        self.perfil_6_link01_titulo = perfil_6_link01_titulo
        self.perfil_6_link01_url = perfil_6_link01_url
        self.perfil_6_link02_titulo = perfil_6_link02_titulo
        self.perfil_6_link02_url = perfil_6_link02_url
        self.perfil_6_link03_titulo = perfil_6_link03_titulo
        self.perfil_6_link03_url = perfil_6_link03_url
        self.perfil_6_link04_titulo = perfil_6_link04_titulo
        self.perfil_6_link04_url = perfil_6_link04_url
        self.perfil_7 = perfil_7
        self.perfil_7_link01_titulo = perfil_7_link01_titulo
        self.perfil_7_link01_url = perfil_7_link01_url
        self.perfil_7_link02_titulo = perfil_7_link02_titulo
        self.perfil_7_link02_url = perfil_7_link02_url
        self.perfil_7_link03_titulo = perfil_7_link03_titulo
        self.perfil_7_link03_url = perfil_7_link03_url
        self.perfil_7_link04_titulo = perfil_7_link04_titulo
        self.perfil_7_link04_url = perfil_7_link04_url
        self.perfil_8 = perfil_8
        self.perfil_8_link01_titulo = perfil_8_link01_titulo
        self.perfil_8_link01_url = perfil_8_link01_url
        self.perfil_8_link02_titulo = perfil_8_link02_titulo
        self.perfil_8_link02_url = perfil_8_link02_url
        self.perfil_8_link03_titulo = perfil_8_link03_titulo
        self.perfil_8_link03_url = perfil_8_link03_url
        self.perfil_8_link04_titulo = perfil_8_link04_titulo
        self.perfil_8_link04_url = perfil_8_link04_url

    @property
    def title(self):
        """
        """
        return _(u'Observatório e Você')


class Renderer(base.Renderer):
    """Portlet renderer.
    """

    render = ViewPageTemplateFile('templates/perfil.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

    @property
    def available(self):
        if self.get_perfis():
            return True

    @memoize
    def get_perfis(self):
        ''' funcao que retorna os perfis e seus links
        '''
        perfis = []

        for i in range(1,7):
            perfil = {}
            perfil_numero = 'perfil_%s' % i
            perfil['title'] = getattr(self.data, perfil_numero)
            if perfil['title']:
                perfil['links'] = self.get_links(perfil_numero)
                perfis.append(perfil)
        return perfis

    @memoize
    def get_links(self, perfil):
        ''' funcao que retorna os links de cada perfil
        '''
        links = []

        for i in range(1,5):
            link = {}
            link['title'] = getattr(self.data, '%s_link0%s_titulo' % (perfil, i))
            link['url'] = getattr(self.data, '%s_link0%s_url' % (perfil, i))
            if all(link.values()):
                links.append(link)
        return links


class AddForm(base.AddForm):
    form_fields = form.Fields(IPerfil)
    label = _(u"Adicionar o Portlet de Perfil")
    description = _(u"")

    def create(self, data):
        return Assignment(sumario = data.get('sumario', ''),
            perfil_1 = data.get('perfil_1',''),
            perfil_1_link01_titulo = data.get('perfil_1_link01_titulo', ''),
            perfil_1_link01_url = data.get('perfil_1_link01_url', ''),
            perfil_1_link02_titulo = data.get('perfil_1_link02_titulo', ''),
            perfil_1_link02_url = data.get('perfil_1_link02_url', ''),
            perfil_1_link03_titulo = data.get('perfil_1_link03_titulo', ''),
            perfil_1_link03_url = data.get('perfil_1_link03_url', ''),
            perfil_1_link04_titulo = data.get('perfil_1_link04_titulo', ''),
            perfil_1_link04_url = data.get('perfil_1_link04_url', ''),
            perfil_2 = data.get('perfil_2',''),
            perfil_2_link01_titulo = data.get('perfil_2_link01_titulo', ''),
            perfil_2_link01_url = data.get('perfil_2_link01_url', ''),
            perfil_2_link02_titulo = data.get('perfil_2_link02_titulo', ''),
            perfil_2_link02_url = data.get('perfil_2_link02_url', ''),
            perfil_2_link03_titulo = data.get('perfil_2_link03_titulo', ''),
            perfil_2_link03_url = data.get('perfil_2_link03_url', ''),
            perfil_2_link04_titulo = data.get('perfil_2_link04_titulo', ''),
            perfil_2_link04_url = data.get('perfil_2_link04_url', ''),
            perfil_3 = data.get('perfil_3',''),
            perfil_3_link01_titulo = data.get('perfil_3_link01_titulo', ''),
            perfil_3_link01_url = data.get('perfil_3_link01_url', ''),
            perfil_3_link02_titulo = data.get('perfil_3_link02_titulo', ''),
            perfil_3_link02_url = data.get('perfil_3_link02_url', ''),
            perfil_3_link03_titulo = data.get('perfil_3_link03_titulo', ''),
            perfil_3_link03_url = data.get('perfil_3_link03_url', ''),
            perfil_3_link04_titulo = data.get('perfil_3_link04_titulo', ''),
            perfil_3_link04_url = data.get('perfil_3_link04_url', ''),
            perfil_4 = data.get('perfil_4',''),
            perfil_4_link01_titulo = data.get('perfil_4_link01_titulo', ''),
            perfil_4_link01_url = data.get('perfil_4_link01_url', ''),
            perfil_4_link02_titulo = data.get('perfil_4_link02_titulo', ''),
            perfil_4_link02_url = data.get('perfil_4_link02_url', ''),
            perfil_4_link03_titulo = data.get('perfil_4_link03_titulo', ''),
            perfil_4_link03_url = data.get('perfil_4_link03_url', ''),
            perfil_4_link04_titulo = data.get('perfil_4_link04_titulo', ''),
            perfil_4_link04_url = data.get('perfil_4_link04_url', ''),
            perfil_5 = data.get('perfil_5',''),
            perfil_5_link01_titulo = data.get('perfil_5_link01_titulo', ''),
            perfil_5_link01_url = data.get('perfil_5_link01_url', ''),
            perfil_5_link02_titulo = data.get('perfil_5_link02_titulo', ''),
            perfil_5_link02_url = data.get('perfil_5_link02_url', ''),
            perfil_5_link03_titulo = data.get('perfil_5_link03_titulo', ''),
            perfil_5_link03_url = data.get('perfil_5_link03_url', ''),
            perfil_5_link04_titulo = data.get('perfil_5_link04_titulo', ''),
            perfil_5_link04_url = data.get('perfil_5_link04_url', ''),
            perfil_6 = data.get('perfil_6',''),
            perfil_6_link01_titulo = data.get('perfil_6_link01_titulo', ''),
            perfil_6_link01_url = data.get('perfil_6_link01_url', ''),
            perfil_6_link02_titulo = data.get('perfil_6_link02_titulo', ''),
            perfil_6_link02_url = data.get('perfil_6_link02_url', ''),
            perfil_6_link03_titulo = data.get('perfil_6_link03_titulo', ''),
            perfil_6_link03_url = data.get('perfil_6_link03_url', ''),
            perfil_6_link04_titulo = data.get('perfil_6_link04_titulo', ''),
            perfil_6_link04_url = data.get('perfil_6_link04_url', ''),
            perfil_7 = data.get('perfil_7',''),
            perfil_7_link01_titulo = data.get('perfil_7_link01_titulo', ''),
            perfil_7_link01_url = data.get('perfil_7_link01_url', ''),
            perfil_7_link02_titulo = data.get('perfil_7_link02_titulo', ''),
            perfil_7_link02_url = data.get('perfil_7_link02_url', ''),
            perfil_7_link03_titulo = data.get('perfil_7_link03_titulo', ''),
            perfil_7_link03_url = data.get('perfil_7_link03_url', ''),
            perfil_7_link04_titulo = data.get('perfil_7_link04_titulo', ''),
            perfil_7_link04_url = data.get('perfil_7_link04_url', ''),
            perfil_8 = data.get('perfil_8',''),
            perfil_8_link01_titulo = data.get('perfil_8_link01_titulo', ''),
            perfil_8_link01_url = data.get('perfil_8_link01_url', ''),
            perfil_8_link02_titulo = data.get('perfil_8_link02_titulo', ''),
            perfil_8_link02_url = data.get('perfil_8_link02_url', ''),
            perfil_8_link03_titulo = data.get('perfil_8_link03_titulo', ''),
            perfil_8_link03_url = data.get('perfil_8_link03_url', ''),
            perfil_8_link04_titulo = data.get('perfil_8_link04_titulo', ''),
            perfil_8_link04_url = data.get('perfil_8_link04_url', ''))


class EditForm(base.EditForm):
    form_fields = form.Fields(IPerfil)
    label = _(u"Editar o Portlet de Perfil")
    description = _(u"")
