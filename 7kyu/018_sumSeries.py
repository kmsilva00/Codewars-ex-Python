def series_sum(n):
    j = 1
    out = 0
    for i in range((int(n))):
        out += (1/j)
        j += 3
    return out        

def series_sum1(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum

print(series_sum1(2))