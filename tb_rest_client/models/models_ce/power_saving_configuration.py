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

class PowerSavingConfiguration(object):
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
        'power_mode': 'str',
        'psm_activity_timer': 'int',
        'edrx_cycle': 'int',
        'paging_transmission_window': 'int'
    }

    attribute_map = {
        'power_mode': 'powerMode',
        'psm_activity_timer': 'psmActivityTimer',
        'edrx_cycle': 'edrxCycle',
        'paging_transmission_window': 'pagingTransmissionWindow'
    }

    def __init__(self, power_mode=None, psm_activity_timer=None, edrx_cycle=None, paging_transmission_window=None):  # noqa: E501
        """PowerSavingConfiguration - a model defined in Swagger"""  # noqa: E501
        self._power_mode = None
        self._psm_activity_timer = None
        self._edrx_cycle = None
        self._paging_transmission_window = None
        self.discriminator = None
        if power_mode is not None:
            self.power_mode = power_mode
        if psm_activity_timer is not None:
            self.psm_activity_timer = psm_activity_timer
        if edrx_cycle is not None:
            self.edrx_cycle = edrx_cycle
        if paging_transmission_window is not None:
            self.paging_transmission_window = paging_transmission_window

    @property
    def power_mode(self):
        """Gets the power_mode of this PowerSavingConfiguration.  # noqa: E501


        :return: The power_mode of this PowerSavingConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._power_mode

    @power_mode.setter
    def power_mode(self, power_mode):
        """Sets the power_mode of this PowerSavingConfiguration.


        :param power_mode: The power_mode of this PowerSavingConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["PSM", "DRX", "E_DRX"]  # noqa: E501
        if power_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `power_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(power_mode, allowed_values)
            )

        self._power_mode = power_mode

    @property
    def psm_activity_timer(self):
        """Gets the psm_activity_timer of this PowerSavingConfiguration.  # noqa: E501


        :return: The psm_activity_timer of this PowerSavingConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._psm_activity_timer

    @psm_activity_timer.setter
    def psm_activity_timer(self, psm_activity_timer):
        """Sets the psm_activity_timer of this PowerSavingConfiguration.


        :param psm_activity_timer: The psm_activity_timer of this PowerSavingConfiguration.  # noqa: E501
        :type: int
        """

        self._psm_activity_timer = psm_activity_timer

    @property
    def edrx_cycle(self):
        """Gets the edrx_cycle of this PowerSavingConfiguration.  # noqa: E501


        :return: The edrx_cycle of this PowerSavingConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._edrx_cycle

    @edrx_cycle.setter
    def edrx_cycle(self, edrx_cycle):
        """Sets the edrx_cycle of this PowerSavingConfiguration.


        :param edrx_cycle: The edrx_cycle of this PowerSavingConfiguration.  # noqa: E501
        :type: int
        """

        self._edrx_cycle = edrx_cycle

    @property
    def paging_transmission_window(self):
        """Gets the paging_transmission_window of this PowerSavingConfiguration.  # noqa: E501


        :return: The paging_transmission_window of this PowerSavingConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._paging_transmission_window

    @paging_transmission_window.setter
    def paging_transmission_window(self, paging_transmission_window):
        """Sets the paging_transmission_window of this PowerSavingConfiguration.


        :param paging_transmission_window: The paging_transmission_window of this PowerSavingConfiguration.  # noqa: E501
        :type: int
        """

        self._paging_transmission_window = paging_transmission_window

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
        if issubclass(PowerSavingConfiguration, dict):
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
        if not isinstance(other, PowerSavingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
