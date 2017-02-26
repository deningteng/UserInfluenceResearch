#coding:utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

class DocumentRead(object):
    def __init__(self,directory):
        self.directory=directory
        self.documents={}
        self.documents_name={}

    def get_documents(self):
        return self.documents

    def get_documents_name(self):
        return self.documents_name

    def load_document(self,key_word_list=None, no_key_word_list=None):
        directory=self.directory
        document_name_list = self.get_dirlist(path=directory, key_word_list=key_word_list,
                                              no_key_word_list=no_key_word_list)
        for index in range(0, len(document_name_list),1):
            document_name = document_name_list[index]
            document = self.read_document(directory=directory, document_name=document_name)
            self.documents[index]=document
            self.documents_name[index]=document_name

    def read_document(self,directory,document_name):
        with open(directory+"\\"+document_name) as f:
            text = f.read()
        return text

    def get_dirlist(self,path,key_word_list=None, no_key_word_list=None):
        file_name_list = os.listdir(path)
        if key_word_list == None and no_key_word_list == None:
            temp_file_list = file_name_list
        elif key_word_list != None and no_key_word_list == None:
            temp_file_list = []
            for file_name in file_name_list:
                have_key_words = True
                for key_word in key_word_list:
                    if key_word not in file_name:
                        have_key_words = False
                        break
                    else:
                        pass
                if have_key_words == True:
                    temp_file_list.append(file_name)
        elif key_word_list == None and no_key_word_list != None:
            temp_file_list = []
            for file_name in file_name_list:
                have_no_key_word = False
                for no_key_word in no_key_word_list:
                    if no_key_word in file_name:
                        have_no_key_word = True
                        break
                if have_no_key_word == False:
                    temp_file_list.append(file_name)
        elif key_word_list != None and no_key_word_list != None:
            temp_file_list = []
            for file_name in file_name_list:
                have_key_words = True
                for key_word in key_word_list:
                    if key_word not in file_name:
                        have_key_words = False
                        break
                    else:
                        pass
                have_no_key_word = False
                for no_key_word in no_key_word_list:
                    if no_key_word in file_name:
                        have_no_key_word = True
                        break
                    else:
                        pass
                if have_key_words == True and have_no_key_word == False:
                    temp_file_list.append(file_name)
        return temp_file_list