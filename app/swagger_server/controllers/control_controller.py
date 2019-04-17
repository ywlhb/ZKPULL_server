import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.function2 import pull


def control_device_by_key(deviceKey, OperationID, params, option=None):
    """
    通过连接句柄控制控制器动作
    返回控制器参数（返回参数是字符串数组，内容形式：Paramkey&#x3D;value）
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param OperationID: 
    :type OperationID: int
    :param params: 操作参数：
    :type params: List[int]
    :param option: 默认为空，扩展之用
    :type option: str

    :rtype: None
    """
    rk, re = pull.control_device_bykey(
        deviceKey, OperationID, params)  # 暂时不传option
    rs = 400
    if rk > 0:
        rs = 200
    else:
        rs -= rk
    return re, rs


def control_door_by_key(deviceKey, doorID=1, openSecond=5):
    """
    通过连接句柄控制开门动作
    
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param doorID: 门号（1-4）
    :type doorID: int
    :param openSecond: 开门时间（1-60秒）
    :type openSecond: List[int]

    :rtype: None
    """
    rk, re = pull.control_device_bykey(
        deviceKey, 1, [doorID, 1, openSecond,0])  # 暂时不传option
    rs = 400
    if rk > 0:
        rs = 200
    else:
        rs -= rk
    return re, rs


def control_auxout_by_key(deviceKey, auxoutID=1, openSecond=2):
    """
    通过连接句柄控制辅助输出动作
    
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int
    :param doorID: 辅助输出地址（1-4）
    :type doorID: int

    :rtype: None
    """
    rk, re = pull.control_device_bykey(
        deviceKey, 1, [auxoutID, 2, openSecond, 0])  # 暂时不传option
    rs = 400
    if rk > 0:
        rs = 200
    else:
        rs -= rk
    return re, rs
