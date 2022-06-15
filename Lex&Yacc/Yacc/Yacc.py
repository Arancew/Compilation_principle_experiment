import pre_lex_gacc.ply.yacc as yacc
from pre_lex_gacc.Lex.Lex import tokens
literals = []

# 规定运算符的优先级和结合性，越靠前的运算符优先级越低
# 结合性有左结合，右结合，无结合性
precedence = (
    ('left', '48', '49'),  # 加减法优先级较低
    ('left', '45', '46'),  # 乘除法优先级较高
)

names = {}


# 程序
def p_A(p):
    '''
    A : 17 19 34 35 66 B E 67
    '''
    print("规约成功")


# 声明序列
def p_B(p):
    '''
    B : C B
    |
    '''
    pass


# 声明语句
def p_C(p):
    '''
    C : 17 D 65
    | 13 D 65
    '''
    pass


# 标识符表
def p_D(p):
    '''
    D : 0 33 D
    | 0
	'''
    pass


# 语句序列
def p_E(p):
    '''
    E : F E
    |
    '''
    pass


# 语句
def p_F(p):
    '''
    F : N
    '''
    pass

# 赋值语句
def p_N(p):
    '''
    N : O 65
	'''
    pass


# 表达式
def p_O(p):
    '''
    O : 0 60 S
    '''
    names[p[1]] = p[3]
    print(names[p[1]])
    pass


# 算术表达式 S+S S-S S*S S/S

def p_S_binop(p):
    '''
    S : S 48 S
    | S 49 S
    | S 45 S
    | S 46 S
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


# (S)
def p_S_group(p):
    "S : 34 S 35"
    p[0] = p[2]


# S 为无符号整数
def p_S_number(p):
    "S : 71"
    p[0] = p[1]


# S 为标识符
def p_S_name(p):
    "S : 0"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


# 规约失败
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()
s = 'int main(){int a; int b,c; a = 3*(5+10)*10; b = 3*5+10*10; c = a + b; }'
result = parser.parse(s)
