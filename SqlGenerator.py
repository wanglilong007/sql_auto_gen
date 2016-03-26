import tenjin
#tenjin.set_template_encoding('utf-8')  # optional (defualt 'utf-8')
from tenjin.helpers import *
from tenjin.html import *

class SqlGenerator:
    def __init__(self, sql_tpt_file, data_info_dic_list):
        self.data_info_dic_list = data_info_dic_list
        self.sql_tpt_file = sql_tpt_file

    def gen_sql_str(self):
        engine = tenjin.Engine()
        context = {}
        context['data'] = self.data_info_dic_list
        #print context
        sql_str = engine.render(self.sql_tpt_file, context)
        #print sql_str
        return sql_str
