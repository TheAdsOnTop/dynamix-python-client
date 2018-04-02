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

from swagger_client.models.ad import Ad  # noqa: F401,E501


class ReleasedAd(object):
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
        'ad': 'Ad',
        'ad_rid': 'str',
        'pop_query_params': 'str'
    }

    attribute_map = {
        'ad': 'ad',
        'ad_rid': 'adRid',
        'pop_query_params': 'popQueryParams'
    }

    def __init__(self, ad=None, ad_rid=None, pop_query_params=None):  # noqa: E501
        """ReleasedAd - a model defined in Swagger"""  # noqa: E501

        self._ad = None
        self._ad_rid = None
        self._pop_query_params = None
        self.discriminator = None

        self.ad = ad
        self.ad_rid = ad_rid
        self.pop_query_params = pop_query_params

    @property
    def ad(self):
        """Gets the ad of this ReleasedAd.  # noqa: E501

        Ad contents. This is what stores the ad delivery information.  # noqa: E501

        :return: The ad of this ReleasedAd.  # noqa: E501
        :rtype: Ad
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this ReleasedAd.

        Ad contents. This is what stores the ad delivery information.  # noqa: E501

        :param ad: The ad of this ReleasedAd.  # noqa: E501
        :type: Ad
        """
        if ad is None:
            raise ValueError("Invalid value for `ad`, must not be `None`")  # noqa: E501

        self._ad = ad

    @property
    def ad_rid(self):
        """Gets the ad_rid of this ReleasedAd.  # noqa: E501


        :return: The ad_rid of this ReleasedAd.  # noqa: E501
        :rtype: str
        """
        return self._ad_rid

    @ad_rid.setter
    def ad_rid(self, ad_rid):
        """Sets the ad_rid of this ReleasedAd.


        :param ad_rid: The ad_rid of this ReleasedAd.  # noqa: E501
        :type: str
        """
        if ad_rid is None:
            raise ValueError("Invalid value for `ad_rid`, must not be `None`")  # noqa: E501

        self._ad_rid = ad_rid

    @property
    def pop_query_params(self):
        """Gets the pop_query_params of this ReleasedAd.  # noqa: E501


        :return: The pop_query_params of this ReleasedAd.  # noqa: E501
        :rtype: str
        """
        return self._pop_query_params

    @pop_query_params.setter
    def pop_query_params(self, pop_query_params):
        """Sets the pop_query_params of this ReleasedAd.


        :param pop_query_params: The pop_query_params of this ReleasedAd.  # noqa: E501
        :type: str
        """
        if pop_query_params is None:
            raise ValueError("Invalid value for `pop_query_params`, must not be `None`")  # noqa: E501

        self._pop_query_params = pop_query_params

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
        if not isinstance(other, ReleasedAd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
