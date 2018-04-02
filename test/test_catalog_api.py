# coding: utf-8

"""
    Dynamix

    Sign up for Dynamix & grab your token.  # noqa: E501

    OpenAPI spec version: v0.1.0
    Contact: david@theadsontop.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.catalog_api import CatalogApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCatalogApi(unittest.TestCase):
    """CatalogApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.catalog_api.CatalogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_catalog_item(self):
        """Test case for create_catalog_item

        Create a catalog item  # noqa: E501
        """
        pass

    def test_delete_catalog_item(self):
        """Test case for delete_catalog_item

        Delete a Catalog entry  # noqa: E501
        """
        pass

    def test_get_catalog_item(self):
        """Test case for get_catalog_item

        Get a single Catalog Item  # noqa: E501
        """
        pass

    def test_get_catalog_items(self):
        """Test case for get_catalog_items

        Get Catalog Items Paged  # noqa: E501
        """
        pass

    def test_list_catalog(self):
        """Test case for list_catalog

        List the Catalog entries  # noqa: E501
        """
        pass

    def test_list_catalog_0(self):
        """Test case for list_catalog_0

        List the Catalog entries  # noqa: E501
        """
        pass

    def test_update_catalog_item(self):
        """Test case for update_catalog_item

        Update a Catalog entry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()