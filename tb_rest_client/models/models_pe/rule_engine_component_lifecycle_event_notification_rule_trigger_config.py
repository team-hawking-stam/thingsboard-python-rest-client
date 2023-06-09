# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_ce.notification_rule_trigger_config import NotificationRuleTriggerConfig  # noqa: F401,E501

class RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig(NotificationRuleTriggerConfig):
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
        'only_rule_chain_lifecycle_failures': 'bool',
        'only_rule_node_lifecycle_failures': 'bool',
        'rule_chain_events': 'list[str]',
        'rule_chains': 'list[str]',
        'rule_node_events': 'list[str]',
        'track_rule_node_events': 'bool',
        'trigger_type': 'str'
    }
    if hasattr(NotificationRuleTriggerConfig, "swagger_types"):
        swagger_types.update(NotificationRuleTriggerConfig.swagger_types)

    attribute_map = {
        'only_rule_chain_lifecycle_failures': 'onlyRuleChainLifecycleFailures',
        'only_rule_node_lifecycle_failures': 'onlyRuleNodeLifecycleFailures',
        'rule_chain_events': 'ruleChainEvents',
        'rule_chains': 'ruleChains',
        'rule_node_events': 'ruleNodeEvents',
        'track_rule_node_events': 'trackRuleNodeEvents',
        'trigger_type': 'triggerType'
    }
    if hasattr(NotificationRuleTriggerConfig, "attribute_map"):
        attribute_map.update(NotificationRuleTriggerConfig.attribute_map)

    def __init__(self, only_rule_chain_lifecycle_failures=None, only_rule_node_lifecycle_failures=None, rule_chain_events=None, rule_chains=None, rule_node_events=None, track_rule_node_events=None, trigger_type=None, *args, **kwargs):  # noqa: E501
        """RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._only_rule_chain_lifecycle_failures = None
        self._only_rule_node_lifecycle_failures = None
        self._rule_chain_events = None
        self._rule_chains = None
        self._rule_node_events = None
        self._track_rule_node_events = None
        self._trigger_type = None
        self.discriminator = None
        if only_rule_chain_lifecycle_failures is not None:
            self.only_rule_chain_lifecycle_failures = only_rule_chain_lifecycle_failures
        if only_rule_node_lifecycle_failures is not None:
            self.only_rule_node_lifecycle_failures = only_rule_node_lifecycle_failures
        if rule_chain_events is not None:
            self.rule_chain_events = rule_chain_events
        if rule_chains is not None:
            self.rule_chains = rule_chains
        if rule_node_events is not None:
            self.rule_node_events = rule_node_events
        if track_rule_node_events is not None:
            self.track_rule_node_events = track_rule_node_events
        if trigger_type is not None:
            self.trigger_type = trigger_type
        NotificationRuleTriggerConfig.__init__(self, *args, **kwargs)

    @property
    def only_rule_chain_lifecycle_failures(self):
        """Gets the only_rule_chain_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The only_rule_chain_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._only_rule_chain_lifecycle_failures

    @only_rule_chain_lifecycle_failures.setter
    def only_rule_chain_lifecycle_failures(self, only_rule_chain_lifecycle_failures):
        """Sets the only_rule_chain_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param only_rule_chain_lifecycle_failures: The only_rule_chain_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._only_rule_chain_lifecycle_failures = only_rule_chain_lifecycle_failures

    @property
    def only_rule_node_lifecycle_failures(self):
        """Gets the only_rule_node_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The only_rule_node_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._only_rule_node_lifecycle_failures

    @only_rule_node_lifecycle_failures.setter
    def only_rule_node_lifecycle_failures(self, only_rule_node_lifecycle_failures):
        """Sets the only_rule_node_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param only_rule_node_lifecycle_failures: The only_rule_node_lifecycle_failures of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._only_rule_node_lifecycle_failures = only_rule_node_lifecycle_failures

    @property
    def rule_chain_events(self):
        """Gets the rule_chain_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The rule_chain_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_chain_events

    @rule_chain_events.setter
    def rule_chain_events(self, rule_chain_events):
        """Sets the rule_chain_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param rule_chain_events: The rule_chain_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACTIVATED", "CREATED", "DELETED", "FAILED", "STARTED", "STOPPED", "SUSPENDED", "UPDATED"]  # noqa: E501
        if not set(rule_chain_events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `rule_chain_events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(rule_chain_events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._rule_chain_events = rule_chain_events

    @property
    def rule_chains(self):
        """Gets the rule_chains of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The rule_chains of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_chains

    @rule_chains.setter
    def rule_chains(self, rule_chains):
        """Sets the rule_chains of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param rule_chains: The rule_chains of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """

        self._rule_chains = rule_chains

    @property
    def rule_node_events(self):
        """Gets the rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_node_events

    @rule_node_events.setter
    def rule_node_events(self, rule_node_events):
        """Sets the rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param rule_node_events: The rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACTIVATED", "CREATED", "DELETED", "FAILED", "STARTED", "STOPPED", "SUSPENDED", "UPDATED"]  # noqa: E501
        if not set(rule_node_events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `rule_node_events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(rule_node_events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._rule_node_events = rule_node_events

    @property
    def track_rule_node_events(self):
        """Gets the track_rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The track_rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._track_rule_node_events

    @track_rule_node_events.setter
    def track_rule_node_events(self, track_rule_node_events):
        """Sets the track_rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param track_rule_node_events: The track_rule_node_events of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._track_rule_node_events = track_rule_node_events

    @property
    def trigger_type(self):
        """Gets the trigger_type of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The trigger_type of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.


        :param trigger_type: The trigger_type of this RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "ENTITIES_LIMIT", "ENTITY_ACTION", "INTEGRATION_LIFECYCLE_EVENT", "NEW_PLATFORM_VERSION", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

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
        if issubclass(RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other