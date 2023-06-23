# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_ce.entity_filter import EntityFilter  # noqa: F401,E501

class EdgeTypeFilter(EntityFilter):
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
        'edge_name_filter': 'str',
        'edge_types': 'list[str]'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'edge_name_filter': 'edgeNameFilter',
        'edge_types': 'edgeTypes'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, edge_name_filter=None, edge_types=None, *args, **kwargs):  # noqa: E501
        """EdgeTypeFilter - a model defined in Swagger"""  # noqa: E501
        self._edge_name_filter = None
        self._edge_types = None
        self.discriminator = None
        if edge_name_filter is not None:
            self.edge_name_filter = edge_name_filter
        if edge_types is not None:
            self.edge_types = edge_types
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def edge_name_filter(self):
        """Gets the edge_name_filter of this EdgeTypeFilter.  # noqa: E501


        :return: The edge_name_filter of this EdgeTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._edge_name_filter

    @edge_name_filter.setter
    def edge_name_filter(self, edge_name_filter):
        """Sets the edge_name_filter of this EdgeTypeFilter.


        :param edge_name_filter: The edge_name_filter of this EdgeTypeFilter.  # noqa: E501
        :type: str
        """

        self._edge_name_filter = edge_name_filter

    @property
    def edge_types(self):
        """Gets the edge_types of this EdgeTypeFilter.  # noqa: E501


        :return: The edge_types of this EdgeTypeFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._edge_types

    @edge_types.setter
    def edge_types(self, edge_types):
        """Sets the edge_types of this EdgeTypeFilter.


        :param edge_types: The edge_types of this EdgeTypeFilter.  # noqa: E501
        :type: list[str]
        """

        self._edge_types = edge_types

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
        if issubclass(EdgeTypeFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EdgeTypeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
