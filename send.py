import urllib
import requests
import time
import hashlib
import random
import json
randomnum = random.randint(0,99)
phone = #这里填手机号
sigstr = "appkey=这里填你的key&random=" + str(randomnum) + "&time=" + str(int(time.time()))+ "&mobile=" +str(phone)
hash = hashlib.sha256()
hash.update(sigstr.encode('utf-8'))

test_data = {
    "ext": "",
    "extend": "",
    "params": [
        "变量1",
        "变量2（不够自己加）"
    ],
    "sig": hash.hexdigest(),
    "sign": "签名",
    "tel": {
        "mobile": "手机号",
        "nationcode": "86"
    },
    "time": int(time.time()),
    "tpl_id": 模板ID
}
json_str = json.dumps(test_data)
requrl = "https://yun.tim.qq.com/v5/tlssmssvr/sendsms?sdkappid=这里改成自己的ID&random=" + str(randomnum)
r = requests.post(requrl, data=json_str)
print (r.text)
