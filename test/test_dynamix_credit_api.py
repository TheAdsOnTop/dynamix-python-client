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
from swagger_client.api.dynamix_credit_api import DynamixCreditApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDynamixCreditApi(unittest.TestCase):
    """DynamixCreditApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.dynamix_credit_api.DynamixCreditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_credits(self):
        """Test case for add_credits

        Add credits to a vault.  # noqa: E501
        """
        pass

    def test_check_balance(self):
        """Test case for check_balance

        Checks the balance of a given vault.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
