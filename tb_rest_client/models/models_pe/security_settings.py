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

class SecuritySettings(object):
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
        'password_policy': 'UserPasswordPolicy',
        'max_failed_login_attempts': 'int',
        'user_lockout_notification_email': 'str'
    }

    attribute_map = {
        'password_policy': 'passwordPolicy',
        'max_failed_login_attempts': 'maxFailedLoginAttempts',
        'user_lockout_notification_email': 'userLockoutNotificationEmail'
    }

    def __init__(self, password_policy=None, max_failed_login_attempts=None, user_lockout_notification_email=None):  # noqa: E501
        """SecuritySettings - a model defined in Swagger"""  # noqa: E501
        self._password_policy = None
        self._max_failed_login_attempts = None
        self._user_lockout_notification_email = None
        self.discriminator = None
        if password_policy is not None:
            self.password_policy = password_policy
        if max_failed_login_attempts is not None:
            self.max_failed_login_attempts = max_failed_login_attempts
        if user_lockout_notification_email is not None:
            self.user_lockout_notification_email = user_lockout_notification_email

    @property
    def password_policy(self):
        """Gets the password_policy of this SecuritySettings.  # noqa: E501


        :return: The password_policy of this SecuritySettings.  # noqa: E501
        :rtype: UserPasswordPolicy
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """Sets the password_policy of this SecuritySettings.


        :param password_policy: The password_policy of this SecuritySettings.  # noqa: E501
        :type: UserPasswordPolicy
        """

        self._password_policy = password_policy

    @property
    def max_failed_login_attempts(self):
        """Gets the max_failed_login_attempts of this SecuritySettings.  # noqa: E501

        Maximum number of failed login attempts allowed before user account is locked.  # noqa: E501

        :return: The max_failed_login_attempts of this SecuritySettings.  # noqa: E501
        :rtype: int
        """
        return self._max_failed_login_attempts

    @max_failed_login_attempts.setter
    def max_failed_login_attempts(self, max_failed_login_attempts):
        """Sets the max_failed_login_attempts of this SecuritySettings.

        Maximum number of failed login attempts allowed before user account is locked.  # noqa: E501

        :param max_failed_login_attempts: The max_failed_login_attempts of this SecuritySettings.  # noqa: E501
        :type: int
        """

        self._max_failed_login_attempts = max_failed_login_attempts

    @property
    def user_lockout_notification_email(self):
        """Gets the user_lockout_notification_email of this SecuritySettings.  # noqa: E501

        Email to use for notifications about locked users.  # noqa: E501

        :return: The user_lockout_notification_email of this SecuritySettings.  # noqa: E501
        :rtype: str
        """
        return self._user_lockout_notification_email

    @user_lockout_notification_email.setter
    def user_lockout_notification_email(self, user_lockout_notification_email):
        """Sets the user_lockout_notification_email of this SecuritySettings.

        Email to use for notifications about locked users.  # noqa: E501

        :param user_lockout_notification_email: The user_lockout_notification_email of this SecuritySettings.  # noqa: E501
        :type: str
        """

        self._user_lockout_notification_email = user_lockout_notification_email

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
        if issubclass(SecuritySettings, dict):
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
        if not isinstance(other, SecuritySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
