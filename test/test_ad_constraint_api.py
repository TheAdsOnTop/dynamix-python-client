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
from swagger_client.api.ad_constraint_api import AdConstraintApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdConstraintApi(unittest.TestCase):
    """AdConstraintApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ad_constraint_api.AdConstraintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_constraints(self):
        """Test case for get_constraints

        AdConstraintResource - GetVector  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
