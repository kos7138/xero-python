# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class EmployeeStatutoryLeaveBalance(BaseModel):
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
        'leave_type': 'str',
        'balance_remaining': 'float',
        'units': 'str'
    }

    attribute_map = {
        'leave_type': 'leaveType',
        'balance_remaining': 'balanceRemaining',
        'units': 'units'
    }

    def __init__(self, leave_type=None, balance_remaining=None, units=None):  # noqa: E501
        """EmployeeStatutoryLeaveBalance - a model defined in OpenAPI"""  # noqa: E501

        self._leave_type = None
        self._balance_remaining = None
        self._units = None
        self.discriminator = None

        if leave_type is not None:
            self.leave_type = leave_type
        if balance_remaining is not None:
            self.balance_remaining = balance_remaining
        if units is not None:
            self.units = units

    @property
    def leave_type(self):
        """Gets the leave_type of this EmployeeStatutoryLeaveBalance.  # noqa: E501

        The type of statutory leave  # noqa: E501

        :return: The leave_type of this EmployeeStatutoryLeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._leave_type

    @leave_type.setter
    def leave_type(self, leave_type):
        """Sets the leave_type of this EmployeeStatutoryLeaveBalance.

        The type of statutory leave  # noqa: E501

        :param leave_type: The leave_type of this EmployeeStatutoryLeaveBalance.  # noqa: E501
        :type: str
        """
        allowed_values = ["Sick", "Adoption", "Maternity", "Paternity", "Sharedparental", "None"]  # noqa: E501
        
        if leave_type:
            if leave_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `leave_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(leave_type, allowed_values)
            )

        self._leave_type = leave_type

    @property
    def balance_remaining(self):
        """Gets the balance_remaining of this EmployeeStatutoryLeaveBalance.  # noqa: E501

        The balance remaining for the corresponding leave type as of specified date.  # noqa: E501

        :return: The balance_remaining of this EmployeeStatutoryLeaveBalance.  # noqa: E501
        :rtype: float
        """
        return self._balance_remaining

    @balance_remaining.setter
    def balance_remaining(self, balance_remaining):
        """Sets the balance_remaining of this EmployeeStatutoryLeaveBalance.

        The balance remaining for the corresponding leave type as of specified date.  # noqa: E501

        :param balance_remaining: The balance_remaining of this EmployeeStatutoryLeaveBalance.  # noqa: E501
        :type: float
        """

        self._balance_remaining = balance_remaining

    @property
    def units(self):
        """Gets the units of this EmployeeStatutoryLeaveBalance.  # noqa: E501

        The units will be \"Hours\"  # noqa: E501

        :return: The units of this EmployeeStatutoryLeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this EmployeeStatutoryLeaveBalance.

        The units will be \"Hours\"  # noqa: E501

        :param units: The units of this EmployeeStatutoryLeaveBalance.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hours", "None"]  # noqa: E501
        
        if units:
            if units not in allowed_values:
                raise ValueError(
                    "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                    .format(units, allowed_values)
            )

        self._units = units

