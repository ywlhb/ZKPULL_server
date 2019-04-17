from ctypes import *
from datetime import date, datetime
from swagger_server.models.user import User
from swagger_server.models.user_finger import UserFinger

connects = {}
ipList = {}
dll = windll.LoadLibrary('plcommpro.dll')

# 1. IntPtr Connect(string Parameters)
dll.Connect.argtypes = [c_char_p]
dll.Connect.restype = c_int

# 2. void Disconnect(IntPtr h)
dll.Disconnect.argtypes = [c_int]

# 3. int SetDeviceParam(IntPtr h, string itemvalues)
dll.SetDeviceParam.argtypes = [c_int, c_char_p]
dll.SetDeviceParam.restype = c_int

# 4. int GetDeviceParam(IntPtr h, ref byte buffer, int buffersize, string itemvalues)
dll.GetDeviceParam.argtypes = [c_int, c_char_p, c_int, c_char_p]
dll.GetDeviceParam.restype = c_int

# 5. int ControlDevice(IntPtr h, int operationid, int param1, int param2, int param3, int param4, string options)
dll.ControlDevice.argtypes = [c_int, c_int, 
                              c_int, c_int, c_int, c_int, c_char_p]
dll.ControlDevice.restype = c_int

# 6. int SetDeviceData(IntPtr h, string tablename, string data, string options)
dll.SetDeviceData.argtypes = [c_int, c_char_p, c_char_p, c_char_p]
dll.SetDeviceData.restype = c_int

# 7. int GetDeviceData(IntPtr h, ref byte buffer, int buffersize, string tablename, string filename, string filter, string options)
dll.GetDeviceData.argtypes = [c_int, c_char_p,
                              c_int, c_char_p, c_char_p, c_char_p, c_char_p]
dll.GetDeviceData.restype = c_int

# 8. int GetDeviceDataCount(IntPtr h, string tablename, string data, string options)
dll.GetDeviceDataCount.argtypes = [c_int, c_char_p, c_char_p, c_char_p]
dll.GetDeviceDataCount.restype = c_int

# 9. int DeleteDeviceData(IntPtr h, string tablename, string data, string options)
dll.DeleteDeviceData.argtypes = [c_int, c_char_p, c_char_p, c_char_p]
dll.DeleteDeviceData.restype = c_int

# 10. int GetRTLog(IntPtr h, ref byte buffer, int buffersize);
dll.GetRTLog.argtypes = [c_int, c_char_p, c_int]
dll.GetRTLog.restype = c_int

# dll.GetRTLogExt.argtypes = [c_int, c_char_p, c_int]
# dll.GetRTLogExt.restype = c_int


def add_connect(param: dict):
    key = 0
    if param['ip'] in ipList:
        key = ipList[param['ip']]
    s = 'protocol=TCP,ipaddress={ip},port={port},timeout=4000,passwd={passwd}'
    conp = param.copy()
    sBuf = bytes(s.format(**conp), encoding="utf8")
    nRst = dll.Connect(sBuf)
    if nRst > 0:
        if key == 0:
            key = nRst
        conp['hd'] = nRst
        connects[key] = conp
        ipList[conp['ip']] = key
    #sBuf = b'protocol=TCP,ipaddress=192.168.50.143,port=4370,timeout=4000,passwd='
    return nRst, key

def get_connect_key(ip):
    if ip in ipList:
        return 1, ipList[ip]
    else:
        return 0,None

def get_connect_bykey(key):
    if key in connects:
        conp = connects[key].copy()
        conp['passwd'] = ''
        return key, conp
    else:
        return -1, {}

def del_connect(key):
    if key in connects:
        ip = connects[key]['ip']
        if ip in ipList:
            del ipList[ip]
        hd = connects[key]['hd']
        dll.Disconnect(hd)
        del connects[key]
        return 1, None
    else:
        return -1, None
    
def get_param_bykey(key,params: list):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        # items = b'DeviceID,Door1SensorType,Door1Drivertime,Door1Intertime'
        items = bytes(','.join(params), encoding="utf8")
        sBuf = create_string_buffer(8 * 1024)
        re = dll.GetDeviceParam(hd, sBuf, 1024, items)
        if re == 0:
            st = str(sBuf.value)[2:-1]
            return 1, st.split(',')
        else:
            return re, []
    else:
        return 0, []

def set_param_bykey(key, paramkvs: list):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        items = bytes(','.join(paramkvs), encoding="utf8")
        #items = b'DeviceID,Door1SensorType,Door1Drivertime,Door1Intertime'
        re = dll.SetDeviceParam(hd, items)
        if re == 0:
            return 1, None
        else:
            return re, None
    else:
        return 0, None


def control_device_bykey(key, OperationID, params: list, option=''):
    if len(params) < 4: return 0,'' 
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        sBuf = bytes(option, encoding="utf8")
        re = dll.ControlDevice(hd, OperationID, 
                               params[0], params[1], params[2], params[3], sBuf)
        if re == 0:
            return 1, None
        else:
            return -3, re
    else:
        return -4, None

def get_data_bykey(key, tableName, fieldNames=['*'], filters=[], options=''):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        sBuf = create_string_buffer(8 * 1024 * 1024)
        sTableName = bytes(tableName, encoding="utf8")
        sFieldNames = bytes('\t'.join(fieldNames), encoding="utf8")
        sFilters = bytes(','.join(filters), encoding="utf8")
        sOptions = bytes(options, encoding="utf8")
        re = dll.GetDeviceData(hd, sBuf, 8 * 1024 * 1024,
                                sTableName, sFieldNames, sFilters, sOptions)
        if re >= 0:
            st = str(sBuf.value)[2:-1]
            return re, st.split("\\r\\n")[0:-1]
        else:
            return -3, re
    else:
        return -4, None

def set_data_bykey(key, tableName, data, options=''):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        sTableName = bytes(tableName, encoding="utf8")
        st = '\r\n'.join(data).replace(',', '\t')
        sData = bytes(st, encoding="utf8")
        sOptions = bytes(options, encoding="utf8")
        re = dll.SetDeviceData(hd, sTableName, sData, sOptions)
        if re == 0:
            return 1, None
        else:
            return -3, re
    else:
        return -4, None

def del_data_bykey(key, tableName, filters=[], options=''):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        sTableName = bytes(tableName, encoding="utf8")
        sFilters = bytes(','.join(filters), encoding="utf8")
        sOptions = bytes(options, encoding="utf8")
        re = dll.DeleteDeviceData(hd, sTableName, sFilters, sOptions)
        if re >= 0:
            return 1, None
        else:
            return -3, re
    else:
        return -4, None


def get_user_bykey(key, userID):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        sBuf = create_string_buffer(512 * 1024)
        sTableName = bytes('user', encoding="utf8")
        sFieldNames = bytes('Pin\tCardNo\tPassword', encoding="utf8")
        sFilters = bytes('Pin={}'.format(userID), encoding="utf8")
        sOptions = bytes('', encoding="utf8")
        re = dll.GetDeviceData(hd, sBuf, 512 * 1024,
                               sTableName, sFieldNames, sFilters, sOptions)
        if re < 1: 
            return -3, re

        st = str(sBuf.value)[2:-1]
        va = st.split("\\r\\n")[1].split(',')
        user = User(va[0],'',va[2],int(va[1]))

        sBuf = create_string_buffer(128 * 1024)
        sTableName = bytes('userauthorize', encoding="utf8")
        sFieldNames = bytes('Pin\tAuthorizeTimezoneId\tAuthorizeDoorId', 
                                encoding="utf8")
        reAuthorize = dll.GetDeviceData(hd, sBuf, 128 * 1024,
                               sTableName, sFieldNames, sFilters, sOptions)
        if reAuthorize > 0:
            st = str(sBuf.value)[2:-1]
            va = st.split("\\r\\n")[1].split(',')
            vi = int(va[2])
            user.authorize = [(vi & 1) > 0, (vi & 2) > 0,
                              (vi & 4) > 0, (vi & 8) > 0]
        
        sBuf = create_string_buffer(1 * 1024 * 1024)
        sTableName = bytes('templatev10', encoding="utf8")
        sFieldNames = bytes('Pin\tSize\tFingerID\tValid\tTemplate',
                            encoding="utf8")
        reTemplate = dll.GetDeviceData(hd, sBuf, 1024 * 1024,
                                        sTableName, sFieldNames, sFilters, sOptions)
        if reTemplate > 0:
            st = str(sBuf.value)[2:-1]
            la = st.split("\\r\\n")[1:-1]
            user.finger = []
            for l in la:
                va = l.split(',')
                user.finger.append(UserFinger(int(va[2]), int(
                    va[1]), int(va[3]) == 3, va[4]))

        return 1, user
    else:
        return -4, None

def del_user_bykey(key, userID):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        errCount = 0

        sTableName = bytes('user', encoding="utf8")
        sFilters = bytes('Pin={}'.format(userID), encoding="utf8")
        sOptions = bytes('', encoding="utf8")
        re = dll.DeleteDeviceData(hd, sTableName, sFilters, sOptions)
        if re < 0: 
            return -3, re

        sTableName = bytes('userauthorize', encoding="utf8")
        reAuthorize = dll.DeleteDeviceData(hd, sTableName, sFilters, sOptions)
        if reAuthorize < 0:
            errCount += 1

        sTableName = bytes('templatev10', encoding="utf8")
        reTemplate = dll.DeleteDeviceData(hd, sTableName, sFilters, sOptions)
        if reTemplate < 0:
            errCount += 1

        return 1, errCount
    else:
        return -4, None


def set_user_bykey(key, user: User):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        errCount = 0

        sTableName = bytes('user', encoding="utf8")
        st = 'Pin={0}\tCardNo={1}\tPassword={2}'.format(
            user.id, user.card_no, user.passwd)
        sData = bytes(st, encoding="utf8")
        sOptions = bytes('', encoding="utf8")
        re = dll.SetDeviceData(hd, sTableName, sData, sOptions)
        if re < 0: 
            return -3, re

        if len(user.authorize) == 4:
            vi = 0
            if user.authorize[0]: 
                vi += 1
            if user.authorize[1]:
                vi += 2
            if user.authorize[2]:
                vi += 4
            if user.authorize[3]:
                vi += 8
            sTableName = bytes('userauthorize', encoding="utf8")
            st = 'Pin={0}\tAuthorizeTimezoneId={1}\tAuthorizeDoorId={2}'.format(
                user.id, 1, vi)
            sData = bytes(st, encoding="utf8")
            reAuthorize = dll.SetDeviceData(hd, sTableName, sData, sOptions)
            if reAuthorize < 0: 
                errCount += 1

        sTableName = bytes('templatev10', encoding="utf8")
        sFilters = bytes('Pin={}'.format(user.id), encoding="utf8")
        sOptions = bytes('', encoding="utf8")
        reTemplate = dll.DeleteDeviceData(hd, sTableName, sFilters, sOptions)
        if reTemplate < 0:
            errCount += 1
        if len(user.finger) >0:            
            for f in user.finger:
                st = 'Pin={0}\tSize={1}\tFingerID={2}\tTemplate={3}\tValid={4}'.format(
                    user.id, f.size, f.finger_id, f.template, 3 if f.valid else 1)
                sData = bytes(st, encoding="utf8")
                reTemplate = dll.SetDeviceData(hd, sTableName, sData, sOptions)
                if reTemplate < 0:
                    errCount += 1

        return 1, errCount
    else:
        return -4, None

def get_log_bykey(key):
    if key in connects:
        conp = connects[key]
        hd = conp['hd']
        sBuf = create_string_buffer(4 * 1024 * 1024)
        re = dll.GetRTLog(hd, sBuf, 4 * 1024 * 1024)
        if re >= 0:
            st = str(sBuf.value)[2:-1]
            return 1, st.split("\\r\\n")[0:-1]
        else:
            return -3, re
    else:
        return -4, None


def changeDatetime(sdt):
    now = datetime.now()
    if sdt != None:
        now = datetime.strptime(sdt, '%Y-%m-%d %H:%M:%S')
    vi = 0
    vi += (now.year - 2000) * 12 * 31
    vi += (now.month - 1) * 31
    vi += (now.day - 1)
    vi *= 24 * 60 * 60
    vi += now.hour * 60 * 60
    vi += now.minute * 60
    vi += now.second
    st = 'DateTime=' + str(vi)
    return [st]

        


