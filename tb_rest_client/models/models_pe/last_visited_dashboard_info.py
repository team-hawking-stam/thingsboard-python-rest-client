# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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

class LastVisitedDashboardInfo(object):
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
        'id': 'str',
        'title': 'str',
        'starred': 'bool',
        'last_visited': 'int'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'starred': 'starred',
        'last_visited': 'lastVisited'
    }

    def __init__(self, id=None, title=None, starred=None, last_visited=None):  # noqa: E501
        """LastVisitedDashboardInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._starred = None
        self._last_visited = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if starred is not None:
            self.starred = starred
        if last_visited is not None:
            self.last_visited = last_visited

    @property
    def id(self):
        """Gets the id of this LastVisitedDashboardInfo.  # noqa: E501

        JSON object with Dashboard id.  # noqa: E501

        :return: The id of this LastVisitedDashboardInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LastVisitedDashboardInfo.

        JSON object with Dashboard id.  # noqa: E501

        :param id: The id of this LastVisitedDashboardInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this LastVisitedDashboardInfo.  # noqa: E501

        Title of the dashboard.  # noqa: E501

        :return: The title of this LastVisitedDashboardInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LastVisitedDashboardInfo.

        Title of the dashboard.  # noqa: E501

        :param title: The title of this LastVisitedDashboardInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def starred(self):
        """Gets the starred of this LastVisitedDashboardInfo.  # noqa: E501

        Starred flag  # noqa: E501

        :return: The starred of this LastVisitedDashboardInfo.  # noqa: E501
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this LastVisitedDashboardInfo.

        Starred flag  # noqa: E501

        :param starred: The starred of this LastVisitedDashboardInfo.  # noqa: E501
        :type: bool
        """

        self._starred = starred

    @property
    def last_visited(self):
        """Gets the last_visited of this LastVisitedDashboardInfo.  # noqa: E501

        Last visit timestamp  # noqa: E501

        :return: The last_visited of this LastVisitedDashboardInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_visited

    @last_visited.setter
    def last_visited(self, last_visited):
        """Sets the last_visited of this LastVisitedDashboardInfo.

        Last visit timestamp  # noqa: E501

        :param last_visited: The last_visited of this LastVisitedDashboardInfo.  # noqa: E501
        :type: int
        """

        self._last_visited = last_visited

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
        if issubclass(LastVisitedDashboardInfo, dict):
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
        if not isinstance(other, LastVisitedDashboardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
