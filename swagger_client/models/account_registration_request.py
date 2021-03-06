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

from swagger_client.models.user import User  # noqa: F401,E501


class AccountRegistrationRequest(object):
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
        'new_user': 'User'
    }

    attribute_map = {
        'new_user': 'newUser'
    }

    def __init__(self, new_user=None):  # noqa: E501
        """AccountRegistrationRequest - a model defined in Swagger"""  # noqa: E501

        self._new_user = None
        self.discriminator = None

        self.new_user = new_user

    @property
    def new_user(self):
        """Gets the new_user of this AccountRegistrationRequest.  # noqa: E501


        :return: The new_user of this AccountRegistrationRequest.  # noqa: E501
        :rtype: User
        """
        return self._new_user

    @new_user.setter
    def new_user(self, new_user):
        """Sets the new_user of this AccountRegistrationRequest.


        :param new_user: The new_user of this AccountRegistrationRequest.  # noqa: E501
        :type: User
        """
        if new_user is None:
            raise ValueError("Invalid value for `new_user`, must not be `None`")  # noqa: E501

        self._new_user = new_user

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
        if not isinstance(other, AccountRegistrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
