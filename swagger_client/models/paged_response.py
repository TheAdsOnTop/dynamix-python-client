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

from swagger_client.models.keyed_item_object import KeyedItemObject  # noqa: F401,E501


class PagedResponse(object):
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
        'items': 'list[KeyedItemObject]',
        'next_start_index': 'int',
        'request_page_size': 'int'
    }

    attribute_map = {
        'items': 'items',
        'next_start_index': 'nextStartIndex',
        'request_page_size': 'requestPageSize'
    }

    def __init__(self, items=None, next_start_index=None, request_page_size=None):  # noqa: E501
        """PagedResponse - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._next_start_index = None
        self._request_page_size = None
        self.discriminator = None

        self.items = items
        self.next_start_index = next_start_index
        self.request_page_size = request_page_size

    @property
    def items(self):
        """Gets the items of this PagedResponse.  # noqa: E501


        :return: The items of this PagedResponse.  # noqa: E501
        :rtype: list[KeyedItemObject]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PagedResponse.


        :param items: The items of this PagedResponse.  # noqa: E501
        :type: list[KeyedItemObject]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def next_start_index(self):
        """Gets the next_start_index of this PagedResponse.  # noqa: E501


        :return: The next_start_index of this PagedResponse.  # noqa: E501
        :rtype: int
        """
        return self._next_start_index

    @next_start_index.setter
    def next_start_index(self, next_start_index):
        """Sets the next_start_index of this PagedResponse.


        :param next_start_index: The next_start_index of this PagedResponse.  # noqa: E501
        :type: int
        """
        if next_start_index is None:
            raise ValueError("Invalid value for `next_start_index`, must not be `None`")  # noqa: E501

        self._next_start_index = next_start_index

    @property
    def request_page_size(self):
        """Gets the request_page_size of this PagedResponse.  # noqa: E501


        :return: The request_page_size of this PagedResponse.  # noqa: E501
        :rtype: int
        """
        return self._request_page_size

    @request_page_size.setter
    def request_page_size(self, request_page_size):
        """Sets the request_page_size of this PagedResponse.


        :param request_page_size: The request_page_size of this PagedResponse.  # noqa: E501
        :type: int
        """
        if request_page_size is None:
            raise ValueError("Invalid value for `request_page_size`, must not be `None`")  # noqa: E501

        self._request_page_size = request_page_size

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
        if not isinstance(other, PagedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
