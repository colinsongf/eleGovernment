#coding=gbk
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import jieba

from Tools import savefile, readfile


def corpus_segment(corpus_path, seg_path):
    '''
    corpus_path��δ�ִ����Ͽ�·��
    seg_path�Ƿִʺ����Ͽ�洢·��
    '''
    catelist = os.listdir(corpus_path)  # ��ȡcorpus_path�µ�������Ŀ¼
    '''
    ������Ŀ¼�����־�������������磺
    train_corpus/art/21.txt�У�'train_corpus/'��corpus_path��'art'��catelist�е�һ����Ա
    '''
    print("������ִ���...")
    # ��ȡÿ��Ŀ¼����������е��ļ�
    for mydir in catelist:
        '''
        ����mydir����train_corpus/art/21.txt�е�art����catelist�е�һ�����
        '''
        class_path = corpus_path + mydir + "/"  # ƴ��������Ŀ¼��·���磺train_corpus/art/
        seg_dir = seg_path + mydir + "/"  # ƴ���ִʺ�����Ķ�ӦĿ¼·���磺train_corpus_seg/art/

        if not os.path.exists(seg_dir):  # �Ƿ���ڷִ�Ŀ¼�����û���򴴽���Ŀ¼
            os.makedirs(seg_dir)

        file_list = os.listdir(class_path)  # ��ȡδ�ִ����Ͽ���ĳһ����е������ı�
        '''
        train_corpus/art/�е�
        21.txt,
        22.txt,
        23.txt
        ...
        file_list=['21.txt','22.txt',...]
        '''
        for file_path in file_list:  # �������Ŀ¼�µ������ļ�
            fullname = class_path + file_path  # ƴ���ļ���ȫ·���磺train_corpus/art/21.txt
            content = readfile(fullname)  # ��ȡ�ļ�����
            '''��ʱ��content�����������ԭ�ı��������ַ����������Ŀո񡢿��С��س��ȵȣ�
            ��������������Ҫ����Щ�޹�ʹ�����ַ�ͳͳȥ�������ֻ�б�����������Ľ��յ��ı�����
            '''
            content = content.replace('\r\n'.encode('utf-8'), ''.encode('utf-8')).strip()  # ɾ������
            content = content.replace(' '.encode('utf-8'), ''.encode('utf-8')).strip()  # ɾ�����С�����Ŀո�
            content_seg = jieba.cut(content)  # Ϊ�ļ����ݷִ�
            savefile(seg_dir + file_path, ' '.join(content_seg).encode('utf-8'))  # ���������ļ����浽�ִʺ�����Ŀ¼

    print("�������Ϸִʽ���������")


if __name__ == "__main__":
    # ��ѵ�������зִ�
    corpus_path = "����/"  # δ�ִʷ������Ͽ�·��
    seg_path = "����2/"  # �ִʺ�������Ͽ�·��
    corpus_segment(corpus_path, seg_path)

    # �Բ��Լ����зִ�
    corpus_path = "����/"  # δ�ִʷ������Ͽ�·��
    seg_path = "����2/"  # �ִʺ�������Ͽ�·��
    corpus_segment(corpus_path, seg_path)
