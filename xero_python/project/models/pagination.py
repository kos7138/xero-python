# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel

class Pagination(BaseModel):
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
        'page': 'int',
        'page_size': 'int',
        'page_count': 'int',
        'item_count': 'int'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'pageSize',
        'page_count': 'pageCount',
        'item_count': 'itemCount'
    }

    def __init__(self, page=None, page_size=None, page_count=None, item_count=None):  # noqa: E501
        """Pagination - a model defined in OpenAPI"""  # noqa: E501

        self._page = None
        self._page_size = None
        self._page_count = None
        self._item_count = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if page_count is not None:
            self.page_count = page_count
        if item_count is not None:
            self.item_count = item_count

    @property
    def page(self):
        """Gets the page of this Pagination.  # noqa: E501

        Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.  # noqa: E501

        :return: The page of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this Pagination.

        Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.  # noqa: E501

        :param page: The page of this Pagination.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this Pagination.  # noqa: E501

        Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.  # noqa: E501

        :return: The page_size of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this Pagination.

        Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.  # noqa: E501

        :param page_size: The page_size of this Pagination.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_count(self):
        """Gets the page_count of this Pagination.  # noqa: E501

        Number of pages available  # noqa: E501

        :return: The page_count of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this Pagination.

        Number of pages available  # noqa: E501

        :param page_count: The page_count of this Pagination.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def item_count(self):
        """Gets the item_count of this Pagination.  # noqa: E501

        Number of items returned  # noqa: E501

        :return: The item_count of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this Pagination.

        Number of items returned  # noqa: E501

        :param item_count: The item_count of this Pagination.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

