#coding:utf-8
import jieba
import sys
import re
from documentRead import DocumentRead

reload(sys)
sys.setdefaultencoding('utf8')

stopwords = open("H:\\stopwords.txt", 'rb').read().splitlines()

directory ='H:\\user_content'
documentReader=DocumentRead(directory)
documentReader.load_document()
documents=documentReader.get_documents()
documents_name=documentReader.get_documents_name()

for index in range(0, len(documents_name),1):
    str=unicode(documents[index])
    pattern2 = re.compile(u"-|/+|[u4e00-u9fa5]+|\s+|[.]|\#")
    pattern3 = re.compile(u"[A-Za-z]+")
    str = pattern2.sub("。", str)
    str = pattern3.sub("。", str)
    seg_list = jieba.cut(str, cut_all=False)  # 默认是精确模式

    stayed_line = ""
    for seg in seg_list:
        if seg.encode('utf-8') not in stopwords:
            stayed_line += seg + " "
    file_name = "H:\\user_seg_content\\"+"seg_"+documents_name[index]
    with open(file_name, "w") as f:
        f.write(stayed_line)

print u'done'


# with open("H:\\user_content\\1427592210_content.txt") as f:
#     text=f.read()
# import re
# str=unicode(text)
# # pattern1 = re.compile(u"(http.*?)[\u4e00-\u9fa5]+")
# pattern2 = re.compile(u"-|/+|[u4e00-u9fa5]+|\s+|[.]|\#")
# pattern3 = re.compile(u"[A-Za-z]+")
# # print str
# # str=pattern1.sub("",str)
# str=pattern2.sub("",str)
# str=pattern3.sub("",str)
# seg_list = jieba.cut(str)  # 默认是精确模式
# print u'----------'
#
# stayed_line = ""
# for seg in seg_list:
#     if seg.encode('utf-8') not in stopwords:
#         stayed_line += seg+" "
# file_name="H:\\seg_content.txt"
# with open(file_name,"w") as f:
#     f.write(stayed_line)
# print u'done'