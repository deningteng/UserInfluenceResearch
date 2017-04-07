from documentRead import DocumentRead
import numpy as np
import matplotlib.pyplot as plt
'''
To show the followers count and reports count of users who are high influence in every community
'''
directory ='F:\\Git Repository\\InfluenceScore_result\\'
documentReader=DocumentRead(directory)
documentReader.load_document(key_word_list='InfluenceRank')
document_name=documentReader.get_documents_name()
user_list={}
for index in range(0,len(document_name)):
    user_list[index]=[]
    f=open(directory+document_name[index])
    line_num=0
    for line in f.readlines():
        line_num=line_num+1
        if (line_num>4)&(line_num<25):
            line=line.strip('\n')
            user_list[index].append(line.split(',')[0])

community_report_count={}
for index in range(0,len(document_name)):
    community_report_count[index]=0

community_follower_count={}
for index in range(0,len(document_name)):
    community_follower_count[index]=0

reports=open('reports.csv')
for line in reports.readlines():
    line=line.strip('\n')
    report_count=line.split(',')
    for index in range(0,len(user_list)):
        if report_count[0] in user_list[index]:
            community_report_count[index]=community_report_count[index]+int(report_count[1])

followers=open('followerNum.csv')
for line in followers.readlines():
    line = line.strip('\n')
    follower_count=line.split(',')
    for index in range(0, len(user_list)):
        if follower_count[0] in user_list[index]:
            community_follower_count[index]=community_follower_count[index]+int(follower_count[1])

print community_report_count
print community_follower_count
number=[5150.0,1681.0,1768.0,657.0,1749.0,9313.0,3609.0,1318.0,2686.0,1905.0,980.0,1652.0,799.0,2659.0,1693.0]

x1=community_report_count.keys()
y1= map(lambda (a,b):a/b, zip(community_report_count.values(),number))
print y1
x2=community_follower_count.keys()
y2=map(lambda (a,b):a/b, zip(community_follower_count.values(),number))
print y2
plt.plot(x1,y1,label="$multi$",color="red",linewidth=2)
plt.xlabel('community index')
plt.ylabel('report counts')
plt.title("Reports Count")

# plt.plot(x2,y2,label="$multi$",color="red",linewidth=2)
# plt.xlabel('community index')
# plt.ylabel('follower counts')
# plt.title("Follower Count")
plt.legend()
plt.show()


