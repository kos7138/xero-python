# coding: utf-8

"""
    Xero Files API

    These endpoints are specific to Xero Files API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class FileObject(BaseModel):
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
        'name': 'str',
        'mime_type': 'str',
        'size': 'int',
        'created_date_utc': 'str',
        'updated_date_utc': 'str',
        'user': 'User',
        'id': 'str',
        'folder_id': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'mime_type': 'MimeType',
        'size': 'Size',
        'created_date_utc': 'CreatedDateUtc',
        'updated_date_utc': 'UpdatedDateUtc',
        'user': 'User',
        'id': 'Id',
        'folder_id': 'FolderId'
    }

    def __init__(self, name=None, mime_type=None, size=None, created_date_utc=None, updated_date_utc=None, user=None, id=None, folder_id=None):  # noqa: E501
        """FileObject - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._mime_type = None
        self._size = None
        self._created_date_utc = None
        self._updated_date_utc = None
        self._user = None
        self._id = None
        self._folder_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if mime_type is not None:
            self.mime_type = mime_type
        if size is not None:
            self.size = size
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if user is not None:
            self.user = user
        if id is not None:
            self.id = id
        if folder_id is not None:
            self.folder_id = folder_id

    @property
    def name(self):
        """Gets the name of this FileObject.  # noqa: E501

        File Name  # noqa: E501

        :return: The name of this FileObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileObject.

        File Name  # noqa: E501

        :param name: The name of this FileObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mime_type(self):
        """Gets the mime_type of this FileObject.  # noqa: E501

        MimeType of the file (image/png, image/jpeg, application/pdf, etc..)  # noqa: E501

        :return: The mime_type of this FileObject.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this FileObject.

        MimeType of the file (image/png, image/jpeg, application/pdf, etc..)  # noqa: E501

        :param mime_type: The mime_type of this FileObject.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def size(self):
        """Gets the size of this FileObject.  # noqa: E501

        Numeric value in bytes  # noqa: E501

        :return: The size of this FileObject.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileObject.

        Numeric value in bytes  # noqa: E501

        :param size: The size of this FileObject.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def created_date_utc(self):
        """Gets the created_date_utc of this FileObject.  # noqa: E501

        Created date in UTC  # noqa: E501

        :return: The created_date_utc of this FileObject.  # noqa: E501
        :rtype: str
        """
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        """Sets the created_date_utc of this FileObject.

        Created date in UTC  # noqa: E501

        :param created_date_utc: The created_date_utc of this FileObject.  # noqa: E501
        :type: str
        """

        self._created_date_utc = created_date_utc

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this FileObject.  # noqa: E501

        Updated date in UTC  # noqa: E501

        :return: The updated_date_utc of this FileObject.  # noqa: E501
        :rtype: str
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this FileObject.

        Updated date in UTC  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this FileObject.  # noqa: E501
        :type: str
        """

        self._updated_date_utc = updated_date_utc

    @property
    def user(self):
        """Gets the user of this FileObject.  # noqa: E501


        :return: The user of this FileObject.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FileObject.


        :param user: The user of this FileObject.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def id(self):
        """Gets the id of this FileObject.  # noqa: E501

        File object's UUID  # noqa: E501

        :return: The id of this FileObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileObject.

        File object's UUID  # noqa: E501

        :param id: The id of this FileObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def folder_id(self):
        """Gets the folder_id of this FileObject.  # noqa: E501

        Folder relation object's UUID  # noqa: E501

        :return: The folder_id of this FileObject.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FileObject.

        Folder relation object's UUID  # noqa: E501

        :param folder_id: The folder_id of this FileObject.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

