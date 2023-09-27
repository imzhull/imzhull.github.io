import requests
from config import dingding_rebot_key
from loguru import logger

def dingding(content):
    # method = "post"
    # url = f"https://oapi.dingtalk.com/robot/send?access_token={dingding_rebot_key}"
    # data = {
    #     "msgtype":"text",
    #     "text":{"content",content}
    # }

    # r = requests.request(method=method,url=url,json=data)
    # logger.info(r.text)
    method = "post"
    url = f"https://oapi.dingtalk.com/robot/send?access_token={dingding_rebot_key}"
    data = {
        "msgtype": "text",
        "text": {"content":content}
    }
    r = requests.request(method=method,url=url,json=data)
    logger.info(r.text)

