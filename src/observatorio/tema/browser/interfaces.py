# -*- coding: utf-8 -*-

from zope.interface import Interface


class IDropdownMenuViewlet(Interface):
    """
    """

    def getTabObject(tabUrl=''):
        """Get the submenu tree for tab object"""
