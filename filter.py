import os
import re
'''
To filter the users who are not cover in influence calculation
follower_num_1.csv, message_count_1.csv, reports_count_1.csv are filterd file
'''
directory ='F:\\Git Repository\\user_seg_content\\'
name_list=os.listdir(directory)
userid=[]
for name in name_list:
    # print name
    search= re.match(r'seg_(.*?)_content',name,re.M|re.I)
    userid.append(search.group(1))
f1=open('reports.csv')
file_name='reports_count_1.csv'
with open(file_name, "w") as f:
    for line in f1.readlines():
        element = line.split(',')
        if element[0] in userid:
            f.write(element[0] + ',' + element[1])
