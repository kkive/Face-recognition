# encoding:utf-8
import requests
import base64
import time
import pyautogui
import os
import cv2



def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


second = sleeptime(0, 0, 3)
while 1 == 1:
    time.sleep(second)

# start = time.perf_counter()

    def acc_token(a,b):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+a+'&client_secret='+b+''
        response = requests.get(host)
        if response:
            print(response.json())
    #a = acc_token("iVolkU5gvch2lLgpFIjMeAyx","iZbcKjfxGBAyGWVsGf793fLTM8EaSLhc")
    outaccess_token = "24.afe1d2a6b4086730983b7947bb544713.2592000.1628007607.282335-23578666"

    #拍照



    #image转base64
    filePath=".\\photo\\2.jpg"#照片路径
    f=open(filePath,"rb")
    data = base64.b64encode(f.read())#编码格式，技术文档要求
    f.close()
    image=str(data,'UTF-8')

    '''
    人脸搜索
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    params = {"image":image,"image_type":"BASE64",
              "group_id_list":"user_1,cj,001,1",
              "quality_control":"NONE","liveness_control":"NONE"}
    access_token = outaccess_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    # if response:
    #     print (response.json())

    responseout = response.json()
    if responseout["error_msg"] in "SUCCESS":
        score=responseout["result"]["user_list"][0]["score"]
        user_id=responseout["result"]["user_list"][0]["user_id"]
        if score>85:
            print(user_id,":识别成功")
            pyautogui.hotkey('win','d')#识别成功，使用热键回桌面
            os.startfile("D:\Program Files (x86)\Tencent\WeChat\WeChat.exe")#打开程序
            a = '1'
            with open(".\\result_log.txt",'w') as f:
                f.write(a)
            exit()
        else:
            print("人脸库无此人")
            a = 0
    else:
        print("error:",responseout["error_msg"])

    # end = time.perf_counter()
    # print((end-start))