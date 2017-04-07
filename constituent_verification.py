'''
To filter user from two dimensions, message count and report count
To find four types user: the high and low are setted as higher than 90th and lower than 10th of all user in influence score
high message_count and high report_count
high message_count and low report_count
low message_count and high report_count
low message_count and low report_count
The propose is to compare influence calculation effectiveness of new algorithm with baselines on this four types' users.
We hope new algorithm will show great effectiveness on low message_count and low report_count type users
The evaluation index is follower_count of users, which is twitter's indication to recommdating
'''
from scipy import stats
from get_community_member import community_member
from documentRead import DocumentRead
def get_influence_score(list):
    directory = 'F:\\Git Repository\\InfluenceScore_result\\'
    documentReader = DocumentRead(directory)
    documentReader.load_document(key_word_list='InfluenceRank')
    document_name = documentReader.get_documents_name()
    user_list = {}
    for index in range(0,len(document_name)):
        f = open(directory + document_name[index])
        line_num = 0
        for line in f.readlines():
            line_num = line_num + 1
            if (line_num > 4):
                line = line.strip('\n')
                score=line.split(',')
                user_list[score[0]]=score[1]
    score_list=[]
    for id in list:
        if id in user_list.keys():
            score_list.append(user_list[id])
        else:
            score_list.append(0)
    return score_list

def get_followers_num(list):
    followers_num={}
    f=open('follower_num_1.csv')
    for line in f.readlines():
        line=line.strip('\n')
        user_follower=line.split(',')
        followers_num[user_follower[0]]=user_follower[1]
    follower_num_list=[]

    for item in list:
        if item in followers_num.keys():
            follower_num_list.append(followers_num[item])
        else:
            follower_num_list.append(0)
    return follower_num_list

if __name__ == '__main__':
    proportion=0.1
    community_member=community_member()
    f1=open('reports_count_1.csv')
    f2=open('message_count_1.csv')
    report_dic={}
    message_dic={}
    for line in f1.readlines():
        line=line.strip('\n')
        report=line.split(',')
        report_dic[report[0]]=int(report[1])
    community_member_report=community_member
    for index1 in range(0,len(community_member_report)):
        for index2 in range(0,len(community_member_report[index1])):
            id=community_member_report[index1].keys()[index2]
            if id in report_dic.keys():
                community_member_report[index1][id]=report_dic[id]
            else:
                community_member_report[index1][id]=0
    # print community_member_report.keys()

    for line in f2.readlines():
        line=line.strip('\n')
        message=line.split(',')
        message_dic[message[0]]=int(message[1])
    community_member_message=community_member
    for index1 in range(0,len(community_member_message)):
        for index2 in range(0,len(community_member_message[index1])):
            id=community_member_message[index1].keys()[index2]
            if id in message_dic.keys():
                community_member_message[index1][id]=message_dic[id]
            else:
                community_member_message[index1][id]=0
    # print community_member_message.keys()

    community_report_high_user={}
    community_report_low_user={}
    for index1 in range(0,len(community_member_report)):
        report_dic=community_member_report[index1]
        report_dic_sorted = sorted(report_dic.iteritems(), key=lambda asd: asd[1], reverse=False)
        report_count = len(report_dic_sorted)
        report_high = int(round(report_count * (1-proportion)))
        report_low = int(report_count * proportion)
        report_high_user = []
        report_low_user = []
        for index2 in range(report_high - 1, report_count):
            report_high_user.append(report_dic_sorted[index2][0])
        for index2 in range(0, report_low):
            report_low_user.append(report_dic_sorted[index2][0])
        community_report_high_user[index1]=report_high_user
        community_report_low_user[index1]=report_low_user
    # print community_report_high_user.keys()
    # print community_report_low_user.keys()

    community_message_high_user={}
    community_message_low_user = {}
    for index1 in range(0, len(community_member_message)):
        message_dic=community_member_message[index1]
        message_dic_sorted = sorted(message_dic.iteritems(), key=lambda asd: asd[1], reverse=False)
        message_count = len(message_dic_sorted)
        message_high = int(round(message_count * (1-proportion)))
        message_low = int(message_count * proportion)
        message_high_user = []
        message_low_user = []
        for index2 in range(message_high-1,message_count):
            message_high_user.append(message_dic_sorted[index2][0])
        for index2 in range(0,message_low):
            message_low_user.append(message_dic_sorted[index2][0])
        community_message_high_user[index1]=message_high_user
        community_message_low_user[index1]=message_low_user
    # print community_message_high_user.keys()
    # print community_message_low_user.keys()
    low_message_low_report_user={}
    for index in range(0,len(community_member)):
        low_message_low_report_user[index]=list(set(community_report_low_user[index])&set(community_message_low_user[index]))
        # print get_influence_score(low_message_low_report_user[index])[0:9]
        print stats.kendalltau(get_followers_num(low_message_low_report_user[index]),get_influence_score(low_message_low_report_user[index]))[0]
        # print len(low_message_low_report_user[index])
    # high_message_low_report_user={}
    # for index in range(0,len(community_member)):
    #     high_message_low_report_user[index]=list(set(community_report_low_user[index])&set(community_message_high_user[index]))
    #     print len(high_message_low_report_user[index])
    # low_message_high_report_user={}
    # for index in range(0,len(community_member)):
    #     low_message_high_report_user[index] = list(
    #         set(community_report_high_user[index]) & set(community_message_low_user[index]))
    #     print len(low_message_high_report_user[index])
    print '-------------------------------------------'
    high_message_high_report_user={}
    for index in range(0,len(community_member)):
        high_message_high_report_user[index] = list(set(community_report_high_user[index]) & set(community_message_high_user[index]))
        # print get_influence_score(high_message_high_report_user[index])[0:9]
        print stats.kendalltau(get_followers_num(high_message_high_report_user[index]),get_influence_score(high_message_high_report_user[index]))[0]
        # print len(high_message_high_report_user[index])





    # report_dic_sorted=sorted(report_dic.iteritems(),key=lambda asd:asd[1],reverse=False)
    # report_count=len(report_dic_sorted)
    # report_high=int(round(report_count*0.9))
    # report_low=int(report_count*0.1)
    # report_high_user=[]
    # report_low_user=[]
    # for index in range(report_high-1,report_count):
    #     report_high_user.append(report_dic_sorted[index][0])
    # for index in range(0,report_low):
    #     report_low_user.append(report_dic_sorted[index][0])


    # message_dic_sorted=sorted(message_dic.iteritems(),key=lambda asd:asd[1],reverse=False)
    # message_count=len(message_dic_sorted)
    # message_high=int(round(message_count*0.9))
    # message_low=int(message_count*0.1)
    # message_high_user=[]
    # message_low_user=[]
    # for index in range(message_high-1,message_count):
    #     message_high_user.append(message_dic_sorted[index][0])
    # for index in range(0,message_low):
    #     message_low_user.append(message_dic_sorted[index][0])

    # print report_high_user
    # print report_low_user
    # print message_high_user
    # print message_low_user

    # low_message_low_report_user=list(set(report_low_user)&set(message_low_user))
    # print len(low_message_low_report_user)
    # high_message_low_report_user=list(set(report_low_user)&set(message_high_user))
    # print len(high_message_low_report_user)
    # low_message_high_report_user=list(set(report_high_user)&set(message_low_user))
    # print len(low_message_high_report_user)
    # high_message_high_report_user=list(set(report_high_user)&set(message_high_user))
    # print len(high_message_high_report_user)
    #
    # print stats.kendalltau(get_followers_num(low_message_low_report_user),get_influence_score(low_message_low_report_user))[0]
    # print stats.kendalltau(get_followers_num(high_message_low_report_user), get_influence_score(high_message_low_report_user))[0]
    # print stats.kendalltau(get_followers_num(low_message_high_report_user),get_influence_score(low_message_high_report_user))[0]
    # print stats.kendalltau(get_followers_num(high_message_high_report_user),get_influence_score(high_message_high_report_user))[0]