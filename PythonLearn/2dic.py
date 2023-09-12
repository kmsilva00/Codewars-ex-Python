def makedic(g):
    dic = dict()
    for i in g:    
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    return dic

