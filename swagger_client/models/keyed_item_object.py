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


class KeyedItemObject(object):
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
        'rid': 'str',
        'item': 'object'
    }

    attribute_map = {
        'rid': 'rid',
        'item': 'item'
    }

    def __init__(self, rid=None, item=None):  # noqa: E501
        """KeyedItemObject - a model defined in Swagger"""  # noqa: E501

        self._rid = None
        self._item = None
        self.discriminator = None

        if rid is not None:
            self.rid = rid
        if item is not None:
            self.item = item

    @property
    def rid(self):
        """Gets the rid of this KeyedItemObject.  # noqa: E501


        :return: The rid of this KeyedItemObject.  # noqa: E501
        :rtype: str
        """
        return self._rid

    @rid.setter
    def rid(self, rid):
        """Sets the rid of this KeyedItemObject.


        :param rid: The rid of this KeyedItemObject.  # noqa: E501
        :type: str
        """

        self._rid = rid

    @property
    def item(self):
        """Gets the item of this KeyedItemObject.  # noqa: E501


        :return: The item of this KeyedItemObject.  # noqa: E501
        :rtype: object
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this KeyedItemObject.


        :param item: The item of this KeyedItemObject.  # noqa: E501
        :type: object
        """

        self._item = item

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
        if not isinstance(other, KeyedItemObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
