import connexion
from swagger_server.models.tcp_con_param import TcpConParam
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.function2 import pull

def creat_connect_key(tcpConParam):
    """
    创建控制器的链接句柄
    
    :param tcpConParam: 控制器TCP连接参数
    :type tcpConParam: dict | bytes

    :rtype: int
    """
    re, rk = 0,0
    rs = 400
    if connexion.request.is_json:
        tcpConParam = TcpConParam.from_dict(connexion.request.get_json())
        rk,re = pull.add_connect(tcpConParam.to_dict())

    if rk > 0:
        if rk == re:
            rs = 201
        else:
            rs = 200
    else:
        rs = 400
    return re, rs


def delete_connect(deviceKey):
    """
    关闭并删除控制器连接
    
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int

    :rtype: None
    """
    rk, re = pull.del_connect(deviceKey)
    rs = 400
    if rk > 0:
        rs = 200
    else:
        rs = 404
    return re, rs


def get_con_param_by_hd(deviceKey):
    """
    通过连接句柄查询链接信息
    返回TCP链接参数（不含链接密码）
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int

    :rtype: TcpConParam
    """
    rk, re = pull.get_connect_bykey(deviceKey)
    rs = 0
    conp = None
    if rk > 0:
        rs = 200
        conp = TcpConParam.from_dict(re)
    else:
        rs = 404
    return conp, rs


def get_connect_key(ipAddress):
    """
    通过IP查询控制器链接句柄
    
    :param ipAddress: 控制器TCP连接的IP地址
    :type ipAddress: str

    :rtype: int
    """
    rk, re = pull.get_connect_key(ipAddress)
    rs = 400
    if rk > 0:
        rs = 200
    return re, rs
