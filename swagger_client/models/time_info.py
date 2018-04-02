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

from swagger_client.models.day_bounded_time_range import DayBoundedTimeRange  # noqa: F401,E501


class TimeInfo(object):
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
        'scheduled_play_time': 'int',
        'play_times': 'list[DayBoundedTimeRange]'
    }

    attribute_map = {
        'scheduled_play_time': 'scheduledPlayTime',
        'play_times': 'playTimes'
    }

    def __init__(self, scheduled_play_time=None, play_times=None):  # noqa: E501
        """TimeInfo - a model defined in Swagger"""  # noqa: E501

        self._scheduled_play_time = None
        self._play_times = None
        self.discriminator = None

        self.scheduled_play_time = scheduled_play_time
        self.play_times = play_times

    @property
    def scheduled_play_time(self):
        """Gets the scheduled_play_time of this TimeInfo.  # noqa: E501


        :return: The scheduled_play_time of this TimeInfo.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_play_time

    @scheduled_play_time.setter
    def scheduled_play_time(self, scheduled_play_time):
        """Sets the scheduled_play_time of this TimeInfo.


        :param scheduled_play_time: The scheduled_play_time of this TimeInfo.  # noqa: E501
        :type: int
        """
        if scheduled_play_time is None:
            raise ValueError("Invalid value for `scheduled_play_time`, must not be `None`")  # noqa: E501

        self._scheduled_play_time = scheduled_play_time

    @property
    def play_times(self):
        """Gets the play_times of this TimeInfo.  # noqa: E501


        :return: The play_times of this TimeInfo.  # noqa: E501
        :rtype: list[DayBoundedTimeRange]
        """
        return self._play_times

    @play_times.setter
    def play_times(self, play_times):
        """Sets the play_times of this TimeInfo.


        :param play_times: The play_times of this TimeInfo.  # noqa: E501
        :type: list[DayBoundedTimeRange]
        """
        if play_times is None:
            raise ValueError("Invalid value for `play_times`, must not be `None`")  # noqa: E501

        self._play_times = play_times

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
        if not isinstance(other, TimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other