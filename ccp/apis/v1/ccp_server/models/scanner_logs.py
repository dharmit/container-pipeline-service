# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ccp.apis.v1.ccp_server.models.base_model_ import Model
from ccp.apis.v1.ccp_server import util


class ScannerLogs(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, logs: str = None, description: str = None):  # noqa: E501
        """ScannerLogs - a model defined in Swagger

        :param logs: The logs of this ScannerLogs.  # noqa: E501
        :type logs: str
        :param description: The description of this ScannerLogs.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'logs': str,
            'description': str
        }

        self.attribute_map = {
            'logs': 'logs',
            'description': 'description'
        }

        self._logs = logs
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'ScannerLogs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScannerLogs of this ScannerLogs.  # noqa: E501
        :rtype: ScannerLogs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def logs(self) -> str:
        """Gets the logs of this ScannerLogs.


        :return: The logs of this ScannerLogs.
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs: str):
        """Sets the logs of this ScannerLogs.


        :param logs: The logs of this ScannerLogs.
        :type logs: str
        """

        self._logs = logs

    @property
    def description(self) -> str:
        """Gets the description of this ScannerLogs.


        :return: The description of this ScannerLogs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ScannerLogs.


        :param description: The description of this ScannerLogs.
        :type description: str
        """

        self._description = description
