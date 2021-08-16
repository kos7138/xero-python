# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class BankAccount(BaseModel):
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
        'account_name': 'str',
        'account_number': 'str',
        'sort_code': 'str',
        'particulars': 'str',
        'code': 'str',
        'dollar_amount': 'float',
        'reference': 'str',
        'calculation_type': 'str'
    }

    attribute_map = {
        'account_name': 'accountName',
        'account_number': 'accountNumber',
        'sort_code': 'sortCode',
        'particulars': 'particulars',
        'code': 'code',
        'dollar_amount': 'dollarAmount',
        'reference': 'reference',
        'calculation_type': 'calculationType'
    }

    def __init__(self, account_name=None, account_number=None, sort_code=None, particulars=None, code=None, dollar_amount=None, reference=None, calculation_type=None):  # noqa: E501
        """BankAccount - a model defined in OpenAPI"""  # noqa: E501

        self._account_name = None
        self._account_number = None
        self._sort_code = None
        self._particulars = None
        self._code = None
        self._dollar_amount = None
        self._reference = None
        self._calculation_type = None
        self.discriminator = None

        self.account_name = account_name
        self.account_number = account_number
        self.sort_code = sort_code
        if particulars is not None:
            self.particulars = particulars
        if code is not None:
            self.code = code
        if dollar_amount is not None:
            self.dollar_amount = dollar_amount
        if reference is not None:
            self.reference = reference
        if calculation_type is not None:
            self.calculation_type = calculation_type

    @property
    def account_name(self):
        """Gets the account_name of this BankAccount.  # noqa: E501

        Bank account name (max length = 32)  # noqa: E501

        :return: The account_name of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this BankAccount.

        Bank account name (max length = 32)  # noqa: E501

        :param account_name: The account_name of this BankAccount.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this BankAccount.  # noqa: E501

        Bank account number (digits only; max length = 8)  # noqa: E501

        :return: The account_number of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BankAccount.

        Bank account number (digits only; max length = 8)  # noqa: E501

        :param account_number: The account_number of this BankAccount.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def sort_code(self):
        """Gets the sort_code of this BankAccount.  # noqa: E501

        Bank account sort code (6 digits)  # noqa: E501

        :return: The sort_code of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this BankAccount.

        Bank account sort code (6 digits)  # noqa: E501

        :param sort_code: The sort_code of this BankAccount.  # noqa: E501
        :type: str
        """
        if sort_code is None:
            raise ValueError("Invalid value for `sort_code`, must not be `None`")  # noqa: E501

        self._sort_code = sort_code

    @property
    def particulars(self):
        """Gets the particulars of this BankAccount.  # noqa: E501

        Particulars that appear on the statement.  # noqa: E501

        :return: The particulars of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._particulars

    @particulars.setter
    def particulars(self, particulars):
        """Sets the particulars of this BankAccount.

        Particulars that appear on the statement.  # noqa: E501

        :param particulars: The particulars of this BankAccount.  # noqa: E501
        :type: str
        """

        self._particulars = particulars

    @property
    def code(self):
        """Gets the code of this BankAccount.  # noqa: E501

        Code of a transaction that appear on the statement.  # noqa: E501

        :return: The code of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BankAccount.

        Code of a transaction that appear on the statement.  # noqa: E501

        :param code: The code of this BankAccount.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def dollar_amount(self):
        """Gets the dollar_amount of this BankAccount.  # noqa: E501

        Dollar amount of a transaction.  # noqa: E501

        :return: The dollar_amount of this BankAccount.  # noqa: E501
        :rtype: float
        """
        return self._dollar_amount

    @dollar_amount.setter
    def dollar_amount(self, dollar_amount):
        """Sets the dollar_amount of this BankAccount.

        Dollar amount of a transaction.  # noqa: E501

        :param dollar_amount: The dollar_amount of this BankAccount.  # noqa: E501
        :type: float
        """

        self._dollar_amount = dollar_amount

    @property
    def reference(self):
        """Gets the reference of this BankAccount.  # noqa: E501

        Statement Text/reference for a transaction that appear on the statement.  # noqa: E501

        :return: The reference of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BankAccount.

        Statement Text/reference for a transaction that appear on the statement.  # noqa: E501

        :param reference: The reference of this BankAccount.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def calculation_type(self):
        """Gets the calculation_type of this BankAccount.  # noqa: E501

        Calculation type for the transaction can be 'Fixed Amount' or 'Balance'  # noqa: E501

        :return: The calculation_type of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this BankAccount.

        Calculation type for the transaction can be 'Fixed Amount' or 'Balance'  # noqa: E501

        :param calculation_type: The calculation_type of this BankAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["FixedAmount", "Balance", "None"]  # noqa: E501
        
        if calculation_type:
            if calculation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(calculation_type, allowed_values)
            )

        self._calculation_type = calculation_type

