        # test.assert_equals(pofi(0),'1')
        # test.assert_equals(pofi(1),'i')
        # test.assert_equals(pofi(2),'-1')
        # test.assert_equals(pofi(3),'-i')
        # test.assert_equals(pofi(4),'1')
        # test.assert_equals(pofi(5),'i')
        # test.assert_equals(pofi(6),'-1')
        # test.assert_equals(pofi(7),'-i')
        # test.assert_equals(pofi(8),'1')
        # test.assert_equals(pofi(9),'i')
        # test.assert_equals(pofi(10),'-1')
        
        
def pofi(n):
    while n > 100:
        n -= 100
    o = 1j**n
    if o == (-0-1j):
        o = "-i"
    if o == (-0+1j):
        o = "i"
    if o == (-1+0j):
        o = "-1"
    if o == (1+0j):
        o = "1"        
    return o
    

print(pofi(341))


def pofisol(n):
    return ['1','i','-1','-i'][n%4]


