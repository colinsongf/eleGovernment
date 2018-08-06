import jieba
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法
from sklearn.feature_extraction.text import TfidfVectorizer
from Tools import readfile, readbunchobj

def seg(content):
    content = content.replace('\r\n', '').strip()  # 删除换行
    content = content.replace(' ', '').strip()  # 删除空行、多余的空格
    content_seg = jieba.cut(content)  # 为文件内容分词
    content_seg = ' '.join(content_seg)
    return content_seg, content
def bunch_thing(target_name, contents):
	bunch = Bunch(target_name=[], contents=[])
	bunch.target_name.append(target_name)
	bunch.contents.append(contents)
	print(bunch)
	return bunch

def tf_idf(bunch):
	stpwrdlst = readfile("stopwords.txt").splitlines()
	tfidfspace = Bunch(target_name=bunch.target_name, tdm=[], vocabulary={})
	trainbunch = readbunchobj("train_word_bag/tfdifspace.dat")
	tfidfspace.vocabulary = trainbunch.vocabulary
	vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5, vocabulary=trainbunch.vocabulary)
	print(bunch.contents)
	tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
	return tfidfspace.tdm
def predict(what):
	trainpath = "train_word_bag/tfdifspace.dat"
	train_set = readbunchobj(trainpath)
	clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)
	predicted = clf.predict(what)
	print(predicted)

def main(txt):
	content_seg,content = seg(txt)
	bunch = bunch_thing(content, content_seg)
	what = tf_idf(bunch)
	predict(what)


main("你好沙雕")
