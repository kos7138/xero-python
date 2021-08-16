# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class LineItem(BaseModel):
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
        'line_item_id': 'str',
        'description': 'str',
        'quantity': 'float',
        'unit_amount': 'float',
        'item_code': 'str',
        'account_code': 'str',
        'account_id': 'str',
        'tax_type': 'str',
        'tax_amount': 'float',
        'line_amount': 'float',
        'tracking': 'list[LineItemTracking]',
        'discount_rate': 'float',
        'discount_amount': 'float',
        'repeating_invoice_id': 'str'
    }

    attribute_map = {
        'line_item_id': 'LineItemID',
        'description': 'Description',
        'quantity': 'Quantity',
        'unit_amount': 'UnitAmount',
        'item_code': 'ItemCode',
        'account_code': 'AccountCode',
        'account_id': 'AccountID',
        'tax_type': 'TaxType',
        'tax_amount': 'TaxAmount',
        'line_amount': 'LineAmount',
        'tracking': 'Tracking',
        'discount_rate': 'DiscountRate',
        'discount_amount': 'DiscountAmount',
        'repeating_invoice_id': 'RepeatingInvoiceID'
    }

    def __init__(self, line_item_id=None, description=None, quantity=None, unit_amount=None, item_code=None, account_code=None, account_id=None, tax_type=None, tax_amount=None, line_amount=None, tracking=None, discount_rate=None, discount_amount=None, repeating_invoice_id=None):  # noqa: E501
        """LineItem - a model defined in OpenAPI"""  # noqa: E501

        self._line_item_id = None
        self._description = None
        self._quantity = None
        self._unit_amount = None
        self._item_code = None
        self._account_code = None
        self._account_id = None
        self._tax_type = None
        self._tax_amount = None
        self._line_amount = None
        self._tracking = None
        self._discount_rate = None
        self._discount_amount = None
        self._repeating_invoice_id = None
        self.discriminator = None

        if line_item_id is not None:
            self.line_item_id = line_item_id
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if unit_amount is not None:
            self.unit_amount = unit_amount
        if item_code is not None:
            self.item_code = item_code
        if account_code is not None:
            self.account_code = account_code
        if account_id is not None:
            self.account_id = account_id
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if line_amount is not None:
            self.line_amount = line_amount
        if tracking is not None:
            self.tracking = tracking
        if discount_rate is not None:
            self.discount_rate = discount_rate
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if repeating_invoice_id is not None:
            self.repeating_invoice_id = repeating_invoice_id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this LineItem.  # noqa: E501

        LineItem unique ID  # noqa: E501

        :return: The line_item_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this LineItem.

        LineItem unique ID  # noqa: E501

        :param line_item_id: The line_item_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

    @property
    def description(self):
        """Gets the description of this LineItem.  # noqa: E501

        Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a <Description> element that contains at least 1 character  # noqa: E501

        :return: The description of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LineItem.

        Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a <Description> element that contains at least 1 character  # noqa: E501

        :param description: The description of this LineItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this LineItem.  # noqa: E501

        LineItem Quantity  # noqa: E501

        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.

        LineItem Quantity  # noqa: E501

        :param quantity: The quantity of this LineItem.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def unit_amount(self):
        """Gets the unit_amount of this LineItem.  # noqa: E501

        LineItem Unit Amount  # noqa: E501

        :return: The unit_amount of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this LineItem.

        LineItem Unit Amount  # noqa: E501

        :param unit_amount: The unit_amount of this LineItem.  # noqa: E501
        :type: float
        """

        self._unit_amount = unit_amount

    @property
    def item_code(self):
        """Gets the item_code of this LineItem.  # noqa: E501

        See Items  # noqa: E501

        :return: The item_code of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        """Sets the item_code of this LineItem.

        See Items  # noqa: E501

        :param item_code: The item_code of this LineItem.  # noqa: E501
        :type: str
        """

        self._item_code = item_code

    @property
    def account_code(self):
        """Gets the account_code of this LineItem.  # noqa: E501

        See Accounts  # noqa: E501

        :return: The account_code of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this LineItem.

        See Accounts  # noqa: E501

        :param account_code: The account_code of this LineItem.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def account_id(self):
        """Gets the account_id of this LineItem.  # noqa: E501

        The associated account ID related to this line item  # noqa: E501

        :return: The account_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this LineItem.

        The associated account ID related to this line item  # noqa: E501

        :param account_id: The account_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def tax_type(self):
        """Gets the tax_type of this LineItem.  # noqa: E501

        The tax type from TaxRates  # noqa: E501

        :return: The tax_type of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this LineItem.

        The tax type from TaxRates  # noqa: E501

        :param tax_type: The tax_type of this LineItem.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

    @property
    def tax_amount(self):
        """Gets the tax_amount of this LineItem.  # noqa: E501

        The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated <TaxAmount> is not correct.  # noqa: E501

        :return: The tax_amount of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this LineItem.

        The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated <TaxAmount> is not correct.  # noqa: E501

        :param tax_amount: The tax_amount of this LineItem.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def line_amount(self):
        """Gets the line_amount of this LineItem.  # noqa: E501

        If you wish to omit either of the <Quantity> or <UnitAmount> you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if a DiscountRate has been used . i.e LineAmount = Quantity * Unit Amount * ((100 – DiscountRate)/100)  # noqa: E501

        :return: The line_amount of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._line_amount

    @line_amount.setter
    def line_amount(self, line_amount):
        """Sets the line_amount of this LineItem.

        If you wish to omit either of the <Quantity> or <UnitAmount> you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if a DiscountRate has been used . i.e LineAmount = Quantity * Unit Amount * ((100 – DiscountRate)/100)  # noqa: E501

        :param line_amount: The line_amount of this LineItem.  # noqa: E501
        :type: float
        """

        self._line_amount = line_amount

    @property
    def tracking(self):
        """Gets the tracking of this LineItem.  # noqa: E501

        Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 <TrackingCategory> elements.  # noqa: E501

        :return: The tracking of this LineItem.  # noqa: E501
        :rtype: list[LineItemTracking]
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this LineItem.

        Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 <TrackingCategory> elements.  # noqa: E501

        :param tracking: The tracking of this LineItem.  # noqa: E501
        :type: list[LineItemTracking]
        """

        self._tracking = tracking

    @property
    def discount_rate(self):
        """Gets the discount_rate of this LineItem.  # noqa: E501

        Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts  # noqa: E501

        :return: The discount_rate of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        """Sets the discount_rate of this LineItem.

        Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts  # noqa: E501

        :param discount_rate: The discount_rate of this LineItem.  # noqa: E501
        :type: float
        """

        self._discount_rate = discount_rate

    @property
    def discount_amount(self):
        """Gets the discount_amount of this LineItem.  # noqa: E501

        Discount amount being applied to a line item. Only supported on ACCREC invoices - ACCPAY invoices and credit notes in Xero do not support discounts.  # noqa: E501

        :return: The discount_amount of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this LineItem.

        Discount amount being applied to a line item. Only supported on ACCREC invoices - ACCPAY invoices and credit notes in Xero do not support discounts.  # noqa: E501

        :param discount_amount: The discount_amount of this LineItem.  # noqa: E501
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def repeating_invoice_id(self):
        """Gets the repeating_invoice_id of this LineItem.  # noqa: E501

        The Xero identifier for a Repeating Invoice  # noqa: E501

        :return: The repeating_invoice_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._repeating_invoice_id

    @repeating_invoice_id.setter
    def repeating_invoice_id(self, repeating_invoice_id):
        """Sets the repeating_invoice_id of this LineItem.

        The Xero identifier for a Repeating Invoice  # noqa: E501

        :param repeating_invoice_id: The repeating_invoice_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._repeating_invoice_id = repeating_invoice_id

