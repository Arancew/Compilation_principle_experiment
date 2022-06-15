import re


class PreWork():

    def __init__(self, pre_file_path, file_path):
        self.pre_file_path = pre_file_path
        self.file_path = file_path

    def run(self):
        with open(self.pre_file_path, 'r', encoding='UTF-8') as f:
            txt = f.read()
            deal_txt = re.sub(r'/\*(.|[\r\n])*?\*/|//.*', ' ', txt)  # 去除多行注释和单行注释
            deal_txt = deal_txt.strip()                              # 去除前后空格
            deal_txt = deal_txt.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')  #去掉换行和回车和tab
            deal_txt = ' '.join(deal_txt.split()) #根据空格分开，然后再用一个空格连接在一起，使得多个空格变一个
        with open(self.file_path, 'w') as f:
            f.write(deal_txt)
