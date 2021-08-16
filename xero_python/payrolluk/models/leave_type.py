# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class LeaveType(BaseModel):
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
        'leave_id': 'str',
        'leave_type_id': 'str',
        'name': 'str',
        'is_paid_leave': 'bool',
        'show_on_payslip': 'bool',
        'updated_date_utc': 'datetime',
        'is_active': 'bool',
        'is_statutory_leave': 'bool'
    }

    attribute_map = {
        'leave_id': 'leaveID',
        'leave_type_id': 'leaveTypeID',
        'name': 'name',
        'is_paid_leave': 'isPaidLeave',
        'show_on_payslip': 'showOnPayslip',
        'updated_date_utc': 'updatedDateUTC',
        'is_active': 'isActive',
        'is_statutory_leave': 'isStatutoryLeave'
    }

    def __init__(self, leave_id=None, leave_type_id=None, name=None, is_paid_leave=None, show_on_payslip=None, updated_date_utc=None, is_active=None, is_statutory_leave=None):  # noqa: E501
        """LeaveType - a model defined in OpenAPI"""  # noqa: E501

        self._leave_id = None
        self._leave_type_id = None
        self._name = None
        self._is_paid_leave = None
        self._show_on_payslip = None
        self._updated_date_utc = None
        self._is_active = None
        self._is_statutory_leave = None
        self.discriminator = None

        if leave_id is not None:
            self.leave_id = leave_id
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        self.name = name
        self.is_paid_leave = is_paid_leave
        self.show_on_payslip = show_on_payslip
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_active is not None:
            self.is_active = is_active
        if is_statutory_leave is not None:
            self.is_statutory_leave = is_statutory_leave

    @property
    def leave_id(self):
        """Gets the leave_id of this LeaveType.  # noqa: E501

        Xero unique identifier for the leave  # noqa: E501

        :return: The leave_id of this LeaveType.  # noqa: E501
        :rtype: str
        """
        return self._leave_id

    @leave_id.setter
    def leave_id(self, leave_id):
        """Sets the leave_id of this LeaveType.

        Xero unique identifier for the leave  # noqa: E501

        :param leave_id: The leave_id of this LeaveType.  # noqa: E501
        :type: str
        """

        self._leave_id = leave_id

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this LeaveType.  # noqa: E501

        Xero unique identifier for the leave type  # noqa: E501

        :return: The leave_type_id of this LeaveType.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this LeaveType.

        Xero unique identifier for the leave type  # noqa: E501

        :param leave_type_id: The leave_type_id of this LeaveType.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def name(self):
        """Gets the name of this LeaveType.  # noqa: E501

        Name of the leave type  # noqa: E501

        :return: The name of this LeaveType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LeaveType.

        Name of the leave type  # noqa: E501

        :param name: The name of this LeaveType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_paid_leave(self):
        """Gets the is_paid_leave of this LeaveType.  # noqa: E501

        Indicate that an employee will be paid when taking this type of leave  # noqa: E501

        :return: The is_paid_leave of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._is_paid_leave

    @is_paid_leave.setter
    def is_paid_leave(self, is_paid_leave):
        """Sets the is_paid_leave of this LeaveType.

        Indicate that an employee will be paid when taking this type of leave  # noqa: E501

        :param is_paid_leave: The is_paid_leave of this LeaveType.  # noqa: E501
        :type: bool
        """
        if is_paid_leave is None:
            raise ValueError("Invalid value for `is_paid_leave`, must not be `None`")  # noqa: E501

        self._is_paid_leave = is_paid_leave

    @property
    def show_on_payslip(self):
        """Gets the show_on_payslip of this LeaveType.  # noqa: E501

        Indicate that a balance for this leave type to be shown on the employee’s payslips  # noqa: E501

        :return: The show_on_payslip of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._show_on_payslip

    @show_on_payslip.setter
    def show_on_payslip(self, show_on_payslip):
        """Sets the show_on_payslip of this LeaveType.

        Indicate that a balance for this leave type to be shown on the employee’s payslips  # noqa: E501

        :param show_on_payslip: The show_on_payslip of this LeaveType.  # noqa: E501
        :type: bool
        """
        if show_on_payslip is None:
            raise ValueError("Invalid value for `show_on_payslip`, must not be `None`")  # noqa: E501

        self._show_on_payslip = show_on_payslip

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this LeaveType.  # noqa: E501

        UTC timestamp of last update to the leave type note  # noqa: E501

        :return: The updated_date_utc of this LeaveType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this LeaveType.

        UTC timestamp of last update to the leave type note  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this LeaveType.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def is_active(self):
        """Gets the is_active of this LeaveType.  # noqa: E501

        Shows whether the leave type is active or not  # noqa: E501

        :return: The is_active of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this LeaveType.

        Shows whether the leave type is active or not  # noqa: E501

        :param is_active: The is_active of this LeaveType.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_statutory_leave(self):
        """Gets the is_statutory_leave of this LeaveType.  # noqa: E501

        Shows whether the leave type is a statutory leave type or not  # noqa: E501

        :return: The is_statutory_leave of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._is_statutory_leave

    @is_statutory_leave.setter
    def is_statutory_leave(self, is_statutory_leave):
        """Sets the is_statutory_leave of this LeaveType.

        Shows whether the leave type is a statutory leave type or not  # noqa: E501

        :param is_statutory_leave: The is_statutory_leave of this LeaveType.  # noqa: E501
        :type: bool
        """

        self._is_statutory_leave = is_statutory_leave

