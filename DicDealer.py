# -*- coding: UTF-8 -*-

class DicDealer:
    def __init__(self, dic_list_org):
        self.dic_list_org = dic_list_org

    def deal_dic(self):
        #实现字典的处理和转换，生成模板需要的上下文数据
        ##########
        dealed_dic_list = []
        
        key_str = self.__get_key_str(self.dic_list_org[0])
        n = len(self.dic_list_org)
        i = 0
        while (i < n):
            row_dic = {}
            value_str = self.__get_value_str(self.dic_list_org[i])
            #print value_str
            row_dic['key_str'] = key_str.encode('gb2312')
            row_dic['value_str'] = value_str.encode('gb2312')
            #print row_dic
            dealed_dic_list.append(row_dic)
            i = i + 1
        return dealed_dic_list

    def __get_key_str(self, row0):
        n = len(row0)
        key_list_tmp = []
        i = 0
        while (i < n):
            item = row0[i]
            key_str = item['keyname']
            #print key_str
            #print type(key_str)
            key_list_tmp.append(key_str)
            i = i + 1
        key_str = ','.join(key_list_tmp)
        return key_str

    def __get_value_str(self, row):
        row_len = len(row)
        row_dic = {}
        j = 0
        item_value_list_tmp = []
        while (j < row_len):
            item = row[j]
            item_value_str = self.__deal_by_type(item['value'], item['type'])
	    #print item_value_str
            #print isinstance(item['value'], unicode)
            item_value_list_tmp.append(item_value_str)
            j = j + 1             
        value_str = ','.join(item_value_list_tmp)
        #print value_str
        return value_str
        
    def __deal_by_type(self, value, value_type):
        if value_type == 'string':
            return '\'%s\'' % (value)
        if value_type == 'int':
            return '%s' % (value)
        if value_type == 'bool':
            return '%s' % (value)

