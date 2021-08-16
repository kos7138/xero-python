# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class EarningsTemplateObject(BaseModel):
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
        'earning_template': 'EarningsTemplate'
    }

    attribute_map = {
        'pagination': 'pagination',
        'problem': 'problem',
        'earning_template': 'earningTemplate'
    }

    def __init__(self, pagination=None, problem=None, earning_template=None):  # noqa: E501
        """EarningsTemplateObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._earning_template = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earning_template is not None:
            self.earning_template = earning_template

    @property
    def pagination(self):
        """Gets the pagination of this EarningsTemplateObject.  # noqa: E501


        :return: The pagination of this EarningsTemplateObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EarningsTemplateObject.


        :param pagination: The pagination of this EarningsTemplateObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EarningsTemplateObject.  # noqa: E501


        :return: The problem of this EarningsTemplateObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EarningsTemplateObject.


        :param problem: The problem of this EarningsTemplateObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def earning_template(self):
        """Gets the earning_template of this EarningsTemplateObject.  # noqa: E501


        :return: The earning_template of this EarningsTemplateObject.  # noqa: E501
        :rtype: EarningsTemplate
        """
        return self._earning_template

    @earning_template.setter
    def earning_template(self, earning_template):
        """Sets the earning_template of this EarningsTemplateObject.


        :param earning_template: The earning_template of this EarningsTemplateObject.  # noqa: E501
        :type: EarningsTemplate
        """

        self._earning_template = earning_template

