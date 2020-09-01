# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.14
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class InvoiceReminder(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"enabled": "bool"}

    attribute_map = {"enabled": "Enabled"}

    def __init__(self, enabled=None):  # noqa: E501
        """InvoiceReminder - a model defined in OpenAPI"""  # noqa: E501

        self._enabled = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled

    @property
    def enabled(self):
        """Gets the enabled of this InvoiceReminder.  # noqa: E501

        setting for on or off  # noqa: E501

        :return: The enabled of this InvoiceReminder.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InvoiceReminder.

        setting for on or off  # noqa: E501

        :param enabled: The enabled of this InvoiceReminder.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled
