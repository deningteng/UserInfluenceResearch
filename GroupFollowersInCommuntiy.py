#coding:utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

dir1='F:\\Git Repository\\weibo'
file_name_list1 = os.listdir(dir1)
followers=[]
for name in file_name_list1:
    path=dir1+'\\'+name
    file = open(path)
    lines = file.readlines()
    for index in range(0, len(lines),1):
        item=lines[index].strip('\n').split(',')
        if len(item)==2:
            followers.append(item)
# print followers
# for follower in followers:
#     print follower[0],follower[1]
#     print '\n'
dir2='F:\\Git Repository\\communityNumbers'

file_name_list2= os.listdir(dir2)
community={}
for index1 in range(0, len(file_name_list2),1):
    path = dir2 + '\\' + file_name_list2[index1]
    file = open(path)
    lines = file.readlines()
    number=[]
    for id in lines:
        number.append(id.strip('\n'))
    community[index1]=number
# print community

groupFollowers={}
for index in range(0,len(community),1):
    group=[]
    groupFollowers[index]=group
for follower in followers:
    for index2 in range(0,len(community),1):
        if (follower[0] in community[index2])&(follower[1] in community[index2]):
            groupFollowers[index2].append(follower)

for index in range(0,len(groupFollowers),1):
    file_name='F:\\Git Repository\\groupFollowersByCommunity\\followersInCommunity%d.csv'%(index)
    with open(file_name, "w") as f:
        for follower in groupFollowers[index]:
            f.write(follower[0]+','+follower[1]+'\n')
    print 'file%d done'%(index)