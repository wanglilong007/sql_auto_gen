# -*- coding: UTF-8 -*-

from ExcelParser import ExcelParser
from DicDealer import DicDealer
from SqlGenerator import SqlGenerator
from StringToFileGenerator import StringToFileGenerator

class SqlGenerateProc ():
    def __init__(self, xls_file, sheet, sql_tpt, sql_file):
        self.xls_file = xls_file
        self.sheet = sheet
        self.sql_tpt = sql_tpt
        self.sql_file = sql_file
    def run(self):
        parser = ExcelParser(self.xls_file, self.sheet)
        rows_list = parser.excel_parse()

        if rows_list == False:
            print 'Check excel template Error!'
            exit
        #print rows_list
        dealer = DicDealer(rows_list)
        dealed_list = dealer.deal_dic()

        #print dealed_list

        gener = SqlGenerator(self.sql_tpt, dealed_list)
        sqlstr = gener.gen_sql_str()
        #print sqlstr

        filegen = StringToFileGenerator(sqlstr)
        filegen.gen_file(self.sql_file)

def merge_file(file_list, final_file):
    sql_final_file = open(final_file, 'w')
    for file_sql in file_list:
        sql_file = open(file_sql, 'r')
        lines = sql_file.read()
        sql_final_file.write(lines)
        sql_final_file.write('\n--------------------------------merge---------------------------------------\n')
        sql_file.close() 
    sql_final_file.close()
