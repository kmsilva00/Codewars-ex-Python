def disemvowel(string_):
    strout = str()
    for i in string_:
        if i in "aeiouAEIOU":
            continue
        else:
            strout += i
    return strout