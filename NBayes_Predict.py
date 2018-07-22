#coding=gbk
#!/usr/bin/env python



from sklearn.naive_bayes import MultinomialNB  # �������ʽ��Ҷ˹�㷨
from sklearn import metrics
from Tools import readbunchobj

# ����ѵ����
trainpath = "train_word_bag/tfdifspace.dat"
train_set = readbunchobj(trainpath)

# ������Լ�
testpath = "test_word_bag/testspace.dat"
test_set = readbunchobj(testpath)

# ѵ��������������ʴ������ͷ����ǩ��alpha:0.001 alphaԽС����������Խ�࣬����Խ��
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

# Ԥ�������
predicted = clf.predict(test_set.tdm)

for flabel, file_name, expct_cate in zip(test_set.label, test_set.filenames, predicted):
    if flabel != expct_cate:
        print(file_name, ": ʵ�����:", flabel, " -->Ԥ�����:", expct_cate)

print("Ԥ�����!!!")

# ������ྫ�ȣ�

def metrics_result(actual, predict):
    print('����:{0:.3f}'.format(metrics.precision_score(actual, predict, average='weighted')))
    print('�ٻ�:{0:0.3f}'.format(metrics.recall_score(actual, predict, average='weighted')))
    print('f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict, average='weighted')))


metrics_result(test_set.label, predicted)
