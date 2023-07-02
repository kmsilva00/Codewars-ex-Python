def duplicate_encode(word):
    dic = dict()
    stro = str()
    strv = stro
    out = str()
    for i in word.lower():    
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    ilist = list(dic.items())
    for i in ilist:
        i = str(i)
        stro += i[-2]
        strv += i[-6]
    
    for j in word.lower():
        s = strv.index(j)
        if int(stro[s]) == 1:
            out += "("
        else:
            out += ")"
    return out

print(duplicate_encode("Success"))