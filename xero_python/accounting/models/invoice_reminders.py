# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class InvoiceReminders(BaseModel):
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
    openapi_types = {"invoice_reminders": "list[InvoiceReminder]"}

    attribute_map = {"invoice_reminders": "InvoiceReminders"}

    def __init__(self, invoice_reminders=None):  # noqa: E501
        """InvoiceReminders - a model defined in OpenAPI"""  # noqa: E501

        self._invoice_reminders = None
        self.discriminator = None

        if invoice_reminders is not None:
            self.invoice_reminders = invoice_reminders

    @property
    def invoice_reminders(self):
        """Gets the invoice_reminders of this InvoiceReminders.  # noqa: E501


        :return: The invoice_reminders of this InvoiceReminders.  # noqa: E501
        :rtype: list[InvoiceReminder]
        """
        return self._invoice_reminders

    @invoice_reminders.setter
    def invoice_reminders(self, invoice_reminders):
        """Sets the invoice_reminders of this InvoiceReminders.


        :param invoice_reminders: The invoice_reminders of this InvoiceReminders.  # noqa: E501
        :type: list[InvoiceReminder]
        """

        self._invoice_reminders = invoice_reminders
