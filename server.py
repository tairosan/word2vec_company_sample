#!/bin/env python
# -*- coding: utf-8 -*-
# Created on 2015/05/24
# @author: tairosan
#

import os
import json
import tornado.ioloop
import tornado.web
import numpy
import urllib
import scipy
import gensim

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
    	print kwargs
    	# 前方の/v1/ を抜く
    	path = self.request.path[4:]
    	# decode
    	decoded = urllib.unquote(path)

    	# gensimのword2vecに用意したpklhァイルをmodelとしてを読み込む
        model = gensim.models.Word2Vec.load('****.pkl')

        # 判定結果を繰り返し処理で配列に入れる
        result = []
        for data in model.most_similar(positive=[unicode(decoded)]):
        	#result = u"{0},".format(data[0])
        	result.append(data[0])

        # jsonにdumpして書き出す	
        self.write(json.dumps(result))

application = tornado.web.Application([
    # (r"/v1/rel", MainHandler),
    (r'/(?P<version>\w+)/(?P<args>.+)', MainHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	# リクエスト処理の開始
	tornado.ioloop.IOLoop.instance().start()
