# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDataController(BaseTestCase):
    """ DataController integration test stubs """

    def test_delete_data_by_key(self):
        """
        Test case for delete_data_by_key

        通过连接句柄与数据表名删除控制器中的数据
        """
        query_string = [('filters', 'filters_example'),
                        ('options', 'options_example')]
        response = self.client.open('/v1/data/{deviceKey}/{tableName}'.format(deviceKey=789, tableName='tableName_example'),
                                    method='DELETE',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_data_by_key(self):
        """
        Test case for get_data_by_key

        通过连接句柄与数据表名取得控制器中的数据
        """
        query_string = [('fieldNames', 'fieldNames_example'),
                        ('filters', 'filters_example'),
                        ('options', 'options_example')]
        response = self.client.open('/v1/data/{deviceKey}/{tableName}'.format(deviceKey=789, tableName='tableName_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_data_by_key(self):
        """
        Test case for set_data_by_key

        通过连接句柄与数据表名设置控制器中的数据
        """
        data = dict(data='data_example',
                    options='options_example')
        response = self.client.open('/v1/data/{deviceKey}/{tableName}'.format(deviceKey=789, tableName='tableName_example'),
                                    method='PUT',
                                    data=data,
                                    content_type='application/x-www-form-urlencoded')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
