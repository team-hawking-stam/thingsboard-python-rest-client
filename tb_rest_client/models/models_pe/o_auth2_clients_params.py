# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
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

class OAuth2ClientsParams(object):
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
        'domains_params': 'list[OAuth2ClientsDomainParams]',
        'enabled': 'bool'
    }

    attribute_map = {
        'domains_params': 'domainsParams',
        'enabled': 'enabled'
    }

    def __init__(self, domains_params=None, enabled=None):  # noqa: E501
        """OAuth2ClientsParams - a model defined in Swagger"""  # noqa: E501
        self._domains_params = None
        self._enabled = None
        self.discriminator = None
        if domains_params is not None:
            self.domains_params = domains_params
        if enabled is not None:
            self.enabled = enabled

    @property
    def domains_params(self):
        """Gets the domains_params of this OAuth2ClientsParams.  # noqa: E501


        :return: The domains_params of this OAuth2ClientsParams.  # noqa: E501
        :rtype: list[OAuth2ClientsDomainParams]
        """
        return self._domains_params

    @domains_params.setter
    def domains_params(self, domains_params):
        """Sets the domains_params of this OAuth2ClientsParams.


        :param domains_params: The domains_params of this OAuth2ClientsParams.  # noqa: E501
        :type: list[OAuth2ClientsDomainParams]
        """

        self._domains_params = domains_params

    @property
    def enabled(self):
        """Gets the enabled of this OAuth2ClientsParams.  # noqa: E501


        :return: The enabled of this OAuth2ClientsParams.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OAuth2ClientsParams.


        :param enabled: The enabled of this OAuth2ClientsParams.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(OAuth2ClientsParams, dict):
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
        if not isinstance(other, OAuth2ClientsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
