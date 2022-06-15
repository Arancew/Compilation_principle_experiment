import pre_lex_gacc.ply.lex as lex
from pre_lex_gacc.ply.lex import TOKEN

# 匹配保留字
reserved = {
    'auto': '1',
    'break': '2',
    'char': '3',
    'case': '4',
    'const': '5',
    'continue': '6',
    'default': '7',
    'do': '8',
    'double': '9',
    'else': '10',
    'enum': '11',
    'extern': '12',
    'float': '13',
    'for': '14',
    'goto': '15',
    'if': '16',
    'int': '17',
    'long': '18',
    'main': '19',
    'return': '20',
    'register': '21',
    'short': '22',
    'signed': '23',
    'sizeof': '24',
    'static': '25',
    'struct': '26',
    'switch': '27',
    'typedef': '28',
    'union': '29',
    'unsigned': '30',
    'void': '31',
    'while': '32',
}
# token列表
tokens = ['0',
          '33', '34', '35', '36', '37', '38', '39',
          '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
          '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
          '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
          '70', '71', '72'] + list(reserved.values())
# 正则表达式的匹配规则
t_33 = r','
t_34 = r'\('
t_35 = r'\)'
t_36 = r'\['
t_37 = r'\]'
t_38 = r'->'
t_39 = r'\.'
t_40 = r'!'
t_41 = r'\+\+'
t_42 = r'--'
t_43 = r'&'
t_44 = r'~'
t_45 = r'\*'
t_46 = r'\/'
t_47 = r'%'
t_48 = r'\+'
t_49 = r'-'
t_50 = r'<<'
t_51 = r'>>'
t_52 = r'<'
t_53 = r'<+'
t_54 = r'>'
t_55 = r'>='
t_56 = r'=='
t_57 = r'!='
t_58 = r'&&'
t_59 = r'\|\|'
t_60 = r'='
t_61 = r'\+='
t_62 = r'-='
t_63 = r'\*='
t_64 = r'\/='
t_65 = r';'
t_66 = r'\{'
t_67 = r'\}'
t_68 = r'\''
t_69 = r'\"'
t_72 = r'\"(\\.|[^"\\])*\"'
digit = r'([0-9])'
no_digit = r'([_A-Za-z])'
identifier = r'(' + no_digit + r'(' + digit + r'|' + no_digit + r')*)'


# 指定了一些操作的正则表达式匹配规则

@TOKEN(identifier)  # 0的正则表达式规则是上面的identifier
def t_0(t):
    t.type = reserved.get(t.value, '0')  # 检查是否为保留字
    return t


def t_70(t):
    r'[0-9]*\.[0-9]+'
    t.value = float(t.value)
    return t


def t_71(t):
    r'\d+'
    t.value = int(t.value)
    return t


# 获取行号
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# 忽略字符规则(空格和tab)
t_ignore = ' \t'


# 检测到非法字符时发生的词法分析错误
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


class LexAnalysis():
    def __init__(self, pre_file_path, file_path):
        self.pre_file_path = pre_file_path
        self.file_path = file_path
        self.lexer = lex.lex()

    def run(self):
        with open(self.pre_file_path, 'r') as f:
            deal_txt = f.read()
        self.lexer.input(deal_txt)
        tmp = ''
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            tmp += str(tok) + '\n'
            # 输出四元式 (tok.type, tok.value, tok.lineno, tok.lexpos)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(tmp)
