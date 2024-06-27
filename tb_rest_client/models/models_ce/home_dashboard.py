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

class HomeDashboard(object):
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
        'id': 'DashboardId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'title': 'str',
        'image': 'str',
        'assigned_customers': 'list[ShortCustomerInfo]',
        'mobile_hide': 'bool',
        'mobile_order': 'int',
        'hide_dashboard_toolbar': 'bool',
        'configuration': 'JsonNode',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'title': 'title',
        'image': 'image',
        'assigned_customers': 'assignedCustomers',
        'mobile_hide': 'mobileHide',
        'mobile_order': 'mobileOrder',
        'hide_dashboard_toolbar': 'hideDashboardToolbar',
        'configuration': 'configuration',
        'name': 'name'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, title=None, image=None, assigned_customers=None, mobile_hide=None, mobile_order=None, hide_dashboard_toolbar=None, configuration=None, name=None):  # noqa: E501
        """HomeDashboard - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._title = None
        self._image = None
        self._assigned_customers = None
        self._mobile_hide = None
        self._mobile_order = None
        self._hide_dashboard_toolbar = None
        self._configuration = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.title = title
        if image is not None:
            self.image = image
        if assigned_customers is not None:
            self.assigned_customers = assigned_customers
        if mobile_hide is not None:
            self.mobile_hide = mobile_hide
        if mobile_order is not None:
            self.mobile_order = mobile_order
        if hide_dashboard_toolbar is not None:
            self.hide_dashboard_toolbar = hide_dashboard_toolbar
        if configuration is not None:
            self.configuration = configuration
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this HomeDashboard.  # noqa: E501


        :return: The id of this HomeDashboard.  # noqa: E501
        :rtype: DashboardId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HomeDashboard.


        :param id: The id of this HomeDashboard.  # noqa: E501
        :type: DashboardId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this HomeDashboard.  # noqa: E501

        Timestamp of the dashboard creation, in milliseconds  # noqa: E501

        :return: The created_time of this HomeDashboard.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this HomeDashboard.

        Timestamp of the dashboard creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this HomeDashboard.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this HomeDashboard.  # noqa: E501


        :return: The tenant_id of this HomeDashboard.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this HomeDashboard.


        :param tenant_id: The tenant_id of this HomeDashboard.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """Gets the title of this HomeDashboard.  # noqa: E501

        Title of the dashboard.  # noqa: E501

        :return: The title of this HomeDashboard.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this HomeDashboard.

        Title of the dashboard.  # noqa: E501

        :param title: The title of this HomeDashboard.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def image(self):
        """Gets the image of this HomeDashboard.  # noqa: E501

        Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.  # noqa: E501

        :return: The image of this HomeDashboard.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this HomeDashboard.

        Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.  # noqa: E501

        :param image: The image of this HomeDashboard.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def assigned_customers(self):
        """Gets the assigned_customers of this HomeDashboard.  # noqa: E501

        List of assigned customers with their info.  # noqa: E501

        :return: The assigned_customers of this HomeDashboard.  # noqa: E501
        :rtype: list[ShortCustomerInfo]
        """
        return self._assigned_customers

    @assigned_customers.setter
    def assigned_customers(self, assigned_customers):
        """Sets the assigned_customers of this HomeDashboard.

        List of assigned customers with their info.  # noqa: E501

        :param assigned_customers: The assigned_customers of this HomeDashboard.  # noqa: E501
        :type: list[ShortCustomerInfo]
        """

        self._assigned_customers = assigned_customers

    @property
    def mobile_hide(self):
        """Gets the mobile_hide of this HomeDashboard.  # noqa: E501

        Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.  # noqa: E501

        :return: The mobile_hide of this HomeDashboard.  # noqa: E501
        :rtype: bool
        """
        return self._mobile_hide

    @mobile_hide.setter
    def mobile_hide(self, mobile_hide):
        """Sets the mobile_hide of this HomeDashboard.

        Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.  # noqa: E501

        :param mobile_hide: The mobile_hide of this HomeDashboard.  # noqa: E501
        :type: bool
        """

        self._mobile_hide = mobile_hide

    @property
    def mobile_order(self):
        """Gets the mobile_order of this HomeDashboard.  # noqa: E501

        Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications  # noqa: E501

        :return: The mobile_order of this HomeDashboard.  # noqa: E501
        :rtype: int
        """
        return self._mobile_order

    @mobile_order.setter
    def mobile_order(self, mobile_order):
        """Sets the mobile_order of this HomeDashboard.

        Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications  # noqa: E501

        :param mobile_order: The mobile_order of this HomeDashboard.  # noqa: E501
        :type: int
        """

        self._mobile_order = mobile_order

    @property
    def hide_dashboard_toolbar(self):
        """Gets the hide_dashboard_toolbar of this HomeDashboard.  # noqa: E501

        Hide dashboard toolbar flag. Useful for rendering dashboards on mobile.  # noqa: E501

        :return: The hide_dashboard_toolbar of this HomeDashboard.  # noqa: E501
        :rtype: bool
        """
        return self._hide_dashboard_toolbar

    @hide_dashboard_toolbar.setter
    def hide_dashboard_toolbar(self, hide_dashboard_toolbar):
        """Sets the hide_dashboard_toolbar of this HomeDashboard.

        Hide dashboard toolbar flag. Useful for rendering dashboards on mobile.  # noqa: E501

        :param hide_dashboard_toolbar: The hide_dashboard_toolbar of this HomeDashboard.  # noqa: E501
        :type: bool
        """

        self._hide_dashboard_toolbar = hide_dashboard_toolbar

    @property
    def configuration(self):
        """Gets the configuration of this HomeDashboard.  # noqa: E501


        :return: The configuration of this HomeDashboard.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this HomeDashboard.


        :param configuration: The configuration of this HomeDashboard.  # noqa: E501
        :type: JsonNode
        """

        self._configuration = configuration

    @property
    def name(self):
        """Gets the name of this HomeDashboard.  # noqa: E501

        Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.  # noqa: E501

        :return: The name of this HomeDashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HomeDashboard.

        Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.  # noqa: E501

        :param name: The name of this HomeDashboard.  # noqa: E501
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
        if issubclass(HomeDashboard, dict):
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
        if not isinstance(other, HomeDashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
