#coding=gbk
import jieba
from gensim import corpora,models,similarities


doc0 = "我不喜欢上海"
doc1 = "上海是一个好地方"
doc2 = "北京是一个好地方"
doc3 = "上海好吃的在哪里"
doc4 = "上海好玩的在哪里"
doc5 = "上海是好地方"
doc6 = "上海路和上海人"
doc7 = "喜欢小吃"
doc_test="我喜欢上海的小吃"   #测试文本

all_doc = []
all_doc.append(doc0)
all_doc.append(doc1)
all_doc.append(doc2)
all_doc.append(doc3)
all_doc.append(doc4)
all_doc.append(doc5)
all_doc.append(doc6)
all_doc.append(doc7)

#以下对目标文档进行分词，并且保存在列表all_doc_list中
all_doc_list = []
for doc in all_doc:
    doc_list = [word for word in jieba.cut(doc)]
    all_doc_list.append(doc_list)

doc_test_list = [word for word in jieba.cut(doc_test)]
#首先用dictionary方法获取词袋（bag-of-words)
dictionary = corpora.Dictionary(all_doc_list)
#词袋中用数字对所有词进行了编号
dictionary.keys()

# dictionary.token2id
#以下使用doc2bow制作语料库
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
#测试文档也转换为二元组的向量
doc_test_vec = dictionary.doc2bow(doc_test_list)
#使用TF-IDF模型对语料库建模
tfidf = models.TfidfModel(corpus)
tfidf[doc_test_vec]
#对每个目标文档，分析测试文档的相似度
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
sim = index[tfidf[doc_test_vec]]
#根据相似度排序
a = sorted(enumerate(sim), key=lambda item: -item[1])

print("和测试文本最相似的是:"+str(a[0][0]))
