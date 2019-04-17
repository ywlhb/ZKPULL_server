# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestLogController(BaseTestCase):
    """ LogController integration test stubs """

    def test_get_log_by_key(self):
        """
        Test case for get_log_by_key

        通过连接句柄取得控制器日志
        """
        response = self.client.open('/v1/log/{deviceKey}'.format(deviceKey=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
