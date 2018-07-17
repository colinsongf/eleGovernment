#coding=gbk
# "http://sousuo.gov.cn/list.htm?q=&n=17&p=25&t=paper&sort=pubtime&childtype=&subchildtype=&pcodeJiguan=&pcodeYear=&pcodeNum=&location=&searchfield=&title=&content=&pcode=&puborg=&timetype=timeqb&mintime=&maxtime="
from urllib import request as rq
import re
import urllib
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


url_List = []
# http://www.taiyuan.gov.cn/intertidwebapp/govChanInfo/getDocuments?pageIndex=5&pageSize=20&siteId=1&ChannelType=1&KeyWord=&KeyWordType=&chanId=11&id=&typeId=&order=1
def get_ip_list(url, headers):
    """ �Ӵ�����վ�ϻ�ȡ����"""
    ip_list = []
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    ul_list = soup.find_all('tr', limit=70)
    print(len(ul_list))
    for i in range(2, len(ul_list)):
        line = ul_list[i].find_all('td')
        ip = line[1].text
        port = line[2].text
        address = ip + ':' + port
        ip_list.append(address)
    return ip_list


def get_proxy(aip):
    """������ʽ���ĵ���proxies"""
    proxy_ip = 'http://' + aip
    proxy_ips = 'https://' + aip
    proxy = {'http': proxy_ip, 'https': proxy_ips}
    print(proxy)
    return proxy
#111.155.116.221:8123   {'http':"http://111.155.116.221:8123" , 'https':"https://111.155.116.221:8123"}

def getContent(i):
    url = "http://www.taiyuan.gov.cn/intertidwebapp/govChanInfo/getDocuments?pageIndex="+str(i)+"&pageSize=20&siteId=1&ChannelType=1&KeyWord=&KeyWordType=&chanId=11&id=&typeId=&order=1"
    try:
        r = requests.get(url,headers=headers,timeout=20)
        time.sleep(random.random()*3)
        # url_List.append(r.json()["url"])
        for url_dict in r.json()['list']:
            url_List.append(url_dict['url'])
            print(url_dict["url"])
            with open('url.txt','a') as txt:
                txt.write("http://www.taiyuan.gov.cn"+url_dict['url']+"\n")
    except:
        pass


def get_file(url):
    try:
        r = requests.get(url,headers=headers,timeout=20)
        time.sleep(random.random()*3)
        html = r.content
        soup = BeautifulSoup(html,'html5lib')
        title = soup.find('title')
        table = soup.find('table','tb001')
        div = soup.find(id='zoom')
        txt = table.text.replace(" ",'').replace('\n','').replace('\r','').replace('\t','')
        # ��Ϣ������012187001/2018-00052����ʱ��2018-02-28���������������칫���ĺŲ�������2018��4��������������֪ͨ
        reg = "��Ϣ������(.*?)����ʱ��(.*?)��������(.*?)�ĺ�(.*?)�����(.*?)���(.*)"
        reg_pattern = re.compile(reg)
        t_list = reg_pattern.findall(txt)
        # print("���ƣ�"+title.text+'\n')
        # print('��Ϣ������:'+t_list[0][0]+'\n')
        # print('����ʱ��:'+t_list[0][1]+'\n')
        # print('��������:'+t_list[0][2]+'\n')
        # print('�ĺ�:'+t_list[0][3]+'\n')
        # print('�����:'+t_list[0][4]+'\n')
        # print('���:'+t_list[0][5]+'\n')
        # print(div.text)
        content = "���ƣ�"+title.text+'\n'+'��Ϣ������:'+t_list[0][0]+'\n'+'����ʱ��:'+t_list[0][1]+'\n'+'��������:'+t_list[0][2]+'\n'+'�ĺ�:'+t_list[0][3]+'\n'+'�����:'+t_list[0][4]+'\n'+'���:'+t_list[0][5]+'\n'+"����:"+div.text
        # print(content)
        with open('res/'+title.text+'.txt','w',encoding="gbk") as txter:
            txter.write(content.encode('gbk','ignore').decode('gbk','ignore'))
            print('�ļ�д��ɹ�')
    except:
        print("�ļ�д��ʧ��")
        pass
# for i in range(70):
#     getContent(i+1)
with open('url.txt','r') as reader:
    url_raw = reader.read()
    url_list = url_raw.split('\n')
for i in url_list:
     get_file(i)
# get_file("http://www.taiyuan.gov.cn/doc/2018/02/28/216430.shtml")






    # req = rq.Request(url,headers=headers2)
    # with  rq.urlopen(req) as getter:
    #     html = getter.read()
    #     json = json.dumps(html)
    #     print(json)

        # soup = BeautifulSoup(html,'html5lib')
        # td_list = soup.findAll(attrs={"class": "info"})
        # for td in td_list:
        #     url_List.append(td.contents[0]["href"])
        # print(url_List)


            # url_List.append(a['href'])
            # print(a['href'])
# dl_list = get_ip_list('http://www.xicidaili.com/wt',headers)
# print(dl_list)
# for i in range(70):
#     dl_list = get_ip_list("http://www.xicidaili.com/nn/5",headers)
#     for i  in dl_list:
#         proxys = get_proxy(i)
#         try:
#             getContent(i,proxys)
#         except:
#             continue

#     try:
#         t = Thread(target=getContent,args=(i,))
#         t.start()
#
#     except:
#         pass
