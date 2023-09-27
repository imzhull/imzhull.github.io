import pytest
import time
from utils.common import initGlobalValue,getToken
from loguru import logger

token = getToken()

initGlobalValue({'extToken':token})  #全局变量初始化

now = time.strftime("%y-%m-%d-%H-%M-%S")
logger.add(f"./logs/debug-{now}.log")

args = ["-s","-v"]
pytest.main(args)