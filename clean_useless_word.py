import re
import sys
from documentRead import DocumentRead

reload(sys)
sys.setdefaultencoding('utf8')
'''
To filter the words in stopwords list
'''
stopwords = open("F:\\Git Repository\\stopwords.txt", 'rb').read().splitlines()

directory ='F:\\Git Repository\\user_seg_content'
documentReader=DocumentRead(directory)
documentReader.load_document()
documents=documentReader.get_documents()
documents_name=documentReader.get_documents_name()

temp=0
for index in range(0, len(documents_name),1):
    temp=temp+1
    str=documents[index]
    word_list=str.replace('\n','').split(' ')
    lines=""
    for word in word_list:
        if word not in stopwords:
            lines+=word+" "
    file_name = "F:\\Git Repository\\user_reseg_content\\" + documents_name[index]
    with open(file_name, "w") as f:
        f.write(lines)
    print 'file %d done'%(temp)

print 'done'

