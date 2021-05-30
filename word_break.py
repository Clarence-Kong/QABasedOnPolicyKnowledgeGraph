#!/usr/bin/env python
# coding=utf-8
#
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')
import os
from pyltp import Segmentor, Postagger, Parser


class LtpLanguageAnalysis(object):
    def __init__(self, model_dir="/home/xxx/ltp-3.4.0/ltp_data/"):
        self.segmentor = Segmentor()
        self.segmentor.load(os.path.join(model_dir, "cws.model"))
        self.postagger = Postagger()
        self.postagger.load(os.path.join(model_dir, "pos.model"))
        self.parser = Parser()
        self.parser.load(os.path.join(model_dir, "parser.model"))

    def analyze(self, text):
        # 分词
        words = self.segmentor.segment(text)
        print()
        '\t'.join(words)

        # 词性标注
        postags = self.postagger.postag(words)
        print
        '\t'.join(postags)

        # 句法分析
        arcs = self.parser.parse(words, postags)
        print
        "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)

    def release_model(self):
        # 释放模型
        self.segmentor.release()
        self.postagger.release()
        self.parser.release()


if __name__ == '__main__':
    ltp = LtpLanguageAnalysis()
    ltp.analyze("无线电频率使用许可（遗失补办）")
    ltp.release_model()
