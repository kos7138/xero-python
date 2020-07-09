# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Phone(BaseModel):
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
        "phone_type": "str",
        "phone_number": "str",
        "phone_area_code": "str",
        "phone_country_code": "str",
    }

    attribute_map = {
        "phone_type": "PhoneType",
        "phone_number": "PhoneNumber",
        "phone_area_code": "PhoneAreaCode",
        "phone_country_code": "PhoneCountryCode",
    }

    def __init__(
        self,
        phone_type=None,
        phone_number=None,
        phone_area_code=None,
        phone_country_code=None,
    ):  # noqa: E501
        """Phone - a model defined in OpenAPI"""  # noqa: E501

        self._phone_type = None
        self._phone_number = None
        self._phone_area_code = None
        self._phone_country_code = None
        self.discriminator = None

        if phone_type is not None:
            self.phone_type = phone_type
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_area_code is not None:
            self.phone_area_code = phone_area_code
        if phone_country_code is not None:
            self.phone_country_code = phone_country_code

    @property
    def phone_type(self):
        """Gets the phone_type of this Phone.  # noqa: E501


        :return: The phone_type of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """Sets the phone_type of this Phone.


        :param phone_type: The phone_type of this Phone.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "DDI", "MOBILE", "FAX", "OFFICE"]  # noqa: E501
        if phone_type not in allowed_values:
            raise ValueError(
                "Invalid value for `phone_type` ({0}), must be one of {1}".format(  # noqa: E501
                    phone_type, allowed_values
                )
            )

        self._phone_type = phone_type

    @property
    def phone_number(self):
        """Gets the phone_number of this Phone.  # noqa: E501

        max length = 50  # noqa: E501

        :return: The phone_number of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Phone.

        max length = 50  # noqa: E501

        :param phone_number: The phone_number of this Phone.  # noqa: E501
        :type: str
        """
        if phone_number is not None and len(phone_number) > 50:
            raise ValueError(
                "Invalid value for `phone_number`, "
                "length must be less than or equal to `50`"
            )  # noqa: E501

        self._phone_number = phone_number

    @property
    def phone_area_code(self):
        """Gets the phone_area_code of this Phone.  # noqa: E501

        max length = 10  # noqa: E501

        :return: The phone_area_code of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._phone_area_code

    @phone_area_code.setter
    def phone_area_code(self, phone_area_code):
        """Sets the phone_area_code of this Phone.

        max length = 10  # noqa: E501

        :param phone_area_code: The phone_area_code of this Phone.  # noqa: E501
        :type: str
        """
        if phone_area_code is not None and len(phone_area_code) > 10:
            raise ValueError(
                "Invalid value for `phone_area_code`, "
                "length must be less than or equal to `10`"
            )  # noqa: E501

        self._phone_area_code = phone_area_code

    @property
    def phone_country_code(self):
        """Gets the phone_country_code of this Phone.  # noqa: E501

        max length = 20  # noqa: E501

        :return: The phone_country_code of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._phone_country_code

    @phone_country_code.setter
    def phone_country_code(self, phone_country_code):
        """Sets the phone_country_code of this Phone.

        max length = 20  # noqa: E501

        :param phone_country_code: The phone_country_code of this Phone.  # noqa: E501
        :type: str
        """
        if phone_country_code is not None and len(phone_country_code) > 20:
            raise ValueError(
                "Invalid value for `phone_country_code`, "
                "length must be less than or equal to `20`"
            )  # noqa: E501

        self._phone_country_code = phone_country_code
