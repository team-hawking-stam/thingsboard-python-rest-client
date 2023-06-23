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

class SignUpSelfRegistrationParams(object):
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
        'sign_up_text_message': 'str',
        'captcha_site_key': 'str',
        'captcha_version': 'str',
        'captcha_action': 'str',
        'show_privacy_policy': 'bool',
        'show_terms_of_use': 'bool'
    }

    attribute_map = {
        'sign_up_text_message': 'signUpTextMessage',
        'captcha_site_key': 'captchaSiteKey',
        'captcha_version': 'captchaVersion',
        'captcha_action': 'captchaAction',
        'show_privacy_policy': 'showPrivacyPolicy',
        'show_terms_of_use': 'showTermsOfUse'
    }

    def __init__(self, sign_up_text_message=None, captcha_site_key=None, captcha_version=None, captcha_action=None, show_privacy_policy=None, show_terms_of_use=None):  # noqa: E501
        """SignUpSelfRegistrationParams - a model defined in Swagger"""  # noqa: E501
        self._sign_up_text_message = None
        self._captcha_site_key = None
        self._captcha_version = None
        self._captcha_action = None
        self._show_privacy_policy = None
        self._show_terms_of_use = None
        self.discriminator = None
        if sign_up_text_message is not None:
            self.sign_up_text_message = sign_up_text_message
        if captcha_site_key is not None:
            self.captcha_site_key = captcha_site_key
        if captcha_version is not None:
            self.captcha_version = captcha_version
        if captcha_action is not None:
            self.captcha_action = captcha_action
        if show_privacy_policy is not None:
            self.show_privacy_policy = show_privacy_policy
        if show_terms_of_use is not None:
            self.show_terms_of_use = show_terms_of_use

    @property
    def sign_up_text_message(self):
        """Gets the sign_up_text_message of this SignUpSelfRegistrationParams.  # noqa: E501


        :return: The sign_up_text_message of this SignUpSelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._sign_up_text_message

    @sign_up_text_message.setter
    def sign_up_text_message(self, sign_up_text_message):
        """Sets the sign_up_text_message of this SignUpSelfRegistrationParams.


        :param sign_up_text_message: The sign_up_text_message of this SignUpSelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._sign_up_text_message = sign_up_text_message

    @property
    def captcha_site_key(self):
        """Gets the captcha_site_key of this SignUpSelfRegistrationParams.  # noqa: E501


        :return: The captcha_site_key of this SignUpSelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_site_key

    @captcha_site_key.setter
    def captcha_site_key(self, captcha_site_key):
        """Sets the captcha_site_key of this SignUpSelfRegistrationParams.


        :param captcha_site_key: The captcha_site_key of this SignUpSelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_site_key = captcha_site_key

    @property
    def captcha_version(self):
        """Gets the captcha_version of this SignUpSelfRegistrationParams.  # noqa: E501


        :return: The captcha_version of this SignUpSelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_version

    @captcha_version.setter
    def captcha_version(self, captcha_version):
        """Sets the captcha_version of this SignUpSelfRegistrationParams.


        :param captcha_version: The captcha_version of this SignUpSelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_version = captcha_version

    @property
    def captcha_action(self):
        """Gets the captcha_action of this SignUpSelfRegistrationParams.  # noqa: E501


        :return: The captcha_action of this SignUpSelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_action

    @captcha_action.setter
    def captcha_action(self, captcha_action):
        """Sets the captcha_action of this SignUpSelfRegistrationParams.


        :param captcha_action: The captcha_action of this SignUpSelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_action = captcha_action

    @property
    def show_privacy_policy(self):
        """Gets the show_privacy_policy of this SignUpSelfRegistrationParams.  # noqa: E501


        :return: The show_privacy_policy of this SignUpSelfRegistrationParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_privacy_policy

    @show_privacy_policy.setter
    def show_privacy_policy(self, show_privacy_policy):
        """Sets the show_privacy_policy of this SignUpSelfRegistrationParams.


        :param show_privacy_policy: The show_privacy_policy of this SignUpSelfRegistrationParams.  # noqa: E501
        :type: bool
        """

        self._show_privacy_policy = show_privacy_policy

    @property
    def show_terms_of_use(self):
        """Gets the show_terms_of_use of this SignUpSelfRegistrationParams.  # noqa: E501


        :return: The show_terms_of_use of this SignUpSelfRegistrationParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_terms_of_use

    @show_terms_of_use.setter
    def show_terms_of_use(self, show_terms_of_use):
        """Sets the show_terms_of_use of this SignUpSelfRegistrationParams.


        :param show_terms_of_use: The show_terms_of_use of this SignUpSelfRegistrationParams.  # noqa: E501
        :type: bool
        """

        self._show_terms_of_use = show_terms_of_use

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
        if issubclass(SignUpSelfRegistrationParams, dict):
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
        if not isinstance(other, SignUpSelfRegistrationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
