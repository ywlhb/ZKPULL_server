# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.tcp_con_param import TcpConParam
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestConnectController(BaseTestCase):
    """ ConnectController integration test stubs """

    def test_creat_connect_key(self):
        """
        Test case for creat_connect_key

        创建控制器的链接句柄
        """
        tcpConParam = TcpConParam()
        response = self.client.open('/v1/connect',
                                    method='POST',
                                    data=json.dumps(tcpConParam),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_connect(self):
        """
        Test case for delete_connect

        关闭并删除控制器连接
        """
        response = self.client.open('/v1/connect/{deviceKey}'.format(deviceKey=789),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_con_param_by_hd(self):
        """
        Test case for get_con_param_by_hd

        通过连接句柄查询链接信息
        """
        response = self.client.open('/v1/connect/{deviceKey}'.format(deviceKey=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_connect_key(self):
        """
        Test case for get_connect_key

        通过IP查询控制器链接句柄
        """
        query_string = [('ipAddress', 'ipAddress_example')]
        response = self.client.open('/v1/connect',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
