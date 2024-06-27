# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0
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
from tb_rest_client.models.models_ce.entity_export_data_object import EntityExportDataObject  # noqa: F401,E501

class WidgetsBundleExportData(EntityExportDataObject):
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
        'entity': 'WidgetsBundle',
        'widgets': 'list[object]',
        'fqns': 'list[str]'
    }
    if hasattr(EntityExportDataObject, "swagger_types"):
        swagger_types.update(EntityExportDataObject.swagger_types)

    attribute_map = {
        'entity': 'entity',
        'widgets': 'widgets',
        'fqns': 'fqns'
    }
    if hasattr(EntityExportDataObject, "attribute_map"):
        attribute_map.update(EntityExportDataObject.attribute_map)

    def __init__(self, entity=None, widgets=None, fqns=None, *args, **kwargs):  # noqa: E501
        """WidgetsBundleExportData - a model defined in Swagger"""  # noqa: E501
        self._entity = None
        self._widgets = None
        self._fqns = None
        self.discriminator = None
        if entity is not None:
            self.entity = entity
        if widgets is not None:
            self.widgets = widgets
        if fqns is not None:
            self.fqns = fqns
        EntityExportDataObject.__init__(self, *args, **kwargs)

    @property
    def entity(self):
        """Gets the entity of this WidgetsBundleExportData.  # noqa: E501


        :return: The entity of this WidgetsBundleExportData.  # noqa: E501
        :rtype: WidgetsBundle
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this WidgetsBundleExportData.


        :param entity: The entity of this WidgetsBundleExportData.  # noqa: E501
        :type: WidgetsBundle
        """

        self._entity = entity

    @property
    def widgets(self):
        """Gets the widgets of this WidgetsBundleExportData.  # noqa: E501


        :return: The widgets of this WidgetsBundleExportData.  # noqa: E501
        :rtype: list[object]
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """Sets the widgets of this WidgetsBundleExportData.


        :param widgets: The widgets of this WidgetsBundleExportData.  # noqa: E501
        :type: list[object]
        """

        self._widgets = widgets

    @property
    def fqns(self):
        """Gets the fqns of this WidgetsBundleExportData.  # noqa: E501


        :return: The fqns of this WidgetsBundleExportData.  # noqa: E501
        :rtype: list[str]
        """
        return self._fqns

    @fqns.setter
    def fqns(self, fqns):
        """Sets the fqns of this WidgetsBundleExportData.


        :param fqns: The fqns of this WidgetsBundleExportData.  # noqa: E501
        :type: list[str]
        """

        self._fqns = fqns

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
        if issubclass(WidgetsBundleExportData, dict):
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
        if not isinstance(other, WidgetsBundleExportData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
