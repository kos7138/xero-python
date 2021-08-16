# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class EmployeeLeaveType(BaseModel):
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
        'leave_type_id': 'str',
        'schedule_of_accrual': 'str',
        'hours_accrued_annually': 'float',
        'maximum_to_accrue': 'float',
        'opening_balance': 'float',
        'rate_accrued_hourly': 'float',
        'percentage_of_gross_earnings': 'float',
        'include_holiday_pay_every_pay': 'bool',
        'show_annual_leave_in_advance': 'bool',
        'annual_leave_total_amount_paid': 'float'
    }

    attribute_map = {
        'leave_type_id': 'leaveTypeID',
        'schedule_of_accrual': 'scheduleOfAccrual',
        'hours_accrued_annually': 'hoursAccruedAnnually',
        'maximum_to_accrue': 'maximumToAccrue',
        'opening_balance': 'openingBalance',
        'rate_accrued_hourly': 'rateAccruedHourly',
        'percentage_of_gross_earnings': 'percentageOfGrossEarnings',
        'include_holiday_pay_every_pay': 'includeHolidayPayEveryPay',
        'show_annual_leave_in_advance': 'showAnnualLeaveInAdvance',
        'annual_leave_total_amount_paid': 'annualLeaveTotalAmountPaid'
    }

    def __init__(self, leave_type_id=None, schedule_of_accrual=None, hours_accrued_annually=None, maximum_to_accrue=None, opening_balance=None, rate_accrued_hourly=None, percentage_of_gross_earnings=None, include_holiday_pay_every_pay=None, show_annual_leave_in_advance=None, annual_leave_total_amount_paid=None):  # noqa: E501
        """EmployeeLeaveType - a model defined in OpenAPI"""  # noqa: E501

        self._leave_type_id = None
        self._schedule_of_accrual = None
        self._hours_accrued_annually = None
        self._maximum_to_accrue = None
        self._opening_balance = None
        self._rate_accrued_hourly = None
        self._percentage_of_gross_earnings = None
        self._include_holiday_pay_every_pay = None
        self._show_annual_leave_in_advance = None
        self._annual_leave_total_amount_paid = None
        self.discriminator = None

        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if schedule_of_accrual is not None:
            self.schedule_of_accrual = schedule_of_accrual
        if hours_accrued_annually is not None:
            self.hours_accrued_annually = hours_accrued_annually
        if maximum_to_accrue is not None:
            self.maximum_to_accrue = maximum_to_accrue
        if opening_balance is not None:
            self.opening_balance = opening_balance
        if rate_accrued_hourly is not None:
            self.rate_accrued_hourly = rate_accrued_hourly
        if percentage_of_gross_earnings is not None:
            self.percentage_of_gross_earnings = percentage_of_gross_earnings
        if include_holiday_pay_every_pay is not None:
            self.include_holiday_pay_every_pay = include_holiday_pay_every_pay
        if show_annual_leave_in_advance is not None:
            self.show_annual_leave_in_advance = show_annual_leave_in_advance
        if annual_leave_total_amount_paid is not None:
            self.annual_leave_total_amount_paid = annual_leave_total_amount_paid

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this EmployeeLeaveType.  # noqa: E501

        The Xero identifier for leave type  # noqa: E501

        :return: The leave_type_id of this EmployeeLeaveType.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this EmployeeLeaveType.

        The Xero identifier for leave type  # noqa: E501

        :param leave_type_id: The leave_type_id of this EmployeeLeaveType.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def schedule_of_accrual(self):
        """Gets the schedule_of_accrual of this EmployeeLeaveType.  # noqa: E501

        The schedule of accrual  # noqa: E501

        :return: The schedule_of_accrual of this EmployeeLeaveType.  # noqa: E501
        :rtype: str
        """
        return self._schedule_of_accrual

    @schedule_of_accrual.setter
    def schedule_of_accrual(self, schedule_of_accrual):
        """Sets the schedule_of_accrual of this EmployeeLeaveType.

        The schedule of accrual  # noqa: E501

        :param schedule_of_accrual: The schedule_of_accrual of this EmployeeLeaveType.  # noqa: E501
        :type: str
        """
        allowed_values = ["AnnuallyAfter6Months", "OnAnniversaryDate", "PercentageOfGrossEarnings", "NoAccruals", "None"]  # noqa: E501
        
        if schedule_of_accrual:
            if schedule_of_accrual not in allowed_values:
                raise ValueError(
                    "Invalid value for `schedule_of_accrual` ({0}), must be one of {1}"  # noqa: E501
                    .format(schedule_of_accrual, allowed_values)
            )

        self._schedule_of_accrual = schedule_of_accrual

    @property
    def hours_accrued_annually(self):
        """Gets the hours_accrued_annually of this EmployeeLeaveType.  # noqa: E501

        The number of hours accrued for the leave annually. This is 0 when the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :return: The hours_accrued_annually of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._hours_accrued_annually

    @hours_accrued_annually.setter
    def hours_accrued_annually(self, hours_accrued_annually):
        """Sets the hours_accrued_annually of this EmployeeLeaveType.

        The number of hours accrued for the leave annually. This is 0 when the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :param hours_accrued_annually: The hours_accrued_annually of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._hours_accrued_annually = hours_accrued_annually

    @property
    def maximum_to_accrue(self):
        """Gets the maximum_to_accrue of this EmployeeLeaveType.  # noqa: E501

        The maximum number of hours that can be accrued for the leave  # noqa: E501

        :return: The maximum_to_accrue of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._maximum_to_accrue

    @maximum_to_accrue.setter
    def maximum_to_accrue(self, maximum_to_accrue):
        """Sets the maximum_to_accrue of this EmployeeLeaveType.

        The maximum number of hours that can be accrued for the leave  # noqa: E501

        :param maximum_to_accrue: The maximum_to_accrue of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._maximum_to_accrue = maximum_to_accrue

    @property
    def opening_balance(self):
        """Gets the opening_balance of this EmployeeLeaveType.  # noqa: E501

        The initial number of hours assigned when the leave was added to the employee  # noqa: E501

        :return: The opening_balance of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        """Sets the opening_balance of this EmployeeLeaveType.

        The initial number of hours assigned when the leave was added to the employee  # noqa: E501

        :param opening_balance: The opening_balance of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._opening_balance = opening_balance

    @property
    def rate_accrued_hourly(self):
        """Gets the rate_accrued_hourly of this EmployeeLeaveType.  # noqa: E501

        The number of hours added to the leave balance for every hour worked by the employee. This is normally 0, unless the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :return: The rate_accrued_hourly of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._rate_accrued_hourly

    @rate_accrued_hourly.setter
    def rate_accrued_hourly(self, rate_accrued_hourly):
        """Sets the rate_accrued_hourly of this EmployeeLeaveType.

        The number of hours added to the leave balance for every hour worked by the employee. This is normally 0, unless the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :param rate_accrued_hourly: The rate_accrued_hourly of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._rate_accrued_hourly = rate_accrued_hourly

    @property
    def percentage_of_gross_earnings(self):
        """Gets the percentage_of_gross_earnings of this EmployeeLeaveType.  # noqa: E501

        Specific for scheduleOfAccrual having percentage of gross earnings. Identifies how much percentage of gross earnings is accrued per pay period.  # noqa: E501

        :return: The percentage_of_gross_earnings of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_gross_earnings

    @percentage_of_gross_earnings.setter
    def percentage_of_gross_earnings(self, percentage_of_gross_earnings):
        """Sets the percentage_of_gross_earnings of this EmployeeLeaveType.

        Specific for scheduleOfAccrual having percentage of gross earnings. Identifies how much percentage of gross earnings is accrued per pay period.  # noqa: E501

        :param percentage_of_gross_earnings: The percentage_of_gross_earnings of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._percentage_of_gross_earnings = percentage_of_gross_earnings

    @property
    def include_holiday_pay_every_pay(self):
        """Gets the include_holiday_pay_every_pay of this EmployeeLeaveType.  # noqa: E501

        Specific to Holiday pay. Flag determining if pay for leave type is added on each pay run.  # noqa: E501

        :return: The include_holiday_pay_every_pay of this EmployeeLeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._include_holiday_pay_every_pay

    @include_holiday_pay_every_pay.setter
    def include_holiday_pay_every_pay(self, include_holiday_pay_every_pay):
        """Sets the include_holiday_pay_every_pay of this EmployeeLeaveType.

        Specific to Holiday pay. Flag determining if pay for leave type is added on each pay run.  # noqa: E501

        :param include_holiday_pay_every_pay: The include_holiday_pay_every_pay of this EmployeeLeaveType.  # noqa: E501
        :type: bool
        """

        self._include_holiday_pay_every_pay = include_holiday_pay_every_pay

    @property
    def show_annual_leave_in_advance(self):
        """Gets the show_annual_leave_in_advance of this EmployeeLeaveType.  # noqa: E501

        Specific to Annual Leave. Flag to include leave available to take in advance in the balance in the payslip  # noqa: E501

        :return: The show_annual_leave_in_advance of this EmployeeLeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._show_annual_leave_in_advance

    @show_annual_leave_in_advance.setter
    def show_annual_leave_in_advance(self, show_annual_leave_in_advance):
        """Sets the show_annual_leave_in_advance of this EmployeeLeaveType.

        Specific to Annual Leave. Flag to include leave available to take in advance in the balance in the payslip  # noqa: E501

        :param show_annual_leave_in_advance: The show_annual_leave_in_advance of this EmployeeLeaveType.  # noqa: E501
        :type: bool
        """

        self._show_annual_leave_in_advance = show_annual_leave_in_advance

    @property
    def annual_leave_total_amount_paid(self):
        """Gets the annual_leave_total_amount_paid of this EmployeeLeaveType.  # noqa: E501

        Specific to Annual Leave. Annual leave balance in dollars  # noqa: E501

        :return: The annual_leave_total_amount_paid of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._annual_leave_total_amount_paid

    @annual_leave_total_amount_paid.setter
    def annual_leave_total_amount_paid(self, annual_leave_total_amount_paid):
        """Sets the annual_leave_total_amount_paid of this EmployeeLeaveType.

        Specific to Annual Leave. Annual leave balance in dollars  # noqa: E501

        :param annual_leave_total_amount_paid: The annual_leave_total_amount_paid of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._annual_leave_total_amount_paid = annual_leave_total_amount_paid

