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

class ObjectAttributes(object):
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
        'dim': 'int',
        'ssid': 'int',
        'uri': 'str',
        'ver': 'object',
        'lwm2m': 'LwM2mVersion',
        'pmin': 'int',
        'pmax': 'int',
        'gt': 'float',
        'lt': 'float',
        'st': 'float',
        'epmin': 'int',
        'epmax': 'int'
    }

    attribute_map = {
        'dim': 'dim',
        'ssid': 'ssid',
        'uri': 'uri',
        'ver': 'ver',
        'lwm2m': 'lwm2m',
        'pmin': 'pmin',
        'pmax': 'pmax',
        'gt': 'gt',
        'lt': 'lt',
        'st': 'st',
        'epmin': 'epmin',
        'epmax': 'epmax'
    }

    def __init__(self, dim=None, ssid=None, uri=None, ver=None, lwm2m=None, pmin=None, pmax=None, gt=None, lt=None, st=None, epmin=None, epmax=None):  # noqa: E501
        """ObjectAttributes - a model defined in Swagger"""  # noqa: E501
        self._dim = None
        self._ssid = None
        self._uri = None
        self._ver = None
        self._lwm2m = None
        self._pmin = None
        self._pmax = None
        self._gt = None
        self._lt = None
        self._st = None
        self._epmin = None
        self._epmax = None
        self.discriminator = None
        if dim is not None:
            self.dim = dim
        if ssid is not None:
            self.ssid = ssid
        if uri is not None:
            self.uri = uri
        if ver is not None:
            self.ver = ver
        if lwm2m is not None:
            self.lwm2m = lwm2m
        if pmin is not None:
            self.pmin = pmin
        if pmax is not None:
            self.pmax = pmax
        if gt is not None:
            self.gt = gt
        if lt is not None:
            self.lt = lt
        if st is not None:
            self.st = st
        if epmin is not None:
            self.epmin = epmin
        if epmax is not None:
            self.epmax = epmax

    @property
    def dim(self):
        """Gets the dim of this ObjectAttributes.  # noqa: E501


        :return: The dim of this ObjectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        """Sets the dim of this ObjectAttributes.


        :param dim: The dim of this ObjectAttributes.  # noqa: E501
        :type: int
        """

        self._dim = dim

    @property
    def ssid(self):
        """Gets the ssid of this ObjectAttributes.  # noqa: E501


        :return: The ssid of this ObjectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this ObjectAttributes.


        :param ssid: The ssid of this ObjectAttributes.  # noqa: E501
        :type: int
        """

        self._ssid = ssid

    @property
    def uri(self):
        """Gets the uri of this ObjectAttributes.  # noqa: E501


        :return: The uri of this ObjectAttributes.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ObjectAttributes.


        :param uri: The uri of this ObjectAttributes.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def ver(self):
        """Gets the ver of this ObjectAttributes.  # noqa: E501


        :return: The ver of this ObjectAttributes.  # noqa: E501
        :rtype: object
        """
        return self._ver

    @ver.setter
    def ver(self, ver):
        """Sets the ver of this ObjectAttributes.


        :param ver: The ver of this ObjectAttributes.  # noqa: E501
        :type: object
        """

        self._ver = ver

    @property
    def lwm2m(self):
        """Gets the lwm2m of this ObjectAttributes.  # noqa: E501


        :return: The lwm2m of this ObjectAttributes.  # noqa: E501
        :rtype: LwM2mVersion
        """
        return self._lwm2m

    @lwm2m.setter
    def lwm2m(self, lwm2m):
        """Sets the lwm2m of this ObjectAttributes.


        :param lwm2m: The lwm2m of this ObjectAttributes.  # noqa: E501
        :type: LwM2mVersion
        """

        self._lwm2m = lwm2m

    @property
    def pmin(self):
        """Gets the pmin of this ObjectAttributes.  # noqa: E501


        :return: The pmin of this ObjectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._pmin

    @pmin.setter
    def pmin(self, pmin):
        """Sets the pmin of this ObjectAttributes.


        :param pmin: The pmin of this ObjectAttributes.  # noqa: E501
        :type: int
        """

        self._pmin = pmin

    @property
    def pmax(self):
        """Gets the pmax of this ObjectAttributes.  # noqa: E501


        :return: The pmax of this ObjectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._pmax

    @pmax.setter
    def pmax(self, pmax):
        """Sets the pmax of this ObjectAttributes.


        :param pmax: The pmax of this ObjectAttributes.  # noqa: E501
        :type: int
        """

        self._pmax = pmax

    @property
    def gt(self):
        """Gets the gt of this ObjectAttributes.  # noqa: E501


        :return: The gt of this ObjectAttributes.  # noqa: E501
        :rtype: float
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this ObjectAttributes.


        :param gt: The gt of this ObjectAttributes.  # noqa: E501
        :type: float
        """

        self._gt = gt

    @property
    def lt(self):
        """Gets the lt of this ObjectAttributes.  # noqa: E501


        :return: The lt of this ObjectAttributes.  # noqa: E501
        :rtype: float
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this ObjectAttributes.


        :param lt: The lt of this ObjectAttributes.  # noqa: E501
        :type: float
        """

        self._lt = lt

    @property
    def st(self):
        """Gets the st of this ObjectAttributes.  # noqa: E501


        :return: The st of this ObjectAttributes.  # noqa: E501
        :rtype: float
        """
        return self._st

    @st.setter
    def st(self, st):
        """Sets the st of this ObjectAttributes.


        :param st: The st of this ObjectAttributes.  # noqa: E501
        :type: float
        """

        self._st = st

    @property
    def epmin(self):
        """Gets the epmin of this ObjectAttributes.  # noqa: E501


        :return: The epmin of this ObjectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._epmin

    @epmin.setter
    def epmin(self, epmin):
        """Sets the epmin of this ObjectAttributes.


        :param epmin: The epmin of this ObjectAttributes.  # noqa: E501
        :type: int
        """

        self._epmin = epmin

    @property
    def epmax(self):
        """Gets the epmax of this ObjectAttributes.  # noqa: E501


        :return: The epmax of this ObjectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._epmax

    @epmax.setter
    def epmax(self, epmax):
        """Sets the epmax of this ObjectAttributes.


        :param epmax: The epmax of this ObjectAttributes.  # noqa: E501
        :type: int
        """

        self._epmax = epmax

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
        if issubclass(ObjectAttributes, dict):
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
        if not isinstance(other, ObjectAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
