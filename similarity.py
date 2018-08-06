#coding=gbk
import jieba
from gensim import corpora,models,similarities


def similarity(answer_list,doc_test):
	all_doc = []
	all_doc.extend(answer_list)
	#���¶�Ŀ���ĵ����зִʣ����ұ������б�all_doc_list��
	all_doc_list = []
	for doc in all_doc:
	    doc_list = [word for word in jieba.cut(doc)]
	    all_doc_list.append(doc_list)

	doc_test_list = [word for word in jieba.cut(doc_test)]
	#������dictionary������ȡ�ʴ���bag-of-words)
	dictionary = corpora.Dictionary(all_doc_list)
	#�ʴ��������ֶ����дʽ����˱��
	dictionary.keys()

	# dictionary.token2id
	#����ʹ��doc2bow�������Ͽ�
	corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
	#�����ĵ�Ҳת��Ϊ��Ԫ�������
	doc_test_vec = dictionary.doc2bow(doc_test_list)
	#ʹ��TF-IDFģ�Ͷ����Ͽ⽨ģ
	tfidf = models.TfidfModel(corpus)
	tfidf[doc_test_vec]
	#��ÿ��Ŀ���ĵ������������ĵ������ƶ�
	index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
	sim = index[tfidf[doc_test_vec]]
	#�������ƶ�����
	a = sorted(enumerate(sim), key=lambda item: -item[1])

	return a[0][0:5]

similarity("")

