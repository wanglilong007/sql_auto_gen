
# -*- coding: UTF-8 -*-

import xlrd
import os
# 获取行和列值
# 第一行为字典的key，接下来的各行为值，并组成列表

class ExcelParser:
    def __init__(self, excel_file,excel_sheet_name):
        self.excel_file = excel_file
        self.excel_sheet_name = excel_sheet_name
        
    def excel_parse(self):
        ## 实现excel的解析，生成字典列表
        xls = xlrd.open_workbook(self.excel_file)
        table = xls.sheet_by_name(self.excel_sheet_name)
        
        nrows = table.nrows
        ncols = table.ncols

        row_list = []
        
        i = 2
        
        while (i < nrows):
            j = 0
            item_list = []
            while (j < ncols):
                dic = {}
                dic['keyname'] = table.cell(0,j).value
                dic['type'] = table.cell(1,j).value
                dic['value'] = table.cell(i,j).value
                if self.check_item(dic) == False:
                    print dic
                    os._exit(1)
                item_list.append(dic)
                j = j + 1
                
            row_list.append(item_list)  
            i = i + 1
        
        return row_list

    def check_item(self, dic):
        if dic['type'] not in ['string', 'int', 'bool']:
            print '%s key type wrong!' % dic['type']
            return False
        if type(dic['value']) not in [unicode,str]:
            print '%s Value type %s wrong!' % (dic['value'],type(dic['value']))
            return False
        if dic['type'] == 'int':
            try:
                int(dic['value'])
            except ValueError:
                print '%s Int Value Error!' % dic['value']
                return False
            else:
                return True
        
