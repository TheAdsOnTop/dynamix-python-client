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

from swagger_client.models.ad_request_weights import AdRequestWeights  # noqa: F401,E501


class EnabledAdSource(object):
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
        'catalog_item_rid': 'str',
        'weight_vector': 'AdRequestWeights'
    }

    attribute_map = {
        'catalog_item_rid': 'catalogItemRid',
        'weight_vector': 'weightVector'
    }

    def __init__(self, catalog_item_rid=None, weight_vector=None):  # noqa: E501
        """EnabledAdSource - a model defined in Swagger"""  # noqa: E501

        self._catalog_item_rid = None
        self._weight_vector = None
        self.discriminator = None

        self.catalog_item_rid = catalog_item_rid
        self.weight_vector = weight_vector

    @property
    def catalog_item_rid(self):
        """Gets the catalog_item_rid of this EnabledAdSource.  # noqa: E501


        :return: The catalog_item_rid of this EnabledAdSource.  # noqa: E501
        :rtype: str
        """
        return self._catalog_item_rid

    @catalog_item_rid.setter
    def catalog_item_rid(self, catalog_item_rid):
        """Sets the catalog_item_rid of this EnabledAdSource.


        :param catalog_item_rid: The catalog_item_rid of this EnabledAdSource.  # noqa: E501
        :type: str
        """
        if catalog_item_rid is None:
            raise ValueError("Invalid value for `catalog_item_rid`, must not be `None`")  # noqa: E501

        self._catalog_item_rid = catalog_item_rid

    @property
    def weight_vector(self):
        """Gets the weight_vector of this EnabledAdSource.  # noqa: E501


        :return: The weight_vector of this EnabledAdSource.  # noqa: E501
        :rtype: AdRequestWeights
        """
        return self._weight_vector

    @weight_vector.setter
    def weight_vector(self, weight_vector):
        """Sets the weight_vector of this EnabledAdSource.


        :param weight_vector: The weight_vector of this EnabledAdSource.  # noqa: E501
        :type: AdRequestWeights
        """
        if weight_vector is None:
            raise ValueError("Invalid value for `weight_vector`, must not be `None`")  # noqa: E501

        self._weight_vector = weight_vector

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
        if not isinstance(other, EnabledAdSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other