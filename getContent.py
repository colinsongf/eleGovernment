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
    """ 从代理网站上获取代理"""
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
    """构建格式化的单个proxies"""
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
        # 信息索引号012187001/2018-00052发布时间2018-02-28发布机构市政府办公厅文号并政发〔2018〕4号主题词其他体裁通知
        reg = "信息索引号(.*?)发布时间(.*?)发布机构(.*?)文号(.*?)主题词(.*?)体裁(.*)"
        reg_pattern = re.compile(reg)
        t_list = reg_pattern.findall(txt)
        # print("名称："+title.text+'\n')
        # print('信息索引号:'+t_list[0][0]+'\n')
        # print('发布时间:'+t_list[0][1]+'\n')
        # print('发布机构:'+t_list[0][2]+'\n')
        # print('文号:'+t_list[0][3]+'\n')
        # print('主题词:'+t_list[0][4]+'\n')
        # print('体裁:'+t_list[0][5]+'\n')
        # print(div.text)
        content = "名称："+title.text+'\n'+'信息索引号:'+t_list[0][0]+'\n'+'发布时间:'+t_list[0][1]+'\n'+'发布机构:'+t_list[0][2]+'\n'+'文号:'+t_list[0][3]+'\n'+'主题词:'+t_list[0][4]+'\n'+'体裁:'+t_list[0][5]+'\n'+"内容:"+div.text
        # print(content)
        with open('res/'+title.text+'.txt','w',encoding="gbk") as txter:
            txter.write(content.encode('gbk','ignore').decode('gbk','ignore'))
            print('文件写入成功')
    except:
        print("文件写入失败")
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
