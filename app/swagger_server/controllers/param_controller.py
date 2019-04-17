import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.function2 import pull


def get_device_param_by_key(deviceKey, paramKeys):
    """
    通过连接句柄查询控制器参数
    返回控制器参数（返回参数是字符串数组，内容形式：Paramkey&#x3D;value）
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param paramKeys: 请求查询的参数名称
    :type paramKeys: List[str]

    :rtype: List[str]
    """
    rk, re = pull.get_param_bykey(deviceKey, paramKeys)
    if rk > 0:
        rs = 200
    elif rk == 0:
        rs = 404
        re = None
    else:
        rs = 403
        re = rk
    return re, rs


def set_device_param_by_key(deviceKey, paramKeyValues):
    """
    通过连接句柄设置控制器参数
    设置控制器参数（参数是字符串数组，内容形式：Paramkey&#x3D;value）
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param paramKeyValues: 需要设置的参数的键值对数组（形式key&#x3D;value）
    :type paramKeyValues: List[str]

    :rtype: List[str]
    """
    rk, re = pull.set_param_bykey(deviceKey, paramKeyValues)
    if rk > 0:
        rs = 200
    elif rk == 0:
        rs = 404
        re = None
    else:
        rs = 403
        re = rk
    return re, rs

def set_device_datetime_by_key(deviceKey, datetime=None):
    """
    通过连接句柄设置控制器时间
    如果不写时间参数，会设置为服务器时间
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param datetime: 需要设置的时间（yyyy-MM-dd HH:mm:ss）
    :type datetime: str

    :rtype: str
    """
    rk, re = pull.set_param_bykey(deviceKey, pull.changeDatetime(datetime))
    if rk > 0:
        rs = 200
    elif rk == 0:
        rs = 404
        re = None
    else:
        rs = 403
        re = rk
    return re, rs
