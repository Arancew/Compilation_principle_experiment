from prettytable import PrettyTable # 用来输出表格



C = ['S->iSeS', 'S->iS', 'S->a']
# 非终结符，必须是一个字符不能写成类似E'，不然转向SLR时会出错
Vn = ['S','A']
# 终结符，必须是一个字符，空字符写成ε
Vt = ['i', 'e','a','#' ]
# 项目集的构造由此项目开始
begin = 'A->·S'
# 开始字符，如G[A]中就是A
BEGIN = 'A'


def findI(I, v):
    newI = []
    global C
    for i in range(len(I)):
        index = location(I[i])
        if index != -1 and I[i][index] == v:
            newI.append(getNextPointI(I[i]))
    addNewI(newI, C)
    return newI


def addNewI(newI, C):
    if newI == []:
        return
    oldLen = len(newI)
    for i in range(oldLen):
        index = location(newI[i])
        if index != -1 and isVn(newI[i][index]):
            for j in range(len(C)):
                if getKey(C[j]) == newI[i][index]:
                    _ = addFirstPoint(C[j])
                    if _ not in newI:
                        newI.append(_)
    if oldLen != len(newI):
        addNewI(newI, C)


def location(i):
    index = i.index('·')
    if index != -1 and (index + 1) != len(i):
        return index + 1
    return -1


def getNextPointI(i):
    iArr = i.split('·')
    iArr[1] = iArr[1][0] + '·' + iArr[1][1:]
    return ''.join(iArr)


def isVn(i):
    global Vn
    if i in Vn:
        return True
    return False


def getKey(i):
    iArr = i.split('->')
    return iArr[0]


def addFirstPoint(i):
    iArr = i.split('->')
    iArr[1] = '·' + iArr[1]
    return '->'.join(iArr)


def printI(I):
    for i in I:
        print(i)
    print("")


def generateTable(GO, I):
    global Vt, Vn
    res = {}
    for k1 in range(len(I)):
        res[k1] = {}
        for k2 in Vt + Vn:
            res[k1][k2] = ' '

    for g in GO:
        for vt in Vt:
            if vt in g:
                addTd(res, g[0], g[1], g[2], 'S')
        for vn in Vn:
            if vn in g:
                addTd(res, g[0], g[1], g[2], '')
    endI = getEndPointI()
    for i in range(1, len(endI)):
        for In in I:
            if endI[i] in In:
                for vt in Vt:
                    addTd(res, I.index(In), vt, i, 'r')
    for In in I:
        if endI[0] in In:
            addTd(res, I.index(In), '#', 'acc', '')
    pt=PrettyTable()
    pt.field_names=['state']+Vt+Vn
    for k1 in res:
        tmp=[]
        tmp.append(str(k1))
        for k2 in res[k1]:
            tmp.append(res[k1][k2])
        print(tmp)
        pt.add_row(tmp)
    print(pt)



def addTd(table, k, a, j, key):
    j = str(j)
    table[k][a] = key + j


def getEndPointI():
    global C
    endI = []
    for i in C:
        endI.append(i + '·')
    return endI

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


def main():
    global begin, C
    I = []
    GO = []
    I0 = [begin]
    addNewI(I0, C)
    I.append(I0)
    print("添加I0:")
    printI(I[0])
    for In in I:
        for v in (Vn + Vt):
            newI = findI(In, v)
            if newI != []:
                thisI = I.index(In)
                if newI in I:
                    GO.append([thisI, v, I.index(newI)])
                else:
                    GO.append([thisI, v, len(I)])
                    print("添加I" + str(len(I)) + ":")
                    I.append(newI)
                    # printI(newI)
    print("GO关系:")
    for g in GO:
        print("GO(I" + str(g[0]) + ", " + g[1] + ") = I" + str(g[2]))
    generateTable(GO, I)


if __name__ == '__main__':
    main()
