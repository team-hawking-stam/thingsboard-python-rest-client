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

class CustomerInfo(object):
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
        'id': 'CustomerId',
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
        'tenant_id': 'TenantId',
        'parent_customer_id': 'CustomerId',
        'version': 'int',
        'custom_menu_id': 'CustomMenuId',
        'owner_name': 'str',
        'groups': 'list[EntityInfo]',
        'name': 'str',
        'customer_id': 'CustomerId',
        'additional_info': 'JsonNode',
        'owner_id': 'EntityId'
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
        'tenant_id': 'tenantId',
        'parent_customer_id': 'parentCustomerId',
        'version': 'version',
        'custom_menu_id': 'customMenuId',
        'owner_name': 'ownerName',
        'groups': 'groups',
        'name': 'name',
        'customer_id': 'customerId',
        'additional_info': 'additionalInfo',
        'owner_id': 'ownerId'
    }

    def __init__(self, id=None, created_time=None, country=None, state=None, city=None, address=None, address2=None, zip=None, phone=None, email=None, title=None, tenant_id=None, parent_customer_id=None, version=None, custom_menu_id=None, owner_name=None, groups=None, name=None, customer_id=None, additional_info=None, owner_id=None):  # noqa: E501
        """CustomerInfo - a model defined in Swagger"""  # noqa: E501
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
        self._tenant_id = None
        self._parent_customer_id = None
        self._version = None
        self._custom_menu_id = None
        self._owner_name = None
        self._groups = None
        self._name = None
        self._customer_id = None
        self._additional_info = None
        self._owner_id = None
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
        self.email = email
        self.title = title
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if parent_customer_id is not None:
            self.parent_customer_id = parent_customer_id
        if version is not None:
            self.version = version
        if custom_menu_id is not None:
            self.custom_menu_id = custom_menu_id
        if owner_name is not None:
            self.owner_name = owner_name
        if groups is not None:
            self.groups = groups
        if name is not None:
            self.name = name
        if customer_id is not None:
            self.customer_id = customer_id
        if additional_info is not None:
            self.additional_info = additional_info
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def id(self):
        """Gets the id of this CustomerInfo.  # noqa: E501


        :return: The id of this CustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerInfo.


        :param id: The id of this CustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this CustomerInfo.  # noqa: E501

        Timestamp of the customer creation, in milliseconds  # noqa: E501

        :return: The created_time of this CustomerInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CustomerInfo.

        Timestamp of the customer creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this CustomerInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def country(self):
        """Gets the country of this CustomerInfo.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerInfo.

        Country  # noqa: E501

        :param country: The country of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this CustomerInfo.  # noqa: E501

        State  # noqa: E501

        :return: The state of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CustomerInfo.

        State  # noqa: E501

        :param state: The state of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def city(self):
        """Gets the city of this CustomerInfo.  # noqa: E501

        City  # noqa: E501

        :return: The city of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CustomerInfo.

        City  # noqa: E501

        :param city: The city of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def address(self):
        """Gets the address of this CustomerInfo.  # noqa: E501

        Address Line 1  # noqa: E501

        :return: The address of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerInfo.

        Address Line 1  # noqa: E501

        :param address: The address of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this CustomerInfo.  # noqa: E501

        Address Line 2  # noqa: E501

        :return: The address2 of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this CustomerInfo.

        Address Line 2  # noqa: E501

        :param address2: The address2 of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def zip(self):
        """Gets the zip of this CustomerInfo.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this CustomerInfo.

        Zip code  # noqa: E501

        :param zip: The zip of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this CustomerInfo.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CustomerInfo.

        Phone number  # noqa: E501

        :param phone: The phone of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this CustomerInfo.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerInfo.

        Email  # noqa: E501

        :param email: The email of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def title(self):
        """Gets the title of this CustomerInfo.  # noqa: E501

        Title of the customer  # noqa: E501

        :return: The title of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CustomerInfo.

        Title of the customer  # noqa: E501

        :param title: The title of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CustomerInfo.  # noqa: E501


        :return: The tenant_id of this CustomerInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CustomerInfo.


        :param tenant_id: The tenant_id of this CustomerInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def parent_customer_id(self):
        """Gets the parent_customer_id of this CustomerInfo.  # noqa: E501


        :return: The parent_customer_id of this CustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._parent_customer_id

    @parent_customer_id.setter
    def parent_customer_id(self, parent_customer_id):
        """Sets the parent_customer_id of this CustomerInfo.


        :param parent_customer_id: The parent_customer_id of this CustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._parent_customer_id = parent_customer_id

    @property
    def version(self):
        """Gets the version of this CustomerInfo.  # noqa: E501


        :return: The version of this CustomerInfo.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustomerInfo.


        :param version: The version of this CustomerInfo.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def custom_menu_id(self):
        """Gets the custom_menu_id of this CustomerInfo.  # noqa: E501


        :return: The custom_menu_id of this CustomerInfo.  # noqa: E501
        :rtype: CustomMenuId
        """
        return self._custom_menu_id

    @custom_menu_id.setter
    def custom_menu_id(self, custom_menu_id):
        """Sets the custom_menu_id of this CustomerInfo.


        :param custom_menu_id: The custom_menu_id of this CustomerInfo.  # noqa: E501
        :type: CustomMenuId
        """

        self._custom_menu_id = custom_menu_id

    @property
    def owner_name(self):
        """Gets the owner_name of this CustomerInfo.  # noqa: E501

        Owner name  # noqa: E501

        :return: The owner_name of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this CustomerInfo.

        Owner name  # noqa: E501

        :param owner_name: The owner_name of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def groups(self):
        """Gets the groups of this CustomerInfo.  # noqa: E501

        Groups  # noqa: E501

        :return: The groups of this CustomerInfo.  # noqa: E501
        :rtype: list[EntityInfo]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CustomerInfo.

        Groups  # noqa: E501

        :param groups: The groups of this CustomerInfo.  # noqa: E501
        :type: list[EntityInfo]
        """

        self._groups = groups

    @property
    def name(self):
        """Gets the name of this CustomerInfo.  # noqa: E501

        Name of the customer. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :return: The name of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerInfo.

        Name of the customer. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :param name: The name of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerInfo.  # noqa: E501


        :return: The customer_id of this CustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerInfo.


        :param customer_id: The customer_id of this CustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def additional_info(self):
        """Gets the additional_info of this CustomerInfo.  # noqa: E501


        :return: The additional_info of this CustomerInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CustomerInfo.


        :param additional_info: The additional_info of this CustomerInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def owner_id(self):
        """Gets the owner_id of this CustomerInfo.  # noqa: E501


        :return: The owner_id of this CustomerInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CustomerInfo.


        :param owner_id: The owner_id of this CustomerInfo.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

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
        if issubclass(CustomerInfo, dict):
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
        if not isinstance(other, CustomerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
