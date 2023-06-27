a = 'eloquent'

def remove_char(s):
    s = list(s)
    ss = str()
    s[0] = ""
    s[-1] = ""
    for i in s:
        ss += i
    return ss

def solremove_char(s):
    return s[1 : -1]