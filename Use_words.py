#coding=gbk
import jieba
import os
from collections import Counter
#
# file_list = os.listdir('分类/')
content = ''
#
txt_list = os.listdir('分类/卫生医疗/')
for txt in txt_list:
    try:
        with open('分类/卫生医疗/'+txt,'r',encoding='utf-8') as reader:
            content = content + reader.read()
    except UnicodeDecodeError:
        with open('分类/卫生医疗/'+txt,'r',encoding='gbk') as reader:
            content = content + reader.read()
with open("stopword.txt",'r',encoding='utf-8') as a:
    words = a.read()
    word_list = words.split('\n')
    for word in word_list:
        if word in content:
            content = content.replace(word,'')
            with open('raw.txt','w',encoding='utf-8') as w:
                w.write(content)

with open('raw.txt','r',encoding='utf-8') as cuter:
    content = cuter.read()
    content = content.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    word_list = jieba.cut(content,cut_all=True)
    c = Counter()
    for i in word_list:
        if len(i)>1 and i != '\r\n':
            c[i] += 1
    print("词频结果：")
    for (k,v) in c.most_common(100):
        print('%s%s %s  %d' % ('  '*(5-len(k)), k, '*'*int(v/50), v))
