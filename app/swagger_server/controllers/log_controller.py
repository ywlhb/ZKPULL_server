import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.function2 import pull

def get_log_by_key(deviceKey):
    """
    通过连接句柄取得控制器日志
    
    :param deviceKey: 控制器的连接句柄
    :type deviceKey: int

    :rtype: List[str]
    """
    rk, re = pull.get_log_bykey(deviceKey)
    rs = 400
    if rk >= 0:
        rs = 200
    else:
        rs -= rk
    return re, rs
