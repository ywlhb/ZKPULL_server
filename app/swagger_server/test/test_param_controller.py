# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestParamController(BaseTestCase):
    """ ParamController integration test stubs """

    def test_get_device_param_by_key(self):
        """
        Test case for get_device_param_by_key

        通过连接句柄查询控制器参数
        """
        query_string = [('paramKeys', 'paramKeys_example')]
        response = self.client.open('/v1/param/{deviceKey}'.format(deviceKey=789),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_device_datetime_by_key(self):
        """
        Test case for set_device_datetime_by_key

        通过连接句柄设置控制器时间
        """
        query_string = [('datetime', 'datetime_example')]
        response = self.client.open('/v1/param/datetime/{deviceKey}'.format(deviceKey=789),
                                    method='PUT',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_device_param_by_key(self):
        """
        Test case for set_device_param_by_key

        通过连接句柄设置控制器参数
        """
        data = dict(paramKeyValues='paramKeyValues_example')
        response = self.client.open('/v1/param/{deviceKey}'.format(deviceKey=789),
                                    method='PUT',
                                    data=data,
                                    content_type='application/x-www-form-urlencoded')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
