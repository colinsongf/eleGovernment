#!/usr/bin/env python
#coding=gbk

import os
import pickle

from sklearn.datasets.base import Bunch
from Tools import readfile


def corpus2Bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)  # ��ȡseg_path�µ�������Ŀ¼��Ҳ���Ƿ�����Ϣ
    # ����һ��Bunchʵ��
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    '''
    extend(addlist)��python list�еĺ�������˼�����µ�list��addlist��ȥ����
    ԭ����list
    '''
    # ��ȡÿ��Ŀ¼�����е��ļ�
    for mydir in catelist:
        class_path = seg_path + mydir + "/"  # ƴ��������Ŀ¼��·��
        file_list = os.listdir(class_path)  # ��ȡclass_path�µ������ļ�
        for file_path in file_list:  # �������Ŀ¼���ļ�
            fullname = class_path + file_path  # ƴ���ļ���ȫ·��
            bunch.label.append(mydir)
            bunch.filenames.append(fullname)
            bunch.contents.append(readfile(fullname))  # ��ȡ�ļ�����
            '''append(element)��python list�еĺ�������˼����ԭ����list�����element��ע����extend()����������'''
    # ��bunch�洢��wordbag_path·����
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("�����ı��������������")


if __name__ == "__main__":
    # ��ѵ��������Bunch��������
    wordbag_path = "train_word_bag/train_set.dat"  # Bunch�洢·��
    seg_path = "����2/"  # �ִʺ�������Ͽ�·��
    corpus2Bunch(wordbag_path, seg_path)

    # �Բ��Լ�����Bunch��������
    wordbag_path = "test_word_bag/test_set.dat"  # Bunch�洢·��
    seg_path = "����2/"  # �ִʺ�������Ͽ�·��
    corpus2Bunch(wordbag_path, seg_path)
