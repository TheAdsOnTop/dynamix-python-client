# coding: utf-8

"""
    Dynamix

    Sign up for Dynamix & grab your token.  # noqa: E501

    OpenAPI spec version: v0.1.0
    Contact: david@theadsontop.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Currency(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'currency_code': 'str',
        'default_fraction_digits': 'int',
        'numeric_code': 'int',
        'display_name': 'str',
        'symbol': 'str'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'default_fraction_digits': 'defaultFractionDigits',
        'numeric_code': 'numericCode',
        'display_name': 'displayName',
        'symbol': 'symbol'
    }

    def __init__(self, currency_code=None, default_fraction_digits=None, numeric_code=None, display_name=None, symbol=None):  # noqa: E501
        """Currency - a model defined in Swagger"""  # noqa: E501

        self._currency_code = None
        self._default_fraction_digits = None
        self._numeric_code = None
        self._display_name = None
        self._symbol = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if default_fraction_digits is not None:
            self.default_fraction_digits = default_fraction_digits
        if numeric_code is not None:
            self.numeric_code = numeric_code
        if display_name is not None:
            self.display_name = display_name
        if symbol is not None:
            self.symbol = symbol

    @property
    def currency_code(self):
        """Gets the currency_code of this Currency.  # noqa: E501


        :return: The currency_code of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Currency.


        :param currency_code: The currency_code of this Currency.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def default_fraction_digits(self):
        """Gets the default_fraction_digits of this Currency.  # noqa: E501


        :return: The default_fraction_digits of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._default_fraction_digits

    @default_fraction_digits.setter
    def default_fraction_digits(self, default_fraction_digits):
        """Sets the default_fraction_digits of this Currency.


        :param default_fraction_digits: The default_fraction_digits of this Currency.  # noqa: E501
        :type: int
        """

        self._default_fraction_digits = default_fraction_digits

    @property
    def numeric_code(self):
        """Gets the numeric_code of this Currency.  # noqa: E501


        :return: The numeric_code of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._numeric_code

    @numeric_code.setter
    def numeric_code(self, numeric_code):
        """Sets the numeric_code of this Currency.


        :param numeric_code: The numeric_code of this Currency.  # noqa: E501
        :type: int
        """

        self._numeric_code = numeric_code

    @property
    def display_name(self):
        """Gets the display_name of this Currency.  # noqa: E501


        :return: The display_name of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Currency.


        :param display_name: The display_name of this Currency.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def symbol(self):
        """Gets the symbol of this Currency.  # noqa: E501


        :return: The symbol of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Currency.


        :param symbol: The symbol of this Currency.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Currency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
