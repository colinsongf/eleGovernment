#coding=gbk
import os
import re
from pyltp import SementicRoleLabeller
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import SentenceSplitter
from pyltp import Parser
class Tools:
    def __init__(self):
        path = 'ltp_data_v3.4.0'
        self.par_model_path = os.path.join(path, 'parser.model')
        self.cws_model_path = os.path.join(path, 'cws.model')
        self.pos_model_path = os.path.join(path, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        self.ner_model_path = os.path.join(path, 'ner.model')
        self.srl_model_path = os.path.join(path, 'pisrl_win.model')
        self.recognizer = NamedEntityRecognizer() # 初始化实例
        self.postagger = Postagger() # 初始化实例
        self.segmentor = Segmentor()  # 初始化实例
        self.labeller = SementicRoleLabeller() # 初始化实例
        self.parser = Parser() # 初始化实例
        self.parser.load(self.par_model_path)  # 加载模型
        self.labeller.load(self.srl_model_path)  # 加载模型
        self.recognizer.load(self.ner_model_path)  # 加载模型
        self.postagger.load(self.pos_model_path)  # 加载模型
        self.segmentor.load(self.cws_model_path)  # 加载模型

    def __del__(self):
        self.parser.release()
        self.labeller.release()
        # self.recognizer.release()
        self.postagger.release()
        self.segmentor.release()
    def read_file_or_dir(self,path):
        if os.path.exists(path):
            pass
        else:
            print("路径不存在!")
            os._exit()
        if os.path.isdir(path):
            file_list = os.listdir(path)
            file_path_list = [path + "/" + file_name for file_name in file_list]
            return file_path_list
        else:
            try:
                with open(path,encoding="utf-8") as rd:
                    content = rd.read()
            except UnicodeDecodeError:
                with open(path,encoding="gbk") as rd:
                    content = rd.read()
            return content

    def nltk(self,txt):#传入单句
        words = self.segmentor.segment(txt)
        postags = self.postagger.postag(words)
        arcs = self.parser.parse(words, postags)
        roles = self.labeller.label(words, postags, arcs)
        return list(words),list(postags),roles

    def deal_with_pos_str(self,pos_str):
        reg_pattern = "n+"
        reg_pattern_2 = "ncn"
        reg_pattern_9 = "an"
        reg_pattern_3 = "un"
        reg_pattern_4 = "v+"
        reg_pattern_5 = "rn"
        reg_pattern_8 = "vcv"
        reg_pattern_6 = "pbnv"
        reg_pattern_7 = "pnv"
        reg_pattern_10 = "av"

        pos_str = re.sub(reg_pattern,"n",pos_str)
        pos_str = re.sub(reg_pattern_2,"n",pos_str)
        pos_str = re.sub(reg_pattern_4,"v",pos_str)
        pos_str = re.sub(reg_pattern_5,"n",pos_str)
        pos_str = re.sub(reg_pattern_9,"n",pos_str)
        pos_str = re.sub(reg_pattern_3,"n",pos_str)
        pos_str = re.sub(reg_pattern_8,"v",pos_str)
        pos_str = re.sub(reg_pattern_6,"v",pos_str)
        pos_str = re.sub(reg_pattern_7,"v",pos_str)
        pos_str = re.sub(reg_pattern_10,"v",pos_str)
        return pos_str
