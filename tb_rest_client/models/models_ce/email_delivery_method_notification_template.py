# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_ce.delivery_method_notification_template import DeliveryMethodNotificationTemplate  # noqa: F401,E501

class EmailDeliveryMethodNotificationTemplate(DeliveryMethodNotificationTemplate):
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
        'body': 'str',
        'enabled': 'bool',
        'subject': 'str'
    }
    if hasattr(DeliveryMethodNotificationTemplate, "swagger_types"):
        swagger_types.update(DeliveryMethodNotificationTemplate.swagger_types)

    attribute_map = {
        'body': 'body',
        'enabled': 'enabled',
        'subject': 'subject'
    }
    if hasattr(DeliveryMethodNotificationTemplate, "attribute_map"):
        attribute_map.update(DeliveryMethodNotificationTemplate.attribute_map)

    def __init__(self, body=None, enabled=None, subject=None, *args, **kwargs):  # noqa: E501
        """EmailDeliveryMethodNotificationTemplate - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._enabled = None
        self._subject = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if enabled is not None:
            self.enabled = enabled
        if subject is not None:
            self.subject = subject
        DeliveryMethodNotificationTemplate.__init__(self, *args, **kwargs)

    @property
    def body(self):
        """Gets the body of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The body of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EmailDeliveryMethodNotificationTemplate.


        :param body: The body of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def enabled(self):
        """Gets the enabled of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The enabled of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EmailDeliveryMethodNotificationTemplate.


        :param enabled: The enabled of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def subject(self):
        """Gets the subject of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The subject of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailDeliveryMethodNotificationTemplate.


        :param subject: The subject of this EmailDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if issubclass(EmailDeliveryMethodNotificationTemplate, dict):
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
        if not isinstance(other, EmailDeliveryMethodNotificationTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other