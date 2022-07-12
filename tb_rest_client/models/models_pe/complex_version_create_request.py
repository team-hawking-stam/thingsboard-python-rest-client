# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from .version_create_request import VersionCreateRequest  # noqa: F401,E501

class ComplexVersionCreateRequest(VersionCreateRequest):
    """

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
        'branch': 'str',
        'entity_types': 'dict(str, EntityTypeVersionCreateConfig)',
        'sync_strategy': 'str',
        'type': 'str',
        'version_name': 'str'
    }
    if hasattr(VersionCreateRequest, "swagger_types"):
        swagger_types.update(VersionCreateRequest.swagger_types)

    attribute_map = {
        'branch': 'branch',
        'entity_types': 'entityTypes',
        'sync_strategy': 'syncStrategy',
        'type': 'type',
        'version_name': 'versionName'
    }
    if hasattr(VersionCreateRequest, "attribute_map"):
        attribute_map.update(VersionCreateRequest.attribute_map)

    def __init__(self, branch=None, entity_types=None, sync_strategy=None, type=None, version_name=None, *args, **kwargs):  # noqa: E501
        """ComplexVersionCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._branch = None
        self._entity_types = None
        self._sync_strategy = None
        self._type = None
        self._version_name = None
        self.discriminator = None
        if branch is not None:
            self.branch = branch
        if entity_types is not None:
            self.entity_types = entity_types
        if sync_strategy is not None:
            self.sync_strategy = sync_strategy
        if type is not None:
            self.type = type
        if version_name is not None:
            self.version_name = version_name
        VersionCreateRequest.__init__(self, *args, **kwargs)

    @property
    def branch(self):
        """Gets the branch of this ComplexVersionCreateRequest.  # noqa: E501


        :return: The branch of this ComplexVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this ComplexVersionCreateRequest.


        :param branch: The branch of this ComplexVersionCreateRequest.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def entity_types(self):
        """Gets the entity_types of this ComplexVersionCreateRequest.  # noqa: E501


        :return: The entity_types of this ComplexVersionCreateRequest.  # noqa: E501
        :rtype: dict(str, EntityTypeVersionCreateConfig)
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this ComplexVersionCreateRequest.


        :param entity_types: The entity_types of this ComplexVersionCreateRequest.  # noqa: E501
        :type: dict(str, EntityTypeVersionCreateConfig)
        """

        self._entity_types = entity_types

    @property
    def sync_strategy(self):
        """Gets the sync_strategy of this ComplexVersionCreateRequest.  # noqa: E501


        :return: The sync_strategy of this ComplexVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._sync_strategy

    @sync_strategy.setter
    def sync_strategy(self, sync_strategy):
        """Sets the sync_strategy of this ComplexVersionCreateRequest.


        :param sync_strategy: The sync_strategy of this ComplexVersionCreateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MERGE", "OVERWRITE"]  # noqa: E501
        if sync_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_strategy, allowed_values)
            )

        self._sync_strategy = sync_strategy

    @property
    def type(self):
        """Gets the type of this ComplexVersionCreateRequest.  # noqa: E501


        :return: The type of this ComplexVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComplexVersionCreateRequest.


        :param type: The type of this ComplexVersionCreateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPLEX", "SINGLE_ENTITY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version_name(self):
        """Gets the version_name of this ComplexVersionCreateRequest.  # noqa: E501


        :return: The version_name of this ComplexVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this ComplexVersionCreateRequest.


        :param version_name: The version_name of this ComplexVersionCreateRequest.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

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
        if issubclass(ComplexVersionCreateRequest, dict):
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
        if not isinstance(other, ComplexVersionCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other