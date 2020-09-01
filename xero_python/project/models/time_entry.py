# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.2.14
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TimeEntry(BaseModel):
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
        "time_entry_id": "str",
        "user_id": "str",
        "project_id": "str",
        "task_id": "str",
        "date_utc": "datetime",
        "date_entered_utc": "datetime",
        "duration": "int",
        "description": "str",
        "status": "str",
    }

    attribute_map = {
        "time_entry_id": "timeEntryId",
        "user_id": "userId",
        "project_id": "projectId",
        "task_id": "taskId",
        "date_utc": "dateUtc",
        "date_entered_utc": "dateEnteredUtc",
        "duration": "duration",
        "description": "description",
        "status": "status",
    }

    def __init__(
        self,
        time_entry_id=None,
        user_id=None,
        project_id=None,
        task_id=None,
        date_utc=None,
        date_entered_utc=None,
        duration=None,
        description=None,
        status=None,
    ):  # noqa: E501
        """TimeEntry - a model defined in OpenAPI"""  # noqa: E501

        self._time_entry_id = None
        self._user_id = None
        self._project_id = None
        self._task_id = None
        self._date_utc = None
        self._date_entered_utc = None
        self._duration = None
        self._description = None
        self._status = None
        self.discriminator = None

        if time_entry_id is not None:
            self.time_entry_id = time_entry_id
        if user_id is not None:
            self.user_id = user_id
        if project_id is not None:
            self.project_id = project_id
        if task_id is not None:
            self.task_id = task_id
        if date_utc is not None:
            self.date_utc = date_utc
        if date_entered_utc is not None:
            self.date_entered_utc = date_entered_utc
        if duration is not None:
            self.duration = duration
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def time_entry_id(self):
        """Gets the time_entry_id of this TimeEntry.  # noqa: E501

        Identifier of the time entry.  # noqa: E501

        :return: The time_entry_id of this TimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._time_entry_id

    @time_entry_id.setter
    def time_entry_id(self, time_entry_id):
        """Sets the time_entry_id of this TimeEntry.

        Identifier of the time entry.  # noqa: E501

        :param time_entry_id: The time_entry_id of this TimeEntry.  # noqa: E501
        :type: str
        """

        self._time_entry_id = time_entry_id

    @property
    def user_id(self):
        """Gets the user_id of this TimeEntry.  # noqa: E501

        The xero user identifier of the person who logged time.  # noqa: E501

        :return: The user_id of this TimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TimeEntry.

        The xero user identifier of the person who logged time.  # noqa: E501

        :param user_id: The user_id of this TimeEntry.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def project_id(self):
        """Gets the project_id of this TimeEntry.  # noqa: E501

        Identifier of the project, that the task (which the time entry is logged against) belongs to.  # noqa: E501

        :return: The project_id of this TimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TimeEntry.

        Identifier of the project, that the task (which the time entry is logged against) belongs to.  # noqa: E501

        :param project_id: The project_id of this TimeEntry.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def task_id(self):
        """Gets the task_id of this TimeEntry.  # noqa: E501

        Identifier of the task that time entry is logged against.  # noqa: E501

        :return: The task_id of this TimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TimeEntry.

        Identifier of the task that time entry is logged against.  # noqa: E501

        :param task_id: The task_id of this TimeEntry.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def date_utc(self):
        """Gets the date_utc of this TimeEntry.  # noqa: E501

        The date time that time entry is logged on. UTC Date Time in ISO-8601 format.  # noqa: E501

        :return: The date_utc of this TimeEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        """Sets the date_utc of this TimeEntry.

        The date time that time entry is logged on. UTC Date Time in ISO-8601 format.  # noqa: E501

        :param date_utc: The date_utc of this TimeEntry.  # noqa: E501
        :type: datetime
        """

        self._date_utc = date_utc

    @property
    def date_entered_utc(self):
        """Gets the date_entered_utc of this TimeEntry.  # noqa: E501

        The date time that time entry is created. UTC Date Time in ISO-8601 format. By default it is set to server time.  # noqa: E501

        :return: The date_entered_utc of this TimeEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._date_entered_utc

    @date_entered_utc.setter
    def date_entered_utc(self, date_entered_utc):
        """Sets the date_entered_utc of this TimeEntry.

        The date time that time entry is created. UTC Date Time in ISO-8601 format. By default it is set to server time.  # noqa: E501

        :param date_entered_utc: The date_entered_utc of this TimeEntry.  # noqa: E501
        :type: datetime
        """

        self._date_entered_utc = date_entered_utc

    @property
    def duration(self):
        """Gets the duration of this TimeEntry.  # noqa: E501

        The duration of logged minutes.  # noqa: E501

        :return: The duration of this TimeEntry.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimeEntry.

        The duration of logged minutes.  # noqa: E501

        :param duration: The duration of this TimeEntry.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def description(self):
        """Gets the description of this TimeEntry.  # noqa: E501

        A description of the time entry.  # noqa: E501

        :return: The description of this TimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TimeEntry.

        A description of the time entry.  # noqa: E501

        :param description: The description of this TimeEntry.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this TimeEntry.  # noqa: E501

        Status of the time entry. By default a time entry is created with status of `ACTIVE`. A `LOCKED` state indicates that the time entry is currently changing state (for example being invoiced). Updates are not allowed when in this state. It will have a status of INVOICED once it is invoiced.  # noqa: E501

        :return: The status of this TimeEntry.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TimeEntry.

        Status of the time entry. By default a time entry is created with status of `ACTIVE`. A `LOCKED` state indicates that the time entry is currently changing state (for example being invoiced). Updates are not allowed when in this state. It will have a status of INVOICED once it is invoiced.  # noqa: E501

        :param status: The status of this TimeEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "LOCKED", "None"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status
