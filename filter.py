#coding=gbk
import os
import re
import sys
import csv

class filter:
    '�ı�������'
    __root_list = []
    __1_dict = {}
    content = ""
    __path = ""
    def __init__(self,path):
        ini_path = "filter.ini"  #�����ļ�
        self.__path = path
        if not os.path.exists(ini_path):
            print("�����ļ�ȱʧ!")
        if not os.path.exists(path):
            print("��Դ�ļ�ȱ��!")
        else:
            try:
                with open(path,encoding="utf-8") as rd:
                    self.content = rd.read()
            except UnicodeDecodeError:
                with open(path,encoding="gbk") as rd:
                    self.content = rd.read()
            try:
                with open(ini_path,encoding="utf-8") as rd_1:
                    self.reg_pattern = rd_1.read()
            except UnicodeDecodeError:
                with open(ini_path,encoding="gbk") as rd_1:
                    self.reg_pattern = rd_1.read()
    def analayis(self):
    #��һ��С���� reg_pattern
        temp_part = ""
        reg_pattern_2 = "����(.*?)ʵʩ���"
        reg_1 = re.compile(self.reg_pattern)
        reg_2 = re.compile(reg_pattern_2)
        title_list = reg_1.findall(self.content)
        if not len(reg_2.findall(self.__path)):
            return
        zt_word = reg_2.findall(self.__path)[0]

        # try:
        #     title_list = reg_1.findall(self.content)
        #     zt_word = reg_2.findall(self.__path)[0]
        # except:
        #     print(self.__path)
        #     print("����ʧ��!")
        #     sys.exit()
        if not len(title_list):
            sys.exit()
        for title in title_list:
            if title_list.index(title) == 0:
                part = self.content.split(title)[0]
                temp_part = part
                continue
            elif title_list.index(title) == len(title_list)-1:
                part = self.content.replace(self.content.split(title)[0],'')
                self.__1_dict[title_list.index(title)+1] = part
                part = self.content.split(title)[0].replace(temp_part,"")
                self.__1_dict[title_list.index(title)] = part
                # print(title_list.index(title)+1)
            else:
                part = self.content.split(title)[0].replace(temp_part,"")
                # print("title:"+title,"part:"+part,"temp_part:"+temp_part,"index:"+str(title_list.index(title)))
                self.__1_dict[title_list.index(title)] = part
            temp_part = self.content.split(title)[0]
        # print(self.__1_dict[4])
        return zt_word,title_list,self.__1_dict
        # str   list  dict
    def get_qa(self,T,zt_word,title_list,__1_dict):
        # f = open("qa_1.txt","a",encoding="utf-8")
        headers = ["q",'a']
        qa_data = []
        ff = open("qa_2.txt","a",encoding="utf-8")
        for i in range(len(title_list)-1):
            qa = {}
            # print(__1_dict[3])
            words,pos,roles = T.nltk(title_list[i].split("��")[1])
            # print(title_list[i].split("��")[1],file = ff)
            # for role in roles:
            #     print( role.index, "".join(["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]),file=ff)
            if len(roles) == 1 and len(roles[0].arguments) == 1 and roles[0].arguments[0].name == "A1":
                question =zt_word +"��"+ title_list[i].split("��")[1] + "?"
                answer = __1_dict[i+1]
                print("���⣺"+question+"\n"+"�𰸣�"+answer+"\n",file=ff)
                qa["q"] = question
                qa["a"] = answer
                qa_data.append(qa)


        # with open('qa.csv', 'w', newline='') as f:
        # # ��ͷ�����ﴫ�룬��Ϊ��һ������
        #     writer = csv.DictWriter(f, headers)
        #     writer.writeheader()
        #     for row in qa_data:
        #         writer.writerow(row)

# f = filter("eleGovernment/res/̫ԭ�������������ڼӿ콨��һ���������»��ص�ʵʩ���-̫ԭ����������.txt")#̫ԭ�����������칫�����ڹ᳹�����������ŵ�����������Ա��������취��ʵʩ���-̫ԭ����������
# zt_word,title_list,__1_dict = f.analayis()
# f.get_qa(zt_word,title_list,__1_dict)
