a = [1, 1, 1, 1, 1, 1, 2]
b = [2, 3, 2, 2, 2]
c = [3, 2, 2, 2, 2]


def stray(arr):
    sett = set(arr)
    listt = list(sett)
    a,b = listt[::]
    av = arr.count(a)
    bv = arr.count(b)
    if av == 1:
        return a
    else: return b

print(stray(a))