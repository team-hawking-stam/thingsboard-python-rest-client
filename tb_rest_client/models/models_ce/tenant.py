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

class Tenant(object):
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
        'id': 'TenantId',
        'created_time': 'int',
        'country': 'str',
        'state': 'str',
        'city': 'str',
        'address': 'str',
        'address2': 'str',
        'zip': 'str',
        'phone': 'str',
        'email': 'str',
        'title': 'str',
        'region': 'str',
        'tenant_profile_id': 'TenantProfileId',
        'version': 'int',
        'name': 'str',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'address': 'address',
        'address2': 'address2',
        'zip': 'zip',
        'phone': 'phone',
        'email': 'email',
        'title': 'title',
        'region': 'region',
        'tenant_profile_id': 'tenantProfileId',
        'version': 'version',
        'name': 'name',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, country=None, state=None, city=None, address=None, address2=None, zip=None, phone=None, email=None, title=None, region=None, tenant_profile_id=None, version=None, name=None, additional_info=None):  # noqa: E501
        """Tenant - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._country = None
        self._state = None
        self._city = None
        self._address = None
        self._address2 = None
        self._zip = None
        self._phone = None
        self._email = None
        self._title = None
        self._region = None
        self._tenant_profile_id = None
        self._version = None
        self._name = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if city is not None:
            self.city = city
        if address is not None:
            self.address = address
        if address2 is not None:
            self.address2 = address2
        if zip is not None:
            self.zip = zip
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        self.title = title
        if region is not None:
            self.region = region
        if tenant_profile_id is not None:
            self.tenant_profile_id = tenant_profile_id
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this Tenant.  # noqa: E501


        :return: The id of this Tenant.  # noqa: E501
        :rtype: TenantId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tenant.


        :param id: The id of this Tenant.  # noqa: E501
        :type: TenantId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this Tenant.  # noqa: E501

        Timestamp of the tenant creation, in milliseconds  # noqa: E501

        :return: The created_time of this Tenant.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Tenant.

        Timestamp of the tenant creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Tenant.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def country(self):
        """Gets the country of this Tenant.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Tenant.

        Country  # noqa: E501

        :param country: The country of this Tenant.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this Tenant.  # noqa: E501

        State  # noqa: E501

        :return: The state of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Tenant.

        State  # noqa: E501

        :param state: The state of this Tenant.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def city(self):
        """Gets the city of this Tenant.  # noqa: E501

        City  # noqa: E501

        :return: The city of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Tenant.

        City  # noqa: E501

        :param city: The city of this Tenant.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def address(self):
        """Gets the address of this Tenant.  # noqa: E501

        Address Line 1  # noqa: E501

        :return: The address of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Tenant.

        Address Line 1  # noqa: E501

        :param address: The address of this Tenant.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Tenant.  # noqa: E501

        Address Line 2  # noqa: E501

        :return: The address2 of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Tenant.

        Address Line 2  # noqa: E501

        :param address2: The address2 of this Tenant.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def zip(self):
        """Gets the zip of this Tenant.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Tenant.

        Zip code  # noqa: E501

        :param zip: The zip of this Tenant.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this Tenant.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Tenant.

        Phone number  # noqa: E501

        :param phone: The phone of this Tenant.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Tenant.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Tenant.

        Email  # noqa: E501

        :param email: The email of this Tenant.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def title(self):
        """Gets the title of this Tenant.  # noqa: E501

        Title of the tenant  # noqa: E501

        :return: The title of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Tenant.

        Title of the tenant  # noqa: E501

        :param title: The title of this Tenant.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def region(self):
        """Gets the region of this Tenant.  # noqa: E501

        Geo region of the tenant  # noqa: E501

        :return: The region of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Tenant.

        Geo region of the tenant  # noqa: E501

        :param region: The region of this Tenant.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def tenant_profile_id(self):
        """Gets the tenant_profile_id of this Tenant.  # noqa: E501


        :return: The tenant_profile_id of this Tenant.  # noqa: E501
        :rtype: TenantProfileId
        """
        return self._tenant_profile_id

    @tenant_profile_id.setter
    def tenant_profile_id(self, tenant_profile_id):
        """Sets the tenant_profile_id of this Tenant.


        :param tenant_profile_id: The tenant_profile_id of this Tenant.  # noqa: E501
        :type: TenantProfileId
        """

        self._tenant_profile_id = tenant_profile_id

    @property
    def version(self):
        """Gets the version of this Tenant.  # noqa: E501


        :return: The version of this Tenant.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Tenant.


        :param version: The version of this Tenant.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this Tenant.  # noqa: E501

        Name of the tenant. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :return: The name of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tenant.

        Name of the tenant. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :param name: The name of this Tenant.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def additional_info(self):
        """Gets the additional_info of this Tenant.  # noqa: E501


        :return: The additional_info of this Tenant.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Tenant.


        :param additional_info: The additional_info of this Tenant.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
        if issubclass(Tenant, dict):
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
        if not isinstance(other, Tenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
