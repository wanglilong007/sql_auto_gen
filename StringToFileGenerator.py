import codecs


class StringToFileGenerator:
    def __init__(self, str):
        self.str = str

    def gen_file(self, filepath):
        sql_file = open(filepath, 'w')
        sql_file.write(self.str)
        #sql_file.write(self.str.encode('utf8'))
        sql_file.close()
