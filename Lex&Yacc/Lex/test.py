from pre_lex_gacc.Prework.Prewrok import PreWork
from Lex import LexAnalysis
tmp1 = PreWork('../Data/data.txt', '../Data/code.txt')
tmp1.run()
tmp2 = LexAnalysis('../Data/code.txt', '../Data/lex_code.txt')
tmp2.run()
