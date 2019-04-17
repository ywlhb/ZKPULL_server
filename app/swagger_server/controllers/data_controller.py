import connexion
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.function2 import pull


def delete_data_by_key(deviceKey, tableName, filters=None, options=None):
    """
    通过连接句柄与数据表名删除控制器中的数据
    
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param tableName: 数据表名：用户表&#x3D;user
    :type tableName: str
    :param filters: 筛选器列表
    :type filters: List[str]
    :param options: 默认为空，扩展之用
    :type options: str

    :rtype: None
    """
    if filters == None:
        filters = []
    if options == None:
        options = ''
    rk, re = pull.del_data_bykey(deviceKey, tableName, filters, options)
    rs = 400
    if rk >= 0:
        rs = 200
    else:
        rs -= rk
    return re, rs


def get_data_by_key(deviceKey, tableName, fieldNames=None, filters=None, options=None):
    """
    通过连接句柄与数据表名取得控制器中的数据
    
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param tableName: 数据表名：用户表&#x3D;user
    :type tableName: str
    :param FieldNames: 字段名列表
    :type FieldNames: List[str]
    :param Filters: 筛选器列表
    :type Filters: List[str]
    :param Options: 选项，当前仅在下载门禁事件记录表的数据时有效，值为“New Record”时下载新记录
    :type Options: str

    :rtype: List[str]
    """
    if fieldNames == None: 
        fieldNames = ['*']
    if filters == None:
        filters = []
    if options == None:
        options = ''
    rk, re = pull.get_data_bykey(
        deviceKey, tableName, fieldNames, filters, options)
    rs = 400
    if rk >= 0:
        rs = 200
    else:
        rs -= rk
    return re, rs


def set_data_by_key(deviceKey, tableName, data, options=None):
    """
    通过连接句柄与数据表名设置控制器中的数据
    如果插入的记录的主键已在设备中则覆盖原记录
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param tableName: 数据表名：用户表&#x3D;user
    :type tableName: str
    :param data: 数据内容
    :type data: List[str]
    :param options: 默认为空，扩展之用
    :type options: str

    :rtype: None
    """
    if options == None:
        options = ''
    rk, re = pull.set_data_bykey(deviceKey, tableName, data, options)
    rs = 400
    if rk >= 0:
        rs = 200
    else:
        rs -= rk
    return re, rs


def del_user_by_key(deviceKey, userID):
    """
    通过连接句柄设置控制器中的用户数据
    如果插入的记录的主键已在设备中则覆盖原记录
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param userID: 
    :type userID: str

    :rtype: None
    """
    rk, re = pull.del_user_bykey(deviceKey, userID)
    rs = 400
    if rk > 0:
        rs = 200
    else:
        rs -= rk
    return re, rs


def get_user_by_key(deviceKey, userID):
    """
    通过连接句柄设置控制器中的用户数据
    如果插入的记录的主键已在设备中则覆盖原记录
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param userID: 
    :type userID: str

    :rtype: User
    """
    rk, re = pull.get_user_bykey(deviceKey, userID)
    rs = 400
    if rk > 0:
        rs = 200
    else:
        rs -= rk
    return re, rs

def set_user_by_key(deviceKey, user):
    """
    通过连接句柄设置控制器中的用户数据
    如果插入的记录的主键已在设备中则覆盖原记录
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param user: 
    :type user: dict | bytes

    :rtype: None
    """
    re, rk = 0, 0
    rs = 400
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())
        rk, re = pull.set_user_bykey(deviceKey, user)
    
    if rk > 0:
        rs = 200
    else:
        rs -= rk
    return re, rs

