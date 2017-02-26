#coding:utf-8
import jieba
with open("H:\\user_content\\1427583973_content.txt") as f:
    text=f.read()

# import re
# pattern = re.compile()
# str = text
# print(pattern.search(str))
#
# import re
# print(re.sub())

seg_list = jieba.cut(text)  # 默认是精确模式
print text
print u'----------'
print(",".join(seg_list))