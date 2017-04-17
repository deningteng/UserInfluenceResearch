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

def get_influence_list(directory):
    # directory = 'F:\\Git Repository\\InfluenceScore_result\\'
    documentReader = DocumentRead(directory)
    documentReader.load_document(key_word_list='InfluenceRank')
    document_name = documentReader.get_documents_name()
    user_influence_list = {}
    for index in range(0,len(document_name)):
        f = open(directory + document_name[index])
        line_num = 0
        for line in f.readlines():
            line_num = line_num + 1
            if (line_num > 4):
                line = line.strip('\n')
                score=line.split(',')
                user_influence_list[score[0]]=score[1]
    return user_influence_list

def get_followers_list():
    followers_num = {}
    f = open('followerNum.csv')
    for line in f.readlines():
        line = line.strip('\n')
        user_follower = line.split(',')
        followers_num[user_follower[0]] = user_follower[1]
    return followers_num
def fmap(a,b):
    return (a,b)
# def get_influence_rank(list,user_influence_list):
#     user_influence = {}
#     rank=[]
#     for item in list:
#         if item in user_influence_list.keys():
#             user_influence[item] = float(user_influence_list[item])
#         else:
#             user_influence[item] = 0.0
#     list_sorted = sorted(user_influence.iteritems(), key=lambda asd: asd[1], reverse=True)
#     for item in list:
#         for index in range(0,len(list_sorted)):
#             if item==list_sorted[index][0]:
#                 rank.append(int(index))
#     return rank

def get_influence_scores(list,user_influence_list):
    scores=[]
    for item in list:
        if item in user_influence_list.keys():
             scores.append(float(user_influence_list[item]))
        else:
            scores.append(0.0)
    return scores

# def get_followers_num_rank(list,user_follower_num):
#     user_follower={}
#     rank=[]
#     for item in list:
#         if item in user_follower_num.keys():
#             user_follower[item]=float(user_follower_num[item])
#         else:
#             user_follower[item]=0.0
#     list_sorted = sorted(user_follower.iteritems(), key=lambda asd: asd[1], reverse=True)
#     for item in list:
#         for index in range(0, len(list_sorted)):
#             if item==list_sorted[index][0]:
#                 rank.append(int(index))
#     return rank

def get_report_radio(list,report_radio_list):
    report_radio=[]
    for item in list:
        if item in report_radio_list.keys():
            report_radio.append(float(report_radio_list[item]))
        else:
            report_radio.append(0.0)
    return report_radio

def get_message_num(list,message_dic):
    message_num_list=[]
    for item in list:
        if item in message_dic.keys():
            message_num_list.append(float(message_dic[item]))
        else:
            message_num_list.append(0.0)
    return message_num_list

def get_report_num(list,report_dic):
    report_num_list=[]
    for item in list:
        if item in report_dic.keys():
            report_num_list.append(report_dic[item])
        else:
            report_num_list.append(0.0)
    return report_num_list

def get_followers_num(list,followers_num):
    follower_num_list=[]
    for item in list:
        if item in followers_num.keys():
            follower_num_list.append(float(followers_num[item]))
        else:
            follower_num_list.append(0.0)
    return follower_num_list

if __name__ == '__main__':
    proportion=0.1
    directory="C:\\dening\\InterestCommunityAcquisition\\result_standard\\"
    user_influence_list = get_influence_list(directory)
    user_follower_num=get_followers_list()
    community_member=community_member("C:\\dening\\InterestCommunityAcquisition\\result_standard\\")
    report_dic = {}
    message_dic = {}
    with open('reports.csv', "r") as f1:
        for line in f1.readlines():
            line=line.strip('\n')
            report=line.split(',')
            report_dic[report[0]]=float(report[1])
    with open('message_count.csv', "r") as f2:
        for line in f2.readlines():
            line=line.strip('\n')
            message=line.split(',')
            message_dic[message[0]]=float(message[1])
    community_member_report=community_member
    for index1 in range(0,len(community_member_report)):
        for index2 in range(0,len(community_member_report[index1])):
            id=community_member_report[index1].keys()[index2]
            if id in report_dic.keys():
                community_member_report[index1][id]=report_dic[id]
            else:
                community_member_report[index1][id]=0.0
    # print community_member_report.keys()


    community_member_message=community_member
    for index1 in range(0,len(community_member_message)):
        for index2 in range(0,len(community_member_message[index1])):
            id=community_member_message[index1].keys()[index2]
            if id in message_dic.keys():
                community_member_message[index1][id]=message_dic[id]
            else:
                community_member_message[index1][id]=0.0
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

    community_followers_high_user={}
    community_followers_low_user = {}
    community_member_follows=community_member

    for index1 in range(0,len(community_member_follows)):
        for index2 in range(0,len(community_member_follows[index1])):
            id=community_member_follows[index1].keys()[index2]
            if id in user_follower_num.keys():
                community_member_follows[index1][id]=user_follower_num[id]
            else:
                community_member_follows[index1][id]=0

    for index1 in range(0, len(community_member_follows)):
        followers_dic = community_member_follows[index1]
        followers_dic_sorted = sorted(followers_dic.iteritems(), key=lambda asd: asd[1], reverse=False)
        followers_count = len(followers_dic_sorted)
        followers_high = int(round(followers_count * (1 - proportion)))
        followers_low = int(followers_count * proportion)
        followers_high_user = []
        followers_low_user = []
        for index2 in range(followers_high - 1, followers_count):
            followers_high_user.append(followers_dic_sorted[index2][0])
        for index2 in range(0, followers_low):
            followers_low_user.append(followers_dic_sorted[index2][0])
        community_followers_high_user[index1] = followers_high_user
        community_followers_low_user[index1] = followers_low_user

    # for index in range(0, len(community_member)):
    #     print len(list(set(community_report_low_user[index]) & set(community_message_low_user[index])&set(community_followers_high_user)))
    print 'message_count-follower_num_count'
    sum=0.0
    for index in range(0,len(community_member)):
        correlation = stats.kendalltau(community_member_message[index].values(), get_followers_num(community_member_message[index].keys(),user_follower_num))[0]
        print correlation
        sum=sum+correlation
    print 'average correlation:%f'%(sum/len(community_member))
    print '-------------------'
    print 'report_count-follower_num_count'
    sum=0.0
    for index in range(0,len(community_member)):
        correlation=stats.kendalltau(community_member_report[index].values(), get_followers_num(community_member_report[index].keys(),user_follower_num))[0]
        print correlation
        sum=sum+correlation
    print 'average correlation:%f'%(sum/len(community_member))

    low_message_low_report_user={}
    print 'low message low report:influence_followers_num_count'
    sum = 0.0
    for index in range(0,len(community_member)):
        low_message_low_report_user[index]=list(set(community_report_low_user[index])&set(community_message_low_user[index]))
        scores=get_influence_scores(low_message_low_report_user[index],user_influence_list)
        followers_num=get_followers_num(low_message_low_report_user[index],user_follower_num)
        correlation= stats.kendalltau(scores,followers_num)[0]
        sum=sum+correlation
        print correlation
    print 'average correlation:%f'%(sum/len(community_member))
        # print len(low_message_low_report_user[index])

    print '--------------------'
    print 'high message high report:influence score_followers_num_count'
    high_message_high_report_user={}
    sum = 0.0
    for index in range(0,len(community_member)):
        high_message_high_report_user[index] = list(set(community_report_high_user[index]) & set(community_message_high_user[index]))
        correlation=stats.kendalltau(get_influence_scores(high_message_high_report_user[index],user_influence_list),get_followers_num(high_message_high_report_user[index],user_follower_num))[0]
        sum=sum+correlation
        print correlation
    print 'average correlation:%f'%(sum/len(community_member))
    print '-------------------'
    sum = 0.0
    print 'report high:influence score_followers_num_count'
    for index in range(0, len(community_member)):
        correlation=stats.kendalltau(get_influence_scores(community_report_high_user[index],user_influence_list),get_followers_num(community_report_high_user[index],user_follower_num))[0]
        sum=sum+correlation
        print correlation
    print 'average correlation:%f' % (sum/len(community_member))
    print '--------------------'
    print 'report low:influence score_followers_num_count'
    print '--------------------'
    sum=0.0
    for index in range(0, len(community_member)):
        correlation= stats.kendalltau(get_influence_scores(community_report_low_user[index],user_influence_list),get_followers_num(community_report_low_user[index],user_follower_num))[0]
        sum=sum+correlation
        print correlation
    print 'average correlation:%f' % (sum/len(community_member))
    print '--------------------'
    sum=0.0
    print 'message low:influence score_followers_num_count'
    for index in range(0, len(community_member)):
        correlation= stats.kendalltau(get_influence_scores(community_message_low_user[index],user_influence_list),get_followers_num(community_message_low_user[index],user_follower_num))[0]
        sum=sum+correlation
        print correlation
    print 'average correlation:%f' % (sum/len(community_member))
    print '--------------------'
    sum=0.0
    print 'message high:influence score_followers_num_count'
    for index in range(0, len(community_member)):
        correlation=stats.kendalltau(get_influence_scores(community_message_high_user[index],user_influence_list),get_followers_num(community_message_high_user[index],user_follower_num))[0]
        sum=sum+correlation
        print correlation
    print 'average correlation:%f' % (sum/len(community_member))
    # community_report_radio={}
    # for index in range(0,len(community_member)):
    #     report_dic=community_member_report[index]
    #     message_dic=community_member_message[index]
    #     report_radio=map(lambda (a,b):float(a)/float(b) if float(b)!=0.0 else 0.0,zip(report_dic.values(),message_dic.values()))
    #     print report_radio
    #     lm=map(fmap,community_member[index].keys(),report_radio)
    #     community_report_radio[index]=dict(lm)
    # print '------------------'
    # sum=0.0
    # print 'high message high report:influence_score_report_radio'
    # for index in range(0,len(community_member)):
    #     correlation=stats.kendalltau(get_influence_scores(high_message_high_report_user[index],user_influence_list),
    #                                  get_report_radio(high_message_high_report_user[index],community_report_radio[index]))[0]
    #     sum=sum+correlation
    #     print correlation
    # print sum

    print 'high message:influence_score_message_count'
    print 'low message:influence_score_message_count'
    print 'message:influence_score_message_count'

    print 'high report:influence score_message_count'
    print 'low report:influence score_message_count'
    print 'report:influence score_message_count'

    print 'high followers:influence score_followers_count'
    print 'low followers:influence score_followers_count'
    print 'followers:influence score_followers_count'


