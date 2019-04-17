# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestControlController(BaseTestCase):
    """ ControlController integration test stubs """

    def test_control_device_by_key(self):
        """
        Test case for control_device_by_key

        通过连接句柄控制控制器动作
        """
        data = dict(OperationID=789,
                    params=56,
                    option='option_example')
        response = self.client.open('/v1/control/{deviceKey}'.format(deviceKey=789),
                                    method='PUT',
                                    data=data,
                                    content_type='application/x-www-form-urlencoded')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_control_door_by_key(self):
        """
        Test case for control_door_by_key

        通过连接句柄控制开门动作
        """
        query_string = [('doorID', 56),
                        ('openSecond', 56)]
        response = self.client.open('/v1/control/door/{deviceKey}'.format(deviceKey=789),
                                    method='PUT',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " +
                       response.data.decode('utf-8'))

    def test_control_auxout_by_key(self):
        """
        Test case for control_auxout_by_key

        通过连接句柄控制辅助输出动作
        """
        query_string = [('auxIDID', 56),
                        ('openSecond', 56)]
        response = self.client.open('/v1/control/auxout/{deviceKey}'.format(deviceKey=789),
                                    method='PUT',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " +
                       response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
