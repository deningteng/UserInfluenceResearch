from documentRead import DocumentRead


def community_member(directory):
    # directory ='F:\\Git Repository\\InfluenceScore_result\\'
    documentReader=DocumentRead(directory)
    documentReader.load_document(key_word_list='memberOfCommunity')
    document_name=documentReader.get_documents_name()
    community_member={}
    for index in range(0,len(document_name)):
        community_member[index]={}
        f=open(directory+document_name[index])
        for line in f.readlines():
            line=line.strip('\n')
            community_member[index][line]=0
    return community_member