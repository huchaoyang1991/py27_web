"""
============================
Author:柠檬班-木森
Time:2020/4/25   9:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

#  通过cmd 启动chromedriver
# import os
#
# os.popen("chromedriver")
data = {
    "capabilities": {
        "browserName": "chrome",
    },
    'desiredCapabilities': {}
}
response = requests.post(url="http://localhost:9515/session", json=data)
sessionid = response.json()["sessionId"]
print("当前会话的sessionid：",sessionid)



# 让浏览器打开百度
data1 = {"url": "http://www.baidu.com"}

url = "http://localhost:9515/session/{}/url".format(sessionid)
requests.post(url=url, json=data1)
