# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ccp.apis.v1.ccp_server.models.base_model_ import Model
from ccp.apis.v1.ccp_server.models.meta import Meta  # noqa: F401,E501
from ccp.apis.v1.ccp_server.models.prebuild_lint_build_scan_logs import \
    PrebuildLintBuildScanLogs  # noqa: F401,E501
from ccp.apis.v1.ccp_server import util


class BuildLogs(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, meta: Meta = None, build: str = None,
                 pre_build: bool = None, status: str = None,
                 failed_stage: str = None,
                 logs: PrebuildLintBuildScanLogs = None):  # noqa: E501
        """BuildLogs - a model defined in Swagger

        :param meta: The meta of this BuildLogs.  # noqa: E501
        :type meta: Meta
        :param build: The build of this BuildLogs.  # noqa: E501
        :type build: str
        :param pre_build: The pre_build of this BuildLogs.  # noqa: E501
        :type pre_build: bool
        :param status: The status of this BuildLogs.  # noqa: E501
        :type status: str
        :param failed_stage: The failed_stage of this BuildLogs.  # noqa: E501
        :type failed_stage: str
        :param logs: The logs of this BuildLogs.  # noqa: E501
        :type logs: PrebuildLintBuildScanLogs
        """
        self.swagger_types = {
            'meta': Meta,
            'build': str,
            'pre_build': bool,
            'status': str,
            'failed_stage': str,
            'logs': PrebuildLintBuildScanLogs
        }

        self.attribute_map = {
            'meta': 'meta',
            'build': 'build',
            'pre_build': 'pre-build',
            'status': 'status',
            'failed_stage': 'failed-stage',
            'logs': 'logs'
        }

        self._meta = meta
        self._build = build
        self._pre_build = pre_build
        self._status = status
        self._failed_stage = failed_stage
        self._logs = logs

    @classmethod
    def from_dict(cls, dikt) -> 'BuildLogs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BuildLogs of this BuildLogs.  # noqa: E501
        :rtype: BuildLogs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> Meta:
        """Gets the meta of this BuildLogs.


        :return: The meta of this BuildLogs.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        """Sets the meta of this BuildLogs.


        :param meta: The meta of this BuildLogs.
        :type meta: Meta
        """

        self._meta = meta

    @property
    def build(self) -> str:
        """Gets the build of this BuildLogs.


        :return: The build of this BuildLogs.
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build: str):
        """Sets the build of this BuildLogs.


        :param build: The build of this BuildLogs.
        :type build: str
        """

        self._build = build

    @property
    def pre_build(self) -> bool:
        """Gets the pre_build of this BuildLogs.


        :return: The pre_build of this BuildLogs.
        :rtype: bool
        """
        return self._pre_build

    @pre_build.setter
    def pre_build(self, pre_build: bool):
        """Sets the pre_build of this BuildLogs.


        :param pre_build: The pre_build of this BuildLogs.
        :type pre_build: bool
        """

        self._pre_build = pre_build

    @property
    def status(self) -> str:
        """Gets the status of this BuildLogs.


        :return: The status of this BuildLogs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this BuildLogs.


        :param status: The status of this BuildLogs.
        :type status: str
        """

        self._status = status

    @property
    def failed_stage(self) -> str:
        """Gets the failed_stage of this BuildLogs.


        :return: The failed_stage of this BuildLogs.
        :rtype: str
        """
        return self._failed_stage

    @failed_stage.setter
    def failed_stage(self, failed_stage: str):
        """Sets the failed_stage of this BuildLogs.


        :param failed_stage: The failed_stage of this BuildLogs.
        :type failed_stage: str
        """

        self._failed_stage = failed_stage

    @property
    def logs(self) -> PrebuildLintBuildScanLogs:
        """Gets the logs of this BuildLogs.


        :return: The logs of this BuildLogs.
        :rtype: PrebuildLintBuildScanLogs
        """
        return self._logs

    @logs.setter
    def logs(self, logs: PrebuildLintBuildScanLogs):
        """Sets the logs of this BuildLogs.


        :param logs: The logs of this BuildLogs.
        :type logs: PrebuildLintBuildScanLogs
        """

        self._logs = logs
