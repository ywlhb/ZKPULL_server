# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUserController(BaseTestCase):
    """ UserController integration test stubs """

    def test_del_user_by_key(self):
        """
        Test case for del_user_by_key

        通过连接句柄设置控制器中的用户数据
        """
        query_string = [('userID', 'userID_example')]
        response = self.client.open('/v1/data/user/{deviceKey}'.format(deviceKey=789),
                                    method='DELETE',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_user_by_key(self):
        """
        Test case for get_user_by_key

        通过连接句柄设置控制器中的用户数据
        """
        query_string = [('userID', 'userID_example')]
        response = self.client.open('/v1/data/user/{deviceKey}'.format(deviceKey=789),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_user_by_key(self):
        """
        Test case for set_user_by_key

        通过连接句柄设置控制器中的用户数据
        """
        user = User()
        response = self.client.open('/v1/data/user/{deviceKey}'.format(deviceKey=789),
                                    method='PUT',
                                    data=json.dumps(user),
                                    content_type='application/x-www-form-urlencoded')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
