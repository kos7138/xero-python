# coding: utf-8

"""
    Xero Files API

    These endpoints are specific to Xero Files API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class Association(BaseModel):
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
        'file_id': 'str',
        'object_id': 'str',
        'object_group': 'ObjectGroup',
        'object_type': 'ObjectType'
    }

    attribute_map = {
        'file_id': 'FileId',
        'object_id': 'ObjectId',
        'object_group': 'ObjectGroup',
        'object_type': 'ObjectType'
    }

    def __init__(self, file_id=None, object_id=None, object_group=None, object_type=None):  # noqa: E501
        """Association - a model defined in OpenAPI"""  # noqa: E501

        self._file_id = None
        self._object_id = None
        self._object_group = None
        self._object_type = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if object_id is not None:
            self.object_id = object_id
        if object_group is not None:
            self.object_group = object_group
        if object_type is not None:
            self.object_type = object_type

    @property
    def file_id(self):
        """Gets the file_id of this Association.  # noqa: E501

        The unique identifier of the file  # noqa: E501

        :return: The file_id of this Association.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this Association.

        The unique identifier of the file  # noqa: E501

        :param file_id: The file_id of this Association.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def object_id(self):
        """Gets the object_id of this Association.  # noqa: E501

        The identifier of the object that the file is being associated with (e.g. InvoiceID, BankTransactionID, ContactID)  # noqa: E501

        :return: The object_id of this Association.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this Association.

        The identifier of the object that the file is being associated with (e.g. InvoiceID, BankTransactionID, ContactID)  # noqa: E501

        :param object_id: The object_id of this Association.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_group(self):
        """Gets the object_group of this Association.  # noqa: E501


        :return: The object_group of this Association.  # noqa: E501
        :rtype: ObjectGroup
        """
        return self._object_group

    @object_group.setter
    def object_group(self, object_group):
        """Sets the object_group of this Association.


        :param object_group: The object_group of this Association.  # noqa: E501
        :type: ObjectGroup
        """

        self._object_group = object_group

    @property
    def object_type(self):
        """Gets the object_type of this Association.  # noqa: E501


        :return: The object_type of this Association.  # noqa: E501
        :rtype: ObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Association.


        :param object_type: The object_type of this Association.  # noqa: E501
        :type: ObjectType
        """

        self._object_type = object_type

