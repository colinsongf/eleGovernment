#coding=gbk

import csv
from filter import filter
from threading import Thread
from Tool_s import Tools

def get_qa(path):
    T = Tools()
    name_list = T.read_file_or_dir(path)
    for txt_file in name_list:
        f = filter(txt_file)
        zt_word,title_list,__1_dict = f.analayis()
        f.get_qa(T,zt_word,title_list,__1_dict)

    # qa_data = []
    # headers = ["q",'a']
    # with open(path) as reader:
    #     content = reader.read()
    # raw_txt_list = content.replace("\t",'').replace(" ",'').split("\n")
    # for txt in raw_txt_list:
    #     qa = {}
    #     temp_list = txt.split("��")
    #     question = temp_list[0] + "��ʲô"
    #     answer = "".join(temp_list[1:])
    #     qa["q"] = question
    #     qa['a'] = answer
    #     qa_data.append(qa)
    # with open('qa.csv', 'w', newline='') as f:
    # # ��ͷ�����ﴫ�룬��Ϊ��һ������
    #     writer = csv.DictWriter(f, headers)
    #     writer.writeheader()
    #     for row in qa_data:
    #         writer.writerow(row)

    # # ������д�����
    # writer.writerows(datas)




if __name__ == "__main__":
    get_qa("demo")
