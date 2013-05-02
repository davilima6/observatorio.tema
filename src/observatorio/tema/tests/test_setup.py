# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from observatorio.tema.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of observatorio.tema into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if observatorio.tema is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('observatorio.tema'))

    def test_uninstall(self):
        """Test if observatorio.tema is cleanly uninstalled."""
        self.installer.uninstallProducts(['observatorio.tema'])
        self.assertFalse(self.installer.isProductInstalled('observatorio.tema'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IObservatorioTemaLayer is registered."""
        from observatorio.tema.interfaces import IObservatorioTemaLayer
        from plone.browserlayer import utils
        self.failUnless(IObservatorioTemaLayer in utils.registered_layers())
