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

from swagger_client.models.ad_metadata import AdMetadata  # noqa: F401,E501
from swagger_client.models.aot_file import AotFile  # noqa: F401,E501
from swagger_client.models.object_node import ObjectNode  # noqa: F401,E501


class Ad(object):
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
        'file': 'AotFile',
        'ad_source_stream_rid': 'str',
        'ad_metadata': 'AdMetadata',
        'playback_price_in_cents': 'int',
        'custom_properties': 'ObjectNode',
        'read': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'ad_source_stream_rid': 'adSourceStreamRid',
        'ad_metadata': 'adMetadata',
        'playback_price_in_cents': 'playbackPriceInCents',
        'custom_properties': 'customProperties',
        'read': 'read'
    }

    def __init__(self, file=None, ad_source_stream_rid=None, ad_metadata=None, playback_price_in_cents=None, custom_properties=None, read=None):  # noqa: E501
        """Ad - a model defined in Swagger"""  # noqa: E501

        self._file = None
        self._ad_source_stream_rid = None
        self._ad_metadata = None
        self._playback_price_in_cents = None
        self._custom_properties = None
        self._read = None
        self.discriminator = None

        self.file = file
        self.ad_source_stream_rid = ad_source_stream_rid
        self.ad_metadata = ad_metadata
        self.playback_price_in_cents = playback_price_in_cents
        self.custom_properties = custom_properties
        if read is not None:
            self.read = read

    @property
    def file(self):
        """Gets the file of this Ad.  # noqa: E501


        :return: The file of this Ad.  # noqa: E501
        :rtype: AotFile
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Ad.


        :param file: The file of this Ad.  # noqa: E501
        :type: AotFile
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def ad_source_stream_rid(self):
        """Gets the ad_source_stream_rid of this Ad.  # noqa: E501


        :return: The ad_source_stream_rid of this Ad.  # noqa: E501
        :rtype: str
        """
        return self._ad_source_stream_rid

    @ad_source_stream_rid.setter
    def ad_source_stream_rid(self, ad_source_stream_rid):
        """Sets the ad_source_stream_rid of this Ad.


        :param ad_source_stream_rid: The ad_source_stream_rid of this Ad.  # noqa: E501
        :type: str
        """
        if ad_source_stream_rid is None:
            raise ValueError("Invalid value for `ad_source_stream_rid`, must not be `None`")  # noqa: E501

        self._ad_source_stream_rid = ad_source_stream_rid

    @property
    def ad_metadata(self):
        """Gets the ad_metadata of this Ad.  # noqa: E501


        :return: The ad_metadata of this Ad.  # noqa: E501
        :rtype: AdMetadata
        """
        return self._ad_metadata

    @ad_metadata.setter
    def ad_metadata(self, ad_metadata):
        """Sets the ad_metadata of this Ad.


        :param ad_metadata: The ad_metadata of this Ad.  # noqa: E501
        :type: AdMetadata
        """
        if ad_metadata is None:
            raise ValueError("Invalid value for `ad_metadata`, must not be `None`")  # noqa: E501

        self._ad_metadata = ad_metadata

    @property
    def playback_price_in_cents(self):
        """Gets the playback_price_in_cents of this Ad.  # noqa: E501


        :return: The playback_price_in_cents of this Ad.  # noqa: E501
        :rtype: int
        """
        return self._playback_price_in_cents

    @playback_price_in_cents.setter
    def playback_price_in_cents(self, playback_price_in_cents):
        """Sets the playback_price_in_cents of this Ad.


        :param playback_price_in_cents: The playback_price_in_cents of this Ad.  # noqa: E501
        :type: int
        """
        if playback_price_in_cents is None:
            raise ValueError("Invalid value for `playback_price_in_cents`, must not be `None`")  # noqa: E501

        self._playback_price_in_cents = playback_price_in_cents

    @property
    def custom_properties(self):
        """Gets the custom_properties of this Ad.  # noqa: E501


        :return: The custom_properties of this Ad.  # noqa: E501
        :rtype: ObjectNode
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this Ad.


        :param custom_properties: The custom_properties of this Ad.  # noqa: E501
        :type: ObjectNode
        """
        if custom_properties is None:
            raise ValueError("Invalid value for `custom_properties`, must not be `None`")  # noqa: E501

        self._custom_properties = custom_properties

    @property
    def read(self):
        """Gets the read of this Ad.  # noqa: E501


        :return: The read of this Ad.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this Ad.


        :param read: The read of this Ad.  # noqa: E501
        :type: bool
        """

        self._read = read

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
        if not isinstance(other, Ad):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other