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

class OAuth2ClientInfo(object):
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
        'id': 'OAuth2ClientId',
        'created_time': 'int',
        'title': 'str',
        'provider_name': 'str',
        'platforms': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'title': 'title',
        'provider_name': 'providerName',
        'platforms': 'platforms',
        'name': 'name'
    }

    def __init__(self, id=None, created_time=None, title=None, provider_name=None, platforms=None, name=None):  # noqa: E501
        """OAuth2ClientInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._title = None
        self._provider_name = None
        self._platforms = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if title is not None:
            self.title = title
        if provider_name is not None:
            self.provider_name = provider_name
        if platforms is not None:
            self.platforms = platforms
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this OAuth2ClientInfo.  # noqa: E501


        :return: The id of this OAuth2ClientInfo.  # noqa: E501
        :rtype: OAuth2ClientId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2ClientInfo.


        :param id: The id of this OAuth2ClientInfo.  # noqa: E501
        :type: OAuth2ClientId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this OAuth2ClientInfo.  # noqa: E501


        :return: The created_time of this OAuth2ClientInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OAuth2ClientInfo.


        :param created_time: The created_time of this OAuth2ClientInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def title(self):
        """Gets the title of this OAuth2ClientInfo.  # noqa: E501

        Oauth2 client registration title (e.g. My google)  # noqa: E501

        :return: The title of this OAuth2ClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OAuth2ClientInfo.

        Oauth2 client registration title (e.g. My google)  # noqa: E501

        :param title: The title of this OAuth2ClientInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def provider_name(self):
        """Gets the provider_name of this OAuth2ClientInfo.  # noqa: E501

        Oauth2 client provider name (e.g. Google)  # noqa: E501

        :return: The provider_name of this OAuth2ClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this OAuth2ClientInfo.

        Oauth2 client provider name (e.g. Google)  # noqa: E501

        :param provider_name: The provider_name of this OAuth2ClientInfo.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def platforms(self):
        """Gets the platforms of this OAuth2ClientInfo.  # noqa: E501

        List of platforms for which usage of the OAuth2 client is allowed (empty for all allowed)  # noqa: E501

        :return: The platforms of this OAuth2ClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this OAuth2ClientInfo.

        List of platforms for which usage of the OAuth2 client is allowed (empty for all allowed)  # noqa: E501

        :param platforms: The platforms of this OAuth2ClientInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["WEB", "ANDROID", "IOS"]  # noqa: E501
        if not set(platforms).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `platforms` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(platforms) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._platforms = platforms

    @property
    def name(self):
        """Gets the name of this OAuth2ClientInfo.  # noqa: E501


        :return: The name of this OAuth2ClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2ClientInfo.


        :param name: The name of this OAuth2ClientInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(OAuth2ClientInfo, dict):
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
        if not isinstance(other, OAuth2ClientInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
