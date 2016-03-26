# -*- coding: UTF-8 -*-
from Schedule import SqlGenerateProc
from Schedule import merge_file
# 创建新线程
thread1 = SqlGenerateProc('Template.xlsx', 'LanguageKey', 'SqlTemplates\LangKeyRscSqlCode.sql', 'GeneratedSqlScript\LangKeyRscSqlCode.sql')
thread2 = SqlGenerateProc('Template.xlsx', 'LanguageValue', 'SqlTemplates\LangValueRscSqlCode.sql', 'GeneratedSqlScript\LanguageValueRscSqlCode.sql')
thread3 = SqlGenerateProc('Template.xlsx', 'MenuResource', 'SqlTemplates\MenuRscSqlCode.sql', 'GeneratedSqlScript\MenuRscSqlCode.sql')
thread4 = SqlGenerateProc('Template.xlsx', 'RolePermission', 'SqlTemplates\RolePmsSqlCode.sql', 'GeneratedSqlScript\RolePmsRscSqlCode.sql')

# 开启线程
thread1.run()
thread2.run()
thread3.run()
thread4.run()

print "Exiting Partial Generate Work"

file_list = ['SqlTemplates\TRAN_before.txt','GeneratedSqlScript\LangKeyRscSqlCode.sql', 'GeneratedSqlScript\LanguageValueRscSqlCode.sql',\
             'GeneratedSqlScript\MenuRscSqlCode.sql', 'GeneratedSqlScript\RolePmsRscSqlCode.sql','SqlTemplates\TRAN_end.txt']

merge_file(file_list, 'Zmain.sql')

print 'Succeed Generate SQL Script files!'
