# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ccp.apis.v1.ccp_server.models.base_model_ import Model
from ccp.apis.v1.ccp_server.models.meta import Meta  # noqa: F401,E501
from ccp.apis.v1.ccp_server import util


class TargetFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, meta: Meta = None, prebuild: bool = None,
                 target_file_link: str = None):  # noqa: E501
        """TargetFile - a model defined in Swagger

        :param meta: The meta of this TargetFile.  # noqa: E501
        :type meta: Meta
        :param prebuild: The prebuild of this TargetFile.  # noqa: E501
        :type prebuild: bool
        :param target_file_link: The target_file_link of this TargetFile.  # noqa: E501
        :type target_file_link: str
        """
        self.swagger_types = {
            'meta': Meta,
            'prebuild': bool,
            'target_file_link': str
        }

        self.attribute_map = {
            'meta': 'meta',
            'prebuild': 'prebuild',
            'target_file_link': 'target_file_link'
        }

        self._meta = meta
        self._prebuild = prebuild
        self._target_file_link = target_file_link

    @classmethod
    def from_dict(cls, dikt) -> 'TargetFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TargetFile of this TargetFile.  # noqa: E501
        :rtype: TargetFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> Meta:
        """Gets the meta of this TargetFile.


        :return: The meta of this TargetFile.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        """Sets the meta of this TargetFile.


        :param meta: The meta of this TargetFile.
        :type meta: Meta
        """

        self._meta = meta

    @property
    def prebuild(self) -> bool:
        """Gets the prebuild of this TargetFile.


        :return: The prebuild of this TargetFile.
        :rtype: bool
        """
        return self._prebuild

    @prebuild.setter
    def prebuild(self, prebuild: bool):
        """Sets the prebuild of this TargetFile.


        :param prebuild: The prebuild of this TargetFile.
        :type prebuild: bool
        """

        self._prebuild = prebuild

    @property
    def target_file_link(self) -> str:
        """Gets the target_file_link of this TargetFile.


        :return: The target_file_link of this TargetFile.
        :rtype: str
        """
        return self._target_file_link

    @target_file_link.setter
    def target_file_link(self, target_file_link: str):
        """Sets the target_file_link of this TargetFile.


        :param target_file_link: The target_file_link of this TargetFile.
        :type target_file_link: str
        """

        self._target_file_link = target_file_link
