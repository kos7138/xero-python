# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class Problem(BaseModel):
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
        'type': 'str',
        'title': 'str',
        'status': 'str',
        'detail': 'str',
        'instance': 'str',
        'invalid_fields': 'list[InvalidField]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance',
        'invalid_fields': 'invalidFields'
    }

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, invalid_fields=None):  # noqa: E501
        """Problem - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self._invalid_fields = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if instance is not None:
            self.instance = instance
        if invalid_fields is not None:
            self.invalid_fields = invalid_fields

    @property
    def type(self):
        """Gets the type of this Problem.  # noqa: E501

        The type of error format  # noqa: E501

        :return: The type of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Problem.

        The type of error format  # noqa: E501

        :param type: The type of this Problem.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this Problem.  # noqa: E501

        The type of the error  # noqa: E501

        :return: The title of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Problem.

        The type of the error  # noqa: E501

        :param title: The title of this Problem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this Problem.  # noqa: E501

        The error status code  # noqa: E501

        :return: The status of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Problem.

        The error status code  # noqa: E501

        :param status: The status of this Problem.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this Problem.  # noqa: E501

        A description of the error  # noqa: E501

        :return: The detail of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Problem.

        A description of the error  # noqa: E501

        :param detail: The detail of this Problem.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this Problem.  # noqa: E501


        :return: The instance of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Problem.


        :param instance: The instance of this Problem.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def invalid_fields(self):
        """Gets the invalid_fields of this Problem.  # noqa: E501


        :return: The invalid_fields of this Problem.  # noqa: E501
        :rtype: list[InvalidField]
        """
        return self._invalid_fields

    @invalid_fields.setter
    def invalid_fields(self, invalid_fields):
        """Sets the invalid_fields of this Problem.


        :param invalid_fields: The invalid_fields of this Problem.  # noqa: E501
        :type: list[InvalidField]
        """

        self._invalid_fields = invalid_fields

