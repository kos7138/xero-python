# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class PaySlip(BaseModel):
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
        'pay_slip_id': 'str',
        'employee_id': 'str',
        'pay_run_id': 'str',
        'last_edited': 'date',
        'first_name': 'str',
        'last_name': 'str',
        'total_earnings': 'float',
        'gross_earnings': 'float',
        'total_pay': 'float',
        'total_employer_taxes': 'float',
        'total_employee_taxes': 'float',
        'total_deductions': 'float',
        'total_reimbursements': 'float',
        'total_statutory_deductions': 'float',
        'total_superannuation': 'float',
        'bacs_hash': 'str',
        'payment_method': 'str',
        'earnings_lines': 'list[EarningsLine]',
        'leave_earnings_lines': 'list[LeaveEarningsLine]',
        'timesheet_earnings_lines': 'list[TimesheetEarningsLine]',
        'deduction_lines': 'list[DeductionLine]',
        'reimbursement_lines': 'list[ReimbursementLine]',
        'leave_accrual_lines': 'list[LeaveAccrualLine]',
        'superannuation_lines': 'list[SuperannuationLine]',
        'payment_lines': 'list[PaymentLine]',
        'employee_tax_lines': 'list[TaxLine]',
        'employer_tax_lines': 'list[TaxLine]',
        'statutory_deduction_lines': 'list[StatutoryDeductionLine]',
        'tax_settings': 'TaxSettings',
        'gross_earnings_history': 'GrossEarningsHistory'
    }

    attribute_map = {
        'pay_slip_id': 'paySlipID',
        'employee_id': 'employeeID',
        'pay_run_id': 'payRunID',
        'last_edited': 'lastEdited',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'total_earnings': 'totalEarnings',
        'gross_earnings': 'grossEarnings',
        'total_pay': 'totalPay',
        'total_employer_taxes': 'totalEmployerTaxes',
        'total_employee_taxes': 'totalEmployeeTaxes',
        'total_deductions': 'totalDeductions',
        'total_reimbursements': 'totalReimbursements',
        'total_statutory_deductions': 'totalStatutoryDeductions',
        'total_superannuation': 'totalSuperannuation',
        'bacs_hash': 'bacsHash',
        'payment_method': 'paymentMethod',
        'earnings_lines': 'earningsLines',
        'leave_earnings_lines': 'leaveEarningsLines',
        'timesheet_earnings_lines': 'timesheetEarningsLines',
        'deduction_lines': 'deductionLines',
        'reimbursement_lines': 'reimbursementLines',
        'leave_accrual_lines': 'leaveAccrualLines',
        'superannuation_lines': 'superannuationLines',
        'payment_lines': 'paymentLines',
        'employee_tax_lines': 'employeeTaxLines',
        'employer_tax_lines': 'employerTaxLines',
        'statutory_deduction_lines': 'statutoryDeductionLines',
        'tax_settings': 'taxSettings',
        'gross_earnings_history': 'grossEarningsHistory'
    }

    def __init__(self, pay_slip_id=None, employee_id=None, pay_run_id=None, last_edited=None, first_name=None, last_name=None, total_earnings=None, gross_earnings=None, total_pay=None, total_employer_taxes=None, total_employee_taxes=None, total_deductions=None, total_reimbursements=None, total_statutory_deductions=None, total_superannuation=None, bacs_hash=None, payment_method=None, earnings_lines=None, leave_earnings_lines=None, timesheet_earnings_lines=None, deduction_lines=None, reimbursement_lines=None, leave_accrual_lines=None, superannuation_lines=None, payment_lines=None, employee_tax_lines=None, employer_tax_lines=None, statutory_deduction_lines=None, tax_settings=None, gross_earnings_history=None):  # noqa: E501
        """PaySlip - a model defined in OpenAPI"""  # noqa: E501

        self._pay_slip_id = None
        self._employee_id = None
        self._pay_run_id = None
        self._last_edited = None
        self._first_name = None
        self._last_name = None
        self._total_earnings = None
        self._gross_earnings = None
        self._total_pay = None
        self._total_employer_taxes = None
        self._total_employee_taxes = None
        self._total_deductions = None
        self._total_reimbursements = None
        self._total_statutory_deductions = None
        self._total_superannuation = None
        self._bacs_hash = None
        self._payment_method = None
        self._earnings_lines = None
        self._leave_earnings_lines = None
        self._timesheet_earnings_lines = None
        self._deduction_lines = None
        self._reimbursement_lines = None
        self._leave_accrual_lines = None
        self._superannuation_lines = None
        self._payment_lines = None
        self._employee_tax_lines = None
        self._employer_tax_lines = None
        self._statutory_deduction_lines = None
        self._tax_settings = None
        self._gross_earnings_history = None
        self.discriminator = None

        if pay_slip_id is not None:
            self.pay_slip_id = pay_slip_id
        if employee_id is not None:
            self.employee_id = employee_id
        if pay_run_id is not None:
            self.pay_run_id = pay_run_id
        if last_edited is not None:
            self.last_edited = last_edited
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if total_earnings is not None:
            self.total_earnings = total_earnings
        if gross_earnings is not None:
            self.gross_earnings = gross_earnings
        if total_pay is not None:
            self.total_pay = total_pay
        if total_employer_taxes is not None:
            self.total_employer_taxes = total_employer_taxes
        if total_employee_taxes is not None:
            self.total_employee_taxes = total_employee_taxes
        if total_deductions is not None:
            self.total_deductions = total_deductions
        if total_reimbursements is not None:
            self.total_reimbursements = total_reimbursements
        if total_statutory_deductions is not None:
            self.total_statutory_deductions = total_statutory_deductions
        if total_superannuation is not None:
            self.total_superannuation = total_superannuation
        if bacs_hash is not None:
            self.bacs_hash = bacs_hash
        if payment_method is not None:
            self.payment_method = payment_method
        if earnings_lines is not None:
            self.earnings_lines = earnings_lines
        if leave_earnings_lines is not None:
            self.leave_earnings_lines = leave_earnings_lines
        if timesheet_earnings_lines is not None:
            self.timesheet_earnings_lines = timesheet_earnings_lines
        if deduction_lines is not None:
            self.deduction_lines = deduction_lines
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines
        if leave_accrual_lines is not None:
            self.leave_accrual_lines = leave_accrual_lines
        if superannuation_lines is not None:
            self.superannuation_lines = superannuation_lines
        if payment_lines is not None:
            self.payment_lines = payment_lines
        if employee_tax_lines is not None:
            self.employee_tax_lines = employee_tax_lines
        if employer_tax_lines is not None:
            self.employer_tax_lines = employer_tax_lines
        if statutory_deduction_lines is not None:
            self.statutory_deduction_lines = statutory_deduction_lines
        if tax_settings is not None:
            self.tax_settings = tax_settings
        if gross_earnings_history is not None:
            self.gross_earnings_history = gross_earnings_history

    @property
    def pay_slip_id(self):
        """Gets the pay_slip_id of this PaySlip.  # noqa: E501

        The Xero identifier for a PaySlip  # noqa: E501

        :return: The pay_slip_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._pay_slip_id

    @pay_slip_id.setter
    def pay_slip_id(self, pay_slip_id):
        """Sets the pay_slip_id of this PaySlip.

        The Xero identifier for a PaySlip  # noqa: E501

        :param pay_slip_id: The pay_slip_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._pay_slip_id = pay_slip_id

    @property
    def employee_id(self):
        """Gets the employee_id of this PaySlip.  # noqa: E501

        The Xero identifier for payroll employee  # noqa: E501

        :return: The employee_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this PaySlip.

        The Xero identifier for payroll employee  # noqa: E501

        :param employee_id: The employee_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def pay_run_id(self):
        """Gets the pay_run_id of this PaySlip.  # noqa: E501

        The Xero identifier for the associated payrun  # noqa: E501

        :return: The pay_run_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._pay_run_id

    @pay_run_id.setter
    def pay_run_id(self, pay_run_id):
        """Sets the pay_run_id of this PaySlip.

        The Xero identifier for the associated payrun  # noqa: E501

        :param pay_run_id: The pay_run_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._pay_run_id = pay_run_id

    @property
    def last_edited(self):
        """Gets the last_edited of this PaySlip.  # noqa: E501

        The date payslip was last updated  # noqa: E501

        :return: The last_edited of this PaySlip.  # noqa: E501
        :rtype: date
        """
        return self._last_edited

    @last_edited.setter
    def last_edited(self, last_edited):
        """Sets the last_edited of this PaySlip.

        The date payslip was last updated  # noqa: E501

        :param last_edited: The last_edited of this PaySlip.  # noqa: E501
        :type: date
        """

        self._last_edited = last_edited

    @property
    def first_name(self):
        """Gets the first_name of this PaySlip.  # noqa: E501

        Employee first name  # noqa: E501

        :return: The first_name of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PaySlip.

        Employee first name  # noqa: E501

        :param first_name: The first_name of this PaySlip.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PaySlip.  # noqa: E501

        Employee last name  # noqa: E501

        :return: The last_name of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PaySlip.

        Employee last name  # noqa: E501

        :param last_name: The last_name of this PaySlip.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def total_earnings(self):
        """Gets the total_earnings of this PaySlip.  # noqa: E501

        Total earnings before any deductions. Same as gross earnings for NZ.  # noqa: E501

        :return: The total_earnings of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_earnings

    @total_earnings.setter
    def total_earnings(self, total_earnings):
        """Sets the total_earnings of this PaySlip.

        Total earnings before any deductions. Same as gross earnings for NZ.  # noqa: E501

        :param total_earnings: The total_earnings of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_earnings = total_earnings

    @property
    def gross_earnings(self):
        """Gets the gross_earnings of this PaySlip.  # noqa: E501

        Total earnings before any deductions. Same as total earnings for NZ.  # noqa: E501

        :return: The gross_earnings of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._gross_earnings

    @gross_earnings.setter
    def gross_earnings(self, gross_earnings):
        """Sets the gross_earnings of this PaySlip.

        Total earnings before any deductions. Same as total earnings for NZ.  # noqa: E501

        :param gross_earnings: The gross_earnings of this PaySlip.  # noqa: E501
        :type: float
        """

        self._gross_earnings = gross_earnings

    @property
    def total_pay(self):
        """Gets the total_pay of this PaySlip.  # noqa: E501

        The employee net pay  # noqa: E501

        :return: The total_pay of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_pay

    @total_pay.setter
    def total_pay(self, total_pay):
        """Sets the total_pay of this PaySlip.

        The employee net pay  # noqa: E501

        :param total_pay: The total_pay of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_pay = total_pay

    @property
    def total_employer_taxes(self):
        """Gets the total_employer_taxes of this PaySlip.  # noqa: E501

        The employer's tax obligation  # noqa: E501

        :return: The total_employer_taxes of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_employer_taxes

    @total_employer_taxes.setter
    def total_employer_taxes(self, total_employer_taxes):
        """Sets the total_employer_taxes of this PaySlip.

        The employer's tax obligation  # noqa: E501

        :param total_employer_taxes: The total_employer_taxes of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_employer_taxes = total_employer_taxes

    @property
    def total_employee_taxes(self):
        """Gets the total_employee_taxes of this PaySlip.  # noqa: E501

        The part of an employee's earnings that is deducted for tax purposes  # noqa: E501

        :return: The total_employee_taxes of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_employee_taxes

    @total_employee_taxes.setter
    def total_employee_taxes(self, total_employee_taxes):
        """Sets the total_employee_taxes of this PaySlip.

        The part of an employee's earnings that is deducted for tax purposes  # noqa: E501

        :param total_employee_taxes: The total_employee_taxes of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_employee_taxes = total_employee_taxes

    @property
    def total_deductions(self):
        """Gets the total_deductions of this PaySlip.  # noqa: E501

        Total amount subtracted from an employee's earnings to reach total pay  # noqa: E501

        :return: The total_deductions of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_deductions

    @total_deductions.setter
    def total_deductions(self, total_deductions):
        """Sets the total_deductions of this PaySlip.

        Total amount subtracted from an employee's earnings to reach total pay  # noqa: E501

        :param total_deductions: The total_deductions of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_deductions = total_deductions

    @property
    def total_reimbursements(self):
        """Gets the total_reimbursements of this PaySlip.  # noqa: E501

        Total reimbursements are nontaxable payments to an employee used to repay out-of-pocket expenses when the person incurs those expenses through employment  # noqa: E501

        :return: The total_reimbursements of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_reimbursements

    @total_reimbursements.setter
    def total_reimbursements(self, total_reimbursements):
        """Sets the total_reimbursements of this PaySlip.

        Total reimbursements are nontaxable payments to an employee used to repay out-of-pocket expenses when the person incurs those expenses through employment  # noqa: E501

        :param total_reimbursements: The total_reimbursements of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_reimbursements = total_reimbursements

    @property
    def total_statutory_deductions(self):
        """Gets the total_statutory_deductions of this PaySlip.  # noqa: E501

        Total amounts required by law to subtract from the employee's earnings  # noqa: E501

        :return: The total_statutory_deductions of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_statutory_deductions

    @total_statutory_deductions.setter
    def total_statutory_deductions(self, total_statutory_deductions):
        """Sets the total_statutory_deductions of this PaySlip.

        Total amounts required by law to subtract from the employee's earnings  # noqa: E501

        :param total_statutory_deductions: The total_statutory_deductions of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_statutory_deductions = total_statutory_deductions

    @property
    def total_superannuation(self):
        """Gets the total_superannuation of this PaySlip.  # noqa: E501

        Benefits (also called fringe benefits, perquisites or perks) are various non-earnings compensations provided to employees in addition to their normal earnings or salaries  # noqa: E501

        :return: The total_superannuation of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._total_superannuation

    @total_superannuation.setter
    def total_superannuation(self, total_superannuation):
        """Sets the total_superannuation of this PaySlip.

        Benefits (also called fringe benefits, perquisites or perks) are various non-earnings compensations provided to employees in addition to their normal earnings or salaries  # noqa: E501

        :param total_superannuation: The total_superannuation of this PaySlip.  # noqa: E501
        :type: float
        """

        self._total_superannuation = total_superannuation

    @property
    def bacs_hash(self):
        """Gets the bacs_hash of this PaySlip.  # noqa: E501

        BACS Service User Number  # noqa: E501

        :return: The bacs_hash of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._bacs_hash

    @bacs_hash.setter
    def bacs_hash(self, bacs_hash):
        """Sets the bacs_hash of this PaySlip.

        BACS Service User Number  # noqa: E501

        :param bacs_hash: The bacs_hash of this PaySlip.  # noqa: E501
        :type: str
        """

        self._bacs_hash = bacs_hash

    @property
    def payment_method(self):
        """Gets the payment_method of this PaySlip.  # noqa: E501

        The payment method code  # noqa: E501

        :return: The payment_method of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaySlip.

        The payment method code  # noqa: E501

        :param payment_method: The payment_method of this PaySlip.  # noqa: E501
        :type: str
        """
        allowed_values = ["Cheque", "Electronically", "Manual", "None"]  # noqa: E501
        
        if payment_method:
            if payment_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                    .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def earnings_lines(self):
        """Gets the earnings_lines of this PaySlip.  # noqa: E501


        :return: The earnings_lines of this PaySlip.  # noqa: E501
        :rtype: list[EarningsLine]
        """
        return self._earnings_lines

    @earnings_lines.setter
    def earnings_lines(self, earnings_lines):
        """Sets the earnings_lines of this PaySlip.


        :param earnings_lines: The earnings_lines of this PaySlip.  # noqa: E501
        :type: list[EarningsLine]
        """

        self._earnings_lines = earnings_lines

    @property
    def leave_earnings_lines(self):
        """Gets the leave_earnings_lines of this PaySlip.  # noqa: E501


        :return: The leave_earnings_lines of this PaySlip.  # noqa: E501
        :rtype: list[LeaveEarningsLine]
        """
        return self._leave_earnings_lines

    @leave_earnings_lines.setter
    def leave_earnings_lines(self, leave_earnings_lines):
        """Sets the leave_earnings_lines of this PaySlip.


        :param leave_earnings_lines: The leave_earnings_lines of this PaySlip.  # noqa: E501
        :type: list[LeaveEarningsLine]
        """

        self._leave_earnings_lines = leave_earnings_lines

    @property
    def timesheet_earnings_lines(self):
        """Gets the timesheet_earnings_lines of this PaySlip.  # noqa: E501


        :return: The timesheet_earnings_lines of this PaySlip.  # noqa: E501
        :rtype: list[TimesheetEarningsLine]
        """
        return self._timesheet_earnings_lines

    @timesheet_earnings_lines.setter
    def timesheet_earnings_lines(self, timesheet_earnings_lines):
        """Sets the timesheet_earnings_lines of this PaySlip.


        :param timesheet_earnings_lines: The timesheet_earnings_lines of this PaySlip.  # noqa: E501
        :type: list[TimesheetEarningsLine]
        """

        self._timesheet_earnings_lines = timesheet_earnings_lines

    @property
    def deduction_lines(self):
        """Gets the deduction_lines of this PaySlip.  # noqa: E501


        :return: The deduction_lines of this PaySlip.  # noqa: E501
        :rtype: list[DeductionLine]
        """
        return self._deduction_lines

    @deduction_lines.setter
    def deduction_lines(self, deduction_lines):
        """Sets the deduction_lines of this PaySlip.


        :param deduction_lines: The deduction_lines of this PaySlip.  # noqa: E501
        :type: list[DeductionLine]
        """

        self._deduction_lines = deduction_lines

    @property
    def reimbursement_lines(self):
        """Gets the reimbursement_lines of this PaySlip.  # noqa: E501


        :return: The reimbursement_lines of this PaySlip.  # noqa: E501
        :rtype: list[ReimbursementLine]
        """
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        """Sets the reimbursement_lines of this PaySlip.


        :param reimbursement_lines: The reimbursement_lines of this PaySlip.  # noqa: E501
        :type: list[ReimbursementLine]
        """

        self._reimbursement_lines = reimbursement_lines

    @property
    def leave_accrual_lines(self):
        """Gets the leave_accrual_lines of this PaySlip.  # noqa: E501


        :return: The leave_accrual_lines of this PaySlip.  # noqa: E501
        :rtype: list[LeaveAccrualLine]
        """
        return self._leave_accrual_lines

    @leave_accrual_lines.setter
    def leave_accrual_lines(self, leave_accrual_lines):
        """Sets the leave_accrual_lines of this PaySlip.


        :param leave_accrual_lines: The leave_accrual_lines of this PaySlip.  # noqa: E501
        :type: list[LeaveAccrualLine]
        """

        self._leave_accrual_lines = leave_accrual_lines

    @property
    def superannuation_lines(self):
        """Gets the superannuation_lines of this PaySlip.  # noqa: E501


        :return: The superannuation_lines of this PaySlip.  # noqa: E501
        :rtype: list[SuperannuationLine]
        """
        return self._superannuation_lines

    @superannuation_lines.setter
    def superannuation_lines(self, superannuation_lines):
        """Sets the superannuation_lines of this PaySlip.


        :param superannuation_lines: The superannuation_lines of this PaySlip.  # noqa: E501
        :type: list[SuperannuationLine]
        """

        self._superannuation_lines = superannuation_lines

    @property
    def payment_lines(self):
        """Gets the payment_lines of this PaySlip.  # noqa: E501


        :return: The payment_lines of this PaySlip.  # noqa: E501
        :rtype: list[PaymentLine]
        """
        return self._payment_lines

    @payment_lines.setter
    def payment_lines(self, payment_lines):
        """Sets the payment_lines of this PaySlip.


        :param payment_lines: The payment_lines of this PaySlip.  # noqa: E501
        :type: list[PaymentLine]
        """

        self._payment_lines = payment_lines

    @property
    def employee_tax_lines(self):
        """Gets the employee_tax_lines of this PaySlip.  # noqa: E501


        :return: The employee_tax_lines of this PaySlip.  # noqa: E501
        :rtype: list[TaxLine]
        """
        return self._employee_tax_lines

    @employee_tax_lines.setter
    def employee_tax_lines(self, employee_tax_lines):
        """Sets the employee_tax_lines of this PaySlip.


        :param employee_tax_lines: The employee_tax_lines of this PaySlip.  # noqa: E501
        :type: list[TaxLine]
        """

        self._employee_tax_lines = employee_tax_lines

    @property
    def employer_tax_lines(self):
        """Gets the employer_tax_lines of this PaySlip.  # noqa: E501


        :return: The employer_tax_lines of this PaySlip.  # noqa: E501
        :rtype: list[TaxLine]
        """
        return self._employer_tax_lines

    @employer_tax_lines.setter
    def employer_tax_lines(self, employer_tax_lines):
        """Sets the employer_tax_lines of this PaySlip.


        :param employer_tax_lines: The employer_tax_lines of this PaySlip.  # noqa: E501
        :type: list[TaxLine]
        """

        self._employer_tax_lines = employer_tax_lines

    @property
    def statutory_deduction_lines(self):
        """Gets the statutory_deduction_lines of this PaySlip.  # noqa: E501


        :return: The statutory_deduction_lines of this PaySlip.  # noqa: E501
        :rtype: list[StatutoryDeductionLine]
        """
        return self._statutory_deduction_lines

    @statutory_deduction_lines.setter
    def statutory_deduction_lines(self, statutory_deduction_lines):
        """Sets the statutory_deduction_lines of this PaySlip.


        :param statutory_deduction_lines: The statutory_deduction_lines of this PaySlip.  # noqa: E501
        :type: list[StatutoryDeductionLine]
        """

        self._statutory_deduction_lines = statutory_deduction_lines

    @property
    def tax_settings(self):
        """Gets the tax_settings of this PaySlip.  # noqa: E501


        :return: The tax_settings of this PaySlip.  # noqa: E501
        :rtype: TaxSettings
        """
        return self._tax_settings

    @tax_settings.setter
    def tax_settings(self, tax_settings):
        """Sets the tax_settings of this PaySlip.


        :param tax_settings: The tax_settings of this PaySlip.  # noqa: E501
        :type: TaxSettings
        """

        self._tax_settings = tax_settings

    @property
    def gross_earnings_history(self):
        """Gets the gross_earnings_history of this PaySlip.  # noqa: E501


        :return: The gross_earnings_history of this PaySlip.  # noqa: E501
        :rtype: GrossEarningsHistory
        """
        return self._gross_earnings_history

    @gross_earnings_history.setter
    def gross_earnings_history(self, gross_earnings_history):
        """Sets the gross_earnings_history of this PaySlip.


        :param gross_earnings_history: The gross_earnings_history of this PaySlip.  # noqa: E501
        :type: GrossEarningsHistory
        """

        self._gross_earnings_history = gross_earnings_history

