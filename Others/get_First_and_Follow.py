# 用前需配置全局变量如下
# 拓广文法G[A]，必须写开，不能带或
C = ['A->E', 'E->E+T', 'E->T', 'T->T*F','T->F','F->(E)', 'F->i']
# 非终结符，必须是一个字符不能写成类似E'，不然转向SLR时会出错
Vn = ['A', 'E', 'T', 'F', ]
# 终结符，必须是一个字符，空字符写成ε
Vt = ['+', '*','(', ')', 'i', '#']
# 项目集的构造由此项目开始
begin = 'A->·E'
# 开始字符，如G[A]中就是A
BEGIN = 'A'

def checkEmpty(v):
    global C
    for i in C:
        iArr = i.split('->')
        if iArr[0] == v and iArr[1] == 'ε':
            return True
    return False


def addInSet(arr, o):
    flag = False
    if type(o) == str:
        if o not in arr:
            flag = True
            arr.append(o)
    else:
        for m in o:
            if m not in arr:
                flag = True
                arr.append(m)
    return flag
def getFirst():
    global C, Vt, Vn
    first = {}
    for i in C:
        first[i.split('->')[0]] = []
    while True:
        flag = False
        for i in C:
            key = i.split('->')[0]
            tmp=i.split('->')
            # print(tmp)
            r1 = tmp[1][0]
            if r1 in Vt or r1 == 'ε':
                if addInSet(first[key], r1) == True:
                    flag = True
            if r1 in Vn:
                empty = 0
                for t in i.split('->')[1]:
                    if t in Vn:
                        if addInSet(first[key], [_ for _ in first[t] if _ != 'ε']) == True:
                            flag = True
                        if checkEmpty(t) == False:
                            break
                        else:
                            empty += 1
                    else:
                        break
                if empty == len(i.split('->')[1]):
                    if addInSet(first[key], 'ε') == True:
                        flag = True
        if flag == False:
            break
    return first
def getFOLLOW(first):
    follow = {}
    global C, BEGIN
    for v in Vn:
        if v == BEGIN:
            follow[v] = set('#')
        else:
            follow[v] = set()
    while True:
        _flag = False
        for i in C:
            left = i.split('->')[0]
            right = i.split('->')[1]
            for index in range(len(right)):
                if right[index] in Vt or 'ε' in right[index]:
                    continue
                if index == (len(right) - 1):
                    for _ in follow[left]:
                        lg = len(follow[right[index]])
                        follow[right[index]].add(_)
                        if lg < len(follow[right[index]]):
                            _flag = True
                else:
                    if right[index + 1] in Vt:
                        follow[right[index]].add(right[index + 1])
                        lg = len(follow[right[index]])
                        if lg < len(follow[right[index]]):
                            _flag = True
                    else:
                        for _ in first[right[index + 1]]:
                            if _ != 'ε':
                                follow[right[index]].add(_)
                                lg = len(follow[right[index]])
                                if lg < len(follow[right[index]]):
                                    _flag = True
                    flag = False
                    for _ in right[index + 1:]:
                        if (_ in Vt) or ('ε' not in first[_]):
                            flag = True
                    if flag == False:
                        for _ in follow[left]:
                            follow[right[index]].add(_)
                            lg = len(follow[right[index]])
                            if lg < len(follow[right[index]]):
                                _flag = True

        if _flag == False:
            break
    return follow
if __name__=='__main__':
    First=getFirst()
    Follow=getFOLLOW(First)
    print("FIRST集:")
    for k in Vn:
        if k =='A':
            continue
        print('     FIRST[', k, ']: ', First[k])
    print("FOLLOW集:")
    for k in Vn:
        if k =='A':
            continue
        print('     FOLLOW[', k, ']: ', Follow[k])