# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class TcpConParam(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ip: str=None, port: int=None, timeout: int=None, passwd: str=None, hd: int=None):
        """
        TcpConParam - a model defined in Swagger

        :param ip: The ip of this TcpConParam.
        :type ip: str
        :param port: The port of this TcpConParam.
        :type port: int
        :param timeout: The timeout of this TcpConParam.
        :type timeout: int
        :param passwd: The passwd of this TcpConParam.
        :type passwd: str
        :param hd: The hd of this TcpConParam.
        :type hd: int
        """
        self.swagger_types = {
            'ip': str,
            'port': int,
            'timeout': int,
            'passwd': str,
            'hd': int
        }

        self.attribute_map = {
            'ip': 'ip',
            'port': 'port',
            'timeout': 'timeout',
            'passwd': 'passwd',
            'hd': 'hd'
        }

        self._ip = ip
        self._port = port
        self._timeout = timeout
        self._passwd = passwd
        self._hd = hd

    @classmethod
    def from_dict(cls, dikt) -> 'TcpConParam':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TcpConParam of this TcpConParam.
        :rtype: TcpConParam
        """
        return deserialize_model(dikt, cls)

    @property
    def ip(self) -> str:
        """
        Gets the ip of this TcpConParam.

        :return: The ip of this TcpConParam.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """
        Sets the ip of this TcpConParam.

        :param ip: The ip of this TcpConParam.
        :type ip: str
        """

        self._ip = ip

    @property
    def port(self) -> int:
        """
        Gets the port of this TcpConParam.

        :return: The port of this TcpConParam.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """
        Sets the port of this TcpConParam.

        :param port: The port of this TcpConParam.
        :type port: int
        """

        self._port = port

    @property
    def timeout(self) -> int:
        """
        Gets the timeout of this TcpConParam.

        :return: The timeout of this TcpConParam.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout: int):
        """
        Sets the timeout of this TcpConParam.

        :param timeout: The timeout of this TcpConParam.
        :type timeout: int
        """

        self._timeout = timeout

    @property
    def passwd(self) -> str:
        """
        Gets the passwd of this TcpConParam.

        :return: The passwd of this TcpConParam.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd: str):
        """
        Sets the passwd of this TcpConParam.

        :param passwd: The passwd of this TcpConParam.
        :type passwd: str
        """

        self._passwd = passwd

    @property
    def hd(self) -> int:
        """
        Gets the hd of this TcpConParam.

        :return: The hd of this TcpConParam.
        :rtype: int
        """
        return self._hd

    @hd.setter
    def hd(self, hd: int):
        """
        Sets the hd of this TcpConParam.

        :param hd: The hd of this TcpConParam.
        :type hd: int
        """

        self._hd = hd

