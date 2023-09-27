from utils.logFunc import recordLog
from utils.excleFunc import readExcle,writeExcle
from loguru import logger
from config import base_url
import pytest
import requests
from utils.common import replaceValue,extractValue,setGlobalValue,getGlobalValue


@pytest.mark.parametrize("caseData",readExcle("types"))
def test_01_types(caseData):
    try:
        testNumber = caseData["testNumber"]
        url = base_url + caseData["url"]
        method = caseData["method"]
        headers = replaceValue(caseData["headers"],getGlobalValue())
        data = replaceValue(caseData["data"],getGlobalValue())
        r = requests.request(method=method,url=url,headers=headers,json=data)
        writeExcle("types","L"+testNumber,r.text)
        
    except Exception as e:
        logger.exception(e)
        writeExcle("types","L"+testNumber,e)



# class TestDemo:
#     def test_02_demo(self):
#         assert 1==1
#     def test_03_demo(self):
#         assert 1==2

