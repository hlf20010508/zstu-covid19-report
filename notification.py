import json
import requests
import os

url = 'http://wxpusher.zjiecode.com/api/send/message'
# //内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
appToken = os.environ['WXPUSHER_APPTOKEN']
uid = os.environ['WXPUSHER_UID']

def notify(log):
    params = {
        "appToken": appToken,
        "content":"异常提醒：zstu-covid19-report申报失败。\n"+log,
        "contentType":1,
        "uids": [uid]
    }
    params = json.dumps(params)
    headers = {
        'Content-Type': "application/json",
    }

    html = requests.post(url, data=params, headers=headers)
    print(html.text)