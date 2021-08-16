# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class EmployeeEarningsTemplates(BaseModel):
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
        'pagination': 'Pagination',
        'problem': 'Problem',
        'earning_templates': 'list[EarningsTemplate]'
    }

    attribute_map = {
        'pagination': 'pagination',
        'problem': 'problem',
        'earning_templates': 'earningTemplates'
    }

    def __init__(self, pagination=None, problem=None, earning_templates=None):  # noqa: E501
        """EmployeeEarningsTemplates - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._earning_templates = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earning_templates is not None:
            self.earning_templates = earning_templates

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeEarningsTemplates.  # noqa: E501


        :return: The pagination of this EmployeeEarningsTemplates.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeEarningsTemplates.


        :param pagination: The pagination of this EmployeeEarningsTemplates.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeEarningsTemplates.  # noqa: E501


        :return: The problem of this EmployeeEarningsTemplates.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeEarningsTemplates.


        :param problem: The problem of this EmployeeEarningsTemplates.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def earning_templates(self):
        """Gets the earning_templates of this EmployeeEarningsTemplates.  # noqa: E501


        :return: The earning_templates of this EmployeeEarningsTemplates.  # noqa: E501
        :rtype: list[EarningsTemplate]
        """
        return self._earning_templates

    @earning_templates.setter
    def earning_templates(self, earning_templates):
        """Sets the earning_templates of this EmployeeEarningsTemplates.


        :param earning_templates: The earning_templates of this EmployeeEarningsTemplates.  # noqa: E501
        :type: list[EarningsTemplate]
        """

        self._earning_templates = earning_templates

