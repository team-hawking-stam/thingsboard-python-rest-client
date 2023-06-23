# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
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

class AuditLog(object):
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
        'id': 'AuditLogId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'entity_id': 'EntityId',
        'entity_name': 'str',
        'user_id': 'UserId',
        'user_name': 'str',
        'action_type': 'str',
        'action_data': 'JsonNode',
        'action_status': 'str',
        'action_failure_details': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'entity_id': 'entityId',
        'entity_name': 'entityName',
        'user_id': 'userId',
        'user_name': 'userName',
        'action_type': 'actionType',
        'action_data': 'actionData',
        'action_status': 'actionStatus',
        'action_failure_details': 'actionFailureDetails'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, entity_id=None, entity_name=None, user_id=None, user_name=None, action_type=None, action_data=None, action_status=None, action_failure_details=None):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._entity_id = None
        self._entity_name = None
        self._user_id = None
        self._user_name = None
        self._action_type = None
        self._action_data = None
        self._action_status = None
        self._action_failure_details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_name is not None:
            self.entity_name = entity_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if action_type is not None:
            self.action_type = action_type
        if action_data is not None:
            self.action_data = action_data
        if action_status is not None:
            self.action_status = action_status
        if action_failure_details is not None:
            self.action_failure_details = action_failure_details

    @property
    def id(self):
        """Gets the id of this AuditLog.  # noqa: E501


        :return: The id of this AuditLog.  # noqa: E501
        :rtype: AuditLogId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLog.


        :param id: The id of this AuditLog.  # noqa: E501
        :type: AuditLogId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this AuditLog.  # noqa: E501

        Timestamp of the auditLog creation, in milliseconds  # noqa: E501

        :return: The created_time of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AuditLog.

        Timestamp of the auditLog creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this AuditLog.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AuditLog.  # noqa: E501


        :return: The tenant_id of this AuditLog.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AuditLog.


        :param tenant_id: The tenant_id of this AuditLog.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this AuditLog.  # noqa: E501


        :return: The customer_id of this AuditLog.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AuditLog.


        :param customer_id: The customer_id of this AuditLog.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def entity_id(self):
        """Gets the entity_id of this AuditLog.  # noqa: E501


        :return: The entity_id of this AuditLog.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this AuditLog.


        :param entity_id: The entity_id of this AuditLog.  # noqa: E501
        :type: EntityId
        """

        self._entity_id = entity_id

    @property
    def entity_name(self):
        """Gets the entity_name of this AuditLog.  # noqa: E501

        Name of the logged entity  # noqa: E501

        :return: The entity_name of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this AuditLog.

        Name of the logged entity  # noqa: E501

        :param entity_name: The entity_name of this AuditLog.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def user_id(self):
        """Gets the user_id of this AuditLog.  # noqa: E501


        :return: The user_id of this AuditLog.  # noqa: E501
        :rtype: UserId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditLog.


        :param user_id: The user_id of this AuditLog.  # noqa: E501
        :type: UserId
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this AuditLog.  # noqa: E501

        Unique user name(email) of the user that performed some action on logged entity  # noqa: E501

        :return: The user_name of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AuditLog.

        Unique user name(email) of the user that performed some action on logged entity  # noqa: E501

        :param user_name: The user_name of this AuditLog.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def action_type(self):
        """Gets the action_type of this AuditLog.  # noqa: E501

        String represented Action type  # noqa: E501

        :return: The action_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this AuditLog.

        String represented Action type  # noqa: E501

        :param action_type: The action_type of this AuditLog.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVATED", "ADDED", "ADDED_COMMENT", "ALARM_ACK", "ALARM_ASSIGNED", "ALARM_CLEAR", "ALARM_DELETE", "ALARM_UNASSIGNED", "ASSIGNED_FROM_TENANT", "ASSIGNED_TO_CUSTOMER", "ASSIGNED_TO_EDGE", "ASSIGNED_TO_TENANT", "ATTRIBUTES_DELETED", "ATTRIBUTES_READ", "ATTRIBUTES_UPDATED", "CREDENTIALS_READ", "CREDENTIALS_UPDATED", "DELETED", "DELETED_COMMENT", "LOCKOUT", "LOGIN", "LOGOUT", "PROVISION_FAILURE", "PROVISION_SUCCESS", "RELATIONS_DELETED", "RELATION_ADD_OR_UPDATE", "RELATION_DELETED", "RPC_CALL", "SUSPENDED", "TIMESERIES_DELETED", "TIMESERIES_UPDATED", "UNASSIGNED_FROM_CUSTOMER", "UNASSIGNED_FROM_EDGE", "UPDATED", "UPDATED_COMMENT"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def action_data(self):
        """Gets the action_data of this AuditLog.  # noqa: E501


        :return: The action_data of this AuditLog.  # noqa: E501
        :rtype: JsonNode
        """
        return self._action_data

    @action_data.setter
    def action_data(self, action_data):
        """Sets the action_data of this AuditLog.


        :param action_data: The action_data of this AuditLog.  # noqa: E501
        :type: JsonNode
        """

        self._action_data = action_data

    @property
    def action_status(self):
        """Gets the action_status of this AuditLog.  # noqa: E501

        String represented Action status  # noqa: E501

        :return: The action_status of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this AuditLog.

        String represented Action status  # noqa: E501

        :param action_status: The action_status of this AuditLog.  # noqa: E501
        :type: str
        """
        allowed_values = ["FAILURE", "SUCCESS"]  # noqa: E501
        if action_status not in allowed_values:
            raise ValueError(
                "Invalid value for `action_status` ({0}), must be one of {1}"  # noqa: E501
                .format(action_status, allowed_values)
            )

        self._action_status = action_status

    @property
    def action_failure_details(self):
        """Gets the action_failure_details of this AuditLog.  # noqa: E501

        Failure action details info. An empty string in case of action status type 'SUCCESS', otherwise includes stack trace of the caused exception.  # noqa: E501

        :return: The action_failure_details of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action_failure_details

    @action_failure_details.setter
    def action_failure_details(self, action_failure_details):
        """Sets the action_failure_details of this AuditLog.

        Failure action details info. An empty string in case of action status type 'SUCCESS', otherwise includes stack trace of the caused exception.  # noqa: E501

        :param action_failure_details: The action_failure_details of this AuditLog.  # noqa: E501
        :type: str
        """

        self._action_failure_details = action_failure_details

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
        if issubclass(AuditLog, dict):
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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
