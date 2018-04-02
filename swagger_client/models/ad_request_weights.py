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


class AdRequestWeights(object):
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
        'ad_size_info': 'float',
        'ad_restrictions': 'float',
        'publisher_location_info': 'float',
        'time_info': 'float',
        'publisher_history_info': 'float',
        'monetary_requirement_info': 'float',
        'impression_info': 'float',
        'internet_info': 'float'
    }

    attribute_map = {
        'ad_size_info': 'adSizeInfo',
        'ad_restrictions': 'adRestrictions',
        'publisher_location_info': 'publisherLocationInfo',
        'time_info': 'timeInfo',
        'publisher_history_info': 'publisherHistoryInfo',
        'monetary_requirement_info': 'monetaryRequirementInfo',
        'impression_info': 'impressionInfo',
        'internet_info': 'internetInfo'
    }

    def __init__(self, ad_size_info=None, ad_restrictions=None, publisher_location_info=None, time_info=None, publisher_history_info=None, monetary_requirement_info=None, impression_info=None, internet_info=None):  # noqa: E501
        """AdRequestWeights - a model defined in Swagger"""  # noqa: E501

        self._ad_size_info = None
        self._ad_restrictions = None
        self._publisher_location_info = None
        self._time_info = None
        self._publisher_history_info = None
        self._monetary_requirement_info = None
        self._impression_info = None
        self._internet_info = None
        self.discriminator = None

        if ad_size_info is not None:
            self.ad_size_info = ad_size_info
        if ad_restrictions is not None:
            self.ad_restrictions = ad_restrictions
        if publisher_location_info is not None:
            self.publisher_location_info = publisher_location_info
        if time_info is not None:
            self.time_info = time_info
        if publisher_history_info is not None:
            self.publisher_history_info = publisher_history_info
        if monetary_requirement_info is not None:
            self.monetary_requirement_info = monetary_requirement_info
        if impression_info is not None:
            self.impression_info = impression_info
        if internet_info is not None:
            self.internet_info = internet_info

    @property
    def ad_size_info(self):
        """Gets the ad_size_info of this AdRequestWeights.  # noqa: E501


        :return: The ad_size_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._ad_size_info

    @ad_size_info.setter
    def ad_size_info(self, ad_size_info):
        """Sets the ad_size_info of this AdRequestWeights.


        :param ad_size_info: The ad_size_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._ad_size_info = ad_size_info

    @property
    def ad_restrictions(self):
        """Gets the ad_restrictions of this AdRequestWeights.  # noqa: E501


        :return: The ad_restrictions of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._ad_restrictions

    @ad_restrictions.setter
    def ad_restrictions(self, ad_restrictions):
        """Sets the ad_restrictions of this AdRequestWeights.


        :param ad_restrictions: The ad_restrictions of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._ad_restrictions = ad_restrictions

    @property
    def publisher_location_info(self):
        """Gets the publisher_location_info of this AdRequestWeights.  # noqa: E501


        :return: The publisher_location_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._publisher_location_info

    @publisher_location_info.setter
    def publisher_location_info(self, publisher_location_info):
        """Sets the publisher_location_info of this AdRequestWeights.


        :param publisher_location_info: The publisher_location_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._publisher_location_info = publisher_location_info

    @property
    def time_info(self):
        """Gets the time_info of this AdRequestWeights.  # noqa: E501


        :return: The time_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._time_info

    @time_info.setter
    def time_info(self, time_info):
        """Sets the time_info of this AdRequestWeights.


        :param time_info: The time_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._time_info = time_info

    @property
    def publisher_history_info(self):
        """Gets the publisher_history_info of this AdRequestWeights.  # noqa: E501


        :return: The publisher_history_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._publisher_history_info

    @publisher_history_info.setter
    def publisher_history_info(self, publisher_history_info):
        """Sets the publisher_history_info of this AdRequestWeights.


        :param publisher_history_info: The publisher_history_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._publisher_history_info = publisher_history_info

    @property
    def monetary_requirement_info(self):
        """Gets the monetary_requirement_info of this AdRequestWeights.  # noqa: E501


        :return: The monetary_requirement_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._monetary_requirement_info

    @monetary_requirement_info.setter
    def monetary_requirement_info(self, monetary_requirement_info):
        """Sets the monetary_requirement_info of this AdRequestWeights.


        :param monetary_requirement_info: The monetary_requirement_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._monetary_requirement_info = monetary_requirement_info

    @property
    def impression_info(self):
        """Gets the impression_info of this AdRequestWeights.  # noqa: E501


        :return: The impression_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._impression_info

    @impression_info.setter
    def impression_info(self, impression_info):
        """Sets the impression_info of this AdRequestWeights.


        :param impression_info: The impression_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._impression_info = impression_info

    @property
    def internet_info(self):
        """Gets the internet_info of this AdRequestWeights.  # noqa: E501


        :return: The internet_info of this AdRequestWeights.  # noqa: E501
        :rtype: float
        """
        return self._internet_info

    @internet_info.setter
    def internet_info(self, internet_info):
        """Sets the internet_info of this AdRequestWeights.


        :param internet_info: The internet_info of this AdRequestWeights.  # noqa: E501
        :type: float
        """

        self._internet_info = internet_info

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
        if not isinstance(other, AdRequestWeights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other