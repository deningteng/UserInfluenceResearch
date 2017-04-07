#coding:utf-8
import sys
import os
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')

dir1='F:\\Git Repository\\groupFollowersByCommunity'
file_name_list1 = os.listdir(dir1)
index=0
for name in file_name_list1:
    index=index+1
    path=dir1+'\\'+name
    df=pd.read_csv(path)
    df.columns =['id','followerid']
    group=df.groupby(df['id']).count()
    group.to_csv('F:\\Git Repository\\followerNumberInCommunity\\followersCountCommunity%d.csv'%(index), encoding='utf-8',header=None)