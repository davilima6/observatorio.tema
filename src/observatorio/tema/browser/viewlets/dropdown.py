# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import implements

from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.layout.navigation.navtree import buildFolderTree
from plone.app.layout.navigation.root import getNavigationRoot

from Products.CMFPlone.browser.navtree import NavtreeQueryBuilder

from plone.app.portlets.portlets.navigation import Assignment

from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

#
# Import ram.cache feature and xhmtl_compression (removes whitespace and so on)
#
from plone.memoize.ram import cache
from plone.memoize.compress import xhtml_compress

from observatorio.tema.browser.interfaces import IDropdownMenuViewlet


class DropdownQueryBuilder(NavtreeQueryBuilder):
    """Build a folder tree query suitable for a dropdownmenu
    """

    def __init__(self, context):
        NavtreeQueryBuilder.__init__(self, context)
        self.query['path'] = {'query': '/'.join(context.getPhysicalPath()),
                              'navtree_start': 1,
                              'depth': 2}


class DropdownMenuViewlet(common.GlobalSectionsViewlet):
    """A custom version of the global navigation class that has to have
       dropdown menus for global navigation tabs objects based in
       webcouturier.dropdownmenu
    """
    implements(IDropdownMenuViewlet)

    def _render_cachekey(fun, self):

        context = aq_inner(self.context)

        anonymous = getToolByName(
            context, 'portal_membership').isAnonymousUser()

        def get_language(context, request):
            portal_state = getMultiAdapter(
                (context, request), name=u'plone_portal_state')
            return portal_state.locale().getLocaleID()

        return ''.join((
            self.selected_portal_tab,
            get_language(context, self.request),
            str(anonymous),
        ))

    _template = ViewPageTemplateFile('dropdown_sections.pt')

    @cache(_render_cachekey)
    def cached_viewlet(self):
        return xhtml_compress(self._template())

    def index(self):
        return self._template()

    recurse = ViewPageTemplateFile('dropdown_recurse.pt')

    def update(self):
        common.ViewletBase.update(self)  # Get portal_state and portal_url
        super(DropdownMenuViewlet, self).update()
        context = aq_inner(self.context)
        portal_props = getToolByName(context, 'portal_properties')
        self.properties = portal_props.navtree_properties
        self.navroot_path = getNavigationRoot(context)
        self.data = Assignment(root=self.navroot_path)

    def getTabObject(self, tabUrl='', tabPath=None):
        if tabUrl == self.portal_state.navigation_root_url():
            # We are at the navigation root
            return ''
        if tabPath is None:
            # get path for current tab's object
            try:
                # we are in Plone > 3.0.x
                tabPath = tabUrl.split(self.site_url)[-1]
            except AttributeError:
                # we are in Plone 3.0.x world
                tabPath = tabUrl.split(self.portal_url)[-1]

            if tabPath == '' or '/view' in tabPath:
                # It's either the 'Home' or Image tab. It can't have
                # any dropdown.
                return ''

            if tabPath.startswith("/"):
                tabPath = tabPath[1:]
            elif tabPath.endswith('/'):
                # we need a real path, without a slash that might appear
                # at the end of the path occasionally
                tabPath = str(tabPath.split('/')[0])

            if '%20' in tabPath:
                # we have the space in object's ID that has to be
                # converted to the real spaces
                tabPath = tabPath.replace('%20', ' ').strip()

        if tabPath == '':
            return ''

        portal = self.portal_state.portal()
        portal_path = '/'.join(portal.getPhysicalPath())

        if portal_path != self.navroot_path:
            portal = portal.restrictedTraverse(self.navroot_path)
        tabObj = portal.restrictedTraverse(tabPath, None)

        if tabObj is None:
            # just in case we have missed any possible path
            # in conditions above
            return ''

        strategy = getMultiAdapter((tabObj, self.data), INavtreeStrategy)
        queryBuilder = DropdownQueryBuilder(tabObj)
        query = queryBuilder()

        data = buildFolderTree(tabObj, obj=tabObj, query=query,
                               strategy=strategy)

        bottomLevel = self.data.bottomLevel or self.properties.getProperty(
            'bottomLevel', 0)

        return self.recurse(children=data.get('children', []), level=1,
                            bottomLevel=bottomLevel).strip()
