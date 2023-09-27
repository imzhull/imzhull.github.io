import requests
from config import base_url,account_info
from jsonpath import jsonpath


def getToken():
    """
    获取token
    """
    url = base_url + "/api/v1/e100/account/login/"
    method = "post"
    data = account_info
    r = requests.request(method=method,url=url,json=data)
    token = r.json()["data"]["token"]
    return token


def initGlobalValue(value=None):
    """
    初始化全局变量
    """
    global globalValue  #定义全局变量
    globalValue = {}
    if value not in (None,{}):
        globalValue.update(value)

def setGlobalValue(value:dict):
    """
    修改全局变量
    """
    globalValue.update(value)

def getGlobalValue(key=None):
    """
    获取全局变量
    """
    if key not in (None,{}):
        return globalValue.get(key)
    return globalValue

def replaceValue(text,globalValue):
    """
    替换数据
    """
    if text in (None,""):
        return text
    for k,v in globalValue.items():
        text = text.replace(k,str(v))
    try:
        data = eval(text)
    except:
        data = text
    return data

def extractValue(obj,path):
    """
    提取接口返回的指定数据
    """
    value = jsonpath(obj,path)[0]
    return value
    
