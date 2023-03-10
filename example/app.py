import asyncio
import json
import logging
import time

from pyxxl import ExecutorConfig, PyxxlRunner
from pyxxl.ctx import g
from pyxxl.utils import setup_logging


setup_logging(logging.DEBUG)

config = ExecutorConfig(
    xxl_admin_baseurl="http://localhost:8080/xxl-job-admin/api/",
    executor_app_name="xxl-job-python-executor-sample",
    executor_host="127.0.0.1",
)

app = PyxxlRunner(config)


@app.handler.register(name="demoJobHandler")
async def _test_task():
    # you can get task params with "g"
    print("get executor params: %s" % g.xxl_run_data.executorParams)
    await asyncio.sleep(5)
    return "成功..."


@app.handler.register(name="test_task3")
async def _test_task3():
    await asyncio.sleep(3)
    return "成功3"


@app.handler.register(name="test_task4")
def _test_task4():
    time.sleep(3)
    return "成功3"

jobInfo = {
    'appname':'xxl-job-python-executor-sample',
    'jobDesc':'测试任务111122221',
    'author':'龚伟2233333222a',
    'alarmEmail':'1325075688@qq.com',
    'scheduleType':'CRON',
    'scheduleConf':'1-2 * 3,4,18,23 * * ?',
    'cronGen_display':'1-2 * * * * ?',
    'schedule_conf_CRON':'',
    'schedule_conf_FIX_RATE':'',
    'schedule_conf_FIX_DELAY':'',
    'glueType':'BEAN',
    'executorHandler':'demoJobHandler',
    'executorParam':'123',
    'executorRouteStrategy':'FIRST',
    'childJobId':'',
    'misfireStrategy':'DO_NOTHING',
    'executorBlockStrategy':'SERIAL_EXECUTION',
    'executorTimeout':0,
    'executorFailRetryCount':0,
    'glueRemark':'GLUE代码初始化',
    'glueSource':''
}

import requests
url = 'http://127.0.0.1:8080/xxl-job-admin/jobinfo/add_by_inner'
res = requests.post(url=url, data=jobInfo)
print(res)


# app.run_executor()
