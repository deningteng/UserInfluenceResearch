import sys
import re
import numpy as np
import pandas as pd
from documentRead import DocumentRead
'''
Find followers data for users who are covered in influence calculation
'''

directory ='F:\\Git Repository\\weibo'
documentReader=DocumentRead(directory)
documentReader.load_document()
documents_name=documentReader.get_documents_name()
newdata = []
df = pd.DataFrame(columns=['userid','followerid'])
for index in range(0,len(documents_name)):
    reader = pd.read_csv('F:\\Git Repository\\weibo\\'+documents_name[index],header=None)
    reader.columns=['userid','followerid']
    reader=reader.astype(object)
    # print reader
    df=df.append(reader,ignore_index=True)
# print df2
group=df.groupby(df['userid']).count()
print group
group.to_csv('followerNum.csv',encoding='utf-8')