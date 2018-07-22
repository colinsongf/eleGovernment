#coding=gbk
import os
import re
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import lxml
import json
from threading import Thread
import time
import random
ua = UserAgent()
headers = {
    'User-Agent':ua.random
}
# index_url = "http://www.hlj.gov.cn/gkml/ztfl.html?p=1&c=26"    pattern
#http://gkml.dbw.cn/gkml/web/data/ztfl.ashx?s=2492&p=1&c=17     pattern

def init_class_dict(name):
    if os.path.exists(name+'/'):
        pass
    else:
        os.makedirs(name+'/')


def get_url():
    class_list = [5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    for j in class_list:
        r = requests.get("http://gkml.dbw.cn/gkml/web/data/ztfl.ashx?s=1&p=1&c="+str(j),timeout=20,headers=headers)
        # raw_json = r.text.replace('var commentJsonVarStr___=','')
        reg = re.compile('"count":"(.*?)"')
        count = reg.findall(r.text)[0]
        s = requests.get("http://gkml.dbw.cn/gkml/web/data/ztfl.ashx?s="+str(count)+"&p=1&c="+str(j),timeout=20,headers=headers)
        time.sleep(random.random()*3)
        raw_text = s.text
        reg2 = re.compile('"title":"(.*?)","url":"(.*?)"')
        d_list = reg2.findall(raw_text)
        reg3 = re.compile('"name":"(.*?)"')
        res_list = reg3.findall(raw_text)
        for j in res_list:
            # print(j)
            t = Thread(target=init_class_dict,args=(j,))
            t.start()
        # for i in d_list:
        #     title = i[0]
        #     url = i[1]






get_url()
