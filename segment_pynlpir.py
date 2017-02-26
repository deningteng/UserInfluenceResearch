#coding:utf-8
# import pynlpir
# pynlpir.open(encoding='utf-8')
# phase='NLPIR分词系统前身为2000年发布的ICTCLAS词法分析系统'
#
# result=pynlpir.segment(phase,pos_tagging=False)
#
# for x in result:
#     print result[0]
# pynlpir.close()



import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import pynlpir

pynlpir.open()
s = '因为我比较懒,所以我就只是修改了这句话,代码还是原博客的'
segments = pynlpir.segment(s)
for segment in segments:
    print segment[0], '\t', segment[1]

pynlpir.close()