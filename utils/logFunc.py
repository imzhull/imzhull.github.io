# -*- coding: utf-8 -*-
'''
@文件    :logFunc.py
@说明    :封装的记录日志的方法
@时间    :2023/05/12 21:32:35
@作者    :浪晋
@版本    :1.0
'''

from loguru import logger


def recordLog(url=None,method=None,headers=None,data=None,status=None,text=None):
    """
    @功能    :记录调用接口的日志
    @参数    :
    @返回值  :
    @时间    :2023/05/12 21:33:14
    @作者    :浪晋
    @版本    :1.0
    """
    logger.info(f"请求地址：{url}")
    logger.info(f"请求类型：{method}")
    logger.info(f"请 求 头：{headers}")
    logger.info(f"请求数据：{data}")
    logger.info(f"状 态 码：{status}")
    if status == 200:
        logger.info(f"响应数据：{text}")
    else:
        logger.error(f"响应数据：{text}")