# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
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

class DeferredResultEntityDataDiff(object):
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
        'result': 'object',
        'set_or_expired': 'bool'
    }

    attribute_map = {
        'result': 'result',
        'set_or_expired': 'setOrExpired'
    }

    def __init__(self, result=None, set_or_expired=None):  # noqa: E501
        """DeferredResultEntityDataDiff - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._set_or_expired = None
        self.discriminator = None
        if result is not None:
            self.result = result
        if set_or_expired is not None:
            self.set_or_expired = set_or_expired

    @property
    def result(self):
        """Gets the result of this DeferredResultEntityDataDiff.  # noqa: E501


        :return: The result of this DeferredResultEntityDataDiff.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DeferredResultEntityDataDiff.


        :param result: The result of this DeferredResultEntityDataDiff.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def set_or_expired(self):
        """Gets the set_or_expired of this DeferredResultEntityDataDiff.  # noqa: E501


        :return: The set_or_expired of this DeferredResultEntityDataDiff.  # noqa: E501
        :rtype: bool
        """
        return self._set_or_expired

    @set_or_expired.setter
    def set_or_expired(self, set_or_expired):
        """Sets the set_or_expired of this DeferredResultEntityDataDiff.


        :param set_or_expired: The set_or_expired of this DeferredResultEntityDataDiff.  # noqa: E501
        :type: bool
        """

        self._set_or_expired = set_or_expired

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
        if issubclass(DeferredResultEntityDataDiff, dict):
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
        if not isinstance(other, DeferredResultEntityDataDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
