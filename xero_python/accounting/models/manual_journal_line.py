# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class ManualJournalLine(BaseModel):
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
    openapi_types = {
        'line_amount': 'float',
        'account_code': 'str',
        'account_id': 'str',
        'description': 'str',
        'tax_type': 'str',
        'tracking': 'list[TrackingCategory]',
        'tax_amount': 'float',
        'is_blank': 'bool'
    }

    attribute_map = {
        'line_amount': 'LineAmount',
        'account_code': 'AccountCode',
        'account_id': 'AccountID',
        'description': 'Description',
        'tax_type': 'TaxType',
        'tracking': 'Tracking',
        'tax_amount': 'TaxAmount',
        'is_blank': 'IsBlank'
    }

    def __init__(self, line_amount=None, account_code=None, account_id=None, description=None, tax_type=None, tracking=None, tax_amount=None, is_blank=None):  # noqa: E501
        """ManualJournalLine - a model defined in OpenAPI"""  # noqa: E501

        self._line_amount = None
        self._account_code = None
        self._account_id = None
        self._description = None
        self._tax_type = None
        self._tracking = None
        self._tax_amount = None
        self._is_blank = None
        self.discriminator = None

        if line_amount is not None:
            self.line_amount = line_amount
        if account_code is not None:
            self.account_code = account_code
        if account_id is not None:
            self.account_id = account_id
        if description is not None:
            self.description = description
        if tax_type is not None:
            self.tax_type = tax_type
        if tracking is not None:
            self.tracking = tracking
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if is_blank is not None:
            self.is_blank = is_blank

    @property
    def line_amount(self):
        """Gets the line_amount of this ManualJournalLine.  # noqa: E501

        total for line. Debits are positive, credits are negative value  # noqa: E501

        :return: The line_amount of this ManualJournalLine.  # noqa: E501
        :rtype: float
        """
        return self._line_amount

    @line_amount.setter
    def line_amount(self, line_amount):
        """Sets the line_amount of this ManualJournalLine.

        total for line. Debits are positive, credits are negative value  # noqa: E501

        :param line_amount: The line_amount of this ManualJournalLine.  # noqa: E501
        :type: float
        """

        self._line_amount = line_amount

    @property
    def account_code(self):
        """Gets the account_code of this ManualJournalLine.  # noqa: E501

        See Accounts  # noqa: E501

        :return: The account_code of this ManualJournalLine.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this ManualJournalLine.

        See Accounts  # noqa: E501

        :param account_code: The account_code of this ManualJournalLine.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def account_id(self):
        """Gets the account_id of this ManualJournalLine.  # noqa: E501

        See Accounts  # noqa: E501

        :return: The account_id of this ManualJournalLine.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ManualJournalLine.

        See Accounts  # noqa: E501

        :param account_id: The account_id of this ManualJournalLine.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def description(self):
        """Gets the description of this ManualJournalLine.  # noqa: E501

        Description for journal line  # noqa: E501

        :return: The description of this ManualJournalLine.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ManualJournalLine.

        Description for journal line  # noqa: E501

        :param description: The description of this ManualJournalLine.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tax_type(self):
        """Gets the tax_type of this ManualJournalLine.  # noqa: E501

        The tax type from TaxRates  # noqa: E501

        :return: The tax_type of this ManualJournalLine.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this ManualJournalLine.

        The tax type from TaxRates  # noqa: E501

        :param tax_type: The tax_type of this ManualJournalLine.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

    @property
    def tracking(self):
        """Gets the tracking of this ManualJournalLine.  # noqa: E501

        Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 <TrackingCategory> elements.  # noqa: E501

        :return: The tracking of this ManualJournalLine.  # noqa: E501
        :rtype: list[TrackingCategory]
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this ManualJournalLine.

        Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 <TrackingCategory> elements.  # noqa: E501

        :param tracking: The tracking of this ManualJournalLine.  # noqa: E501
        :type: list[TrackingCategory]
        """

        self._tracking = tracking

    @property
    def tax_amount(self):
        """Gets the tax_amount of this ManualJournalLine.  # noqa: E501

        The calculated tax amount based on the TaxType and LineAmount  # noqa: E501

        :return: The tax_amount of this ManualJournalLine.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this ManualJournalLine.

        The calculated tax amount based on the TaxType and LineAmount  # noqa: E501

        :param tax_amount: The tax_amount of this ManualJournalLine.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def is_blank(self):
        """Gets the is_blank of this ManualJournalLine.  # noqa: E501

        is the line blank  # noqa: E501

        :return: The is_blank of this ManualJournalLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_blank

    @is_blank.setter
    def is_blank(self, is_blank):
        """Sets the is_blank of this ManualJournalLine.

        is the line blank  # noqa: E501

        :param is_blank: The is_blank of this ManualJournalLine.  # noqa: E501
        :type: bool
        """

        self._is_blank = is_blank

