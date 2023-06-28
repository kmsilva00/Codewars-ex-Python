a ="askljhdKJHE23j1ejqadlasdj1ljelkjlzkxczxc"

def get_count(sentence):
    vowerls = ("a","e","i","o","u")
    count = 0
    for i in sentence:
        if i in vowerls:
            count +=1 
    return count

print(get_count(a))


def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")