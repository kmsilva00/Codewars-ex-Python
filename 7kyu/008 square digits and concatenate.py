"""

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer


"""

#My solution ( not very clean but worked first time)

def square_digits(num):
    lnum = [*str(num)]
    num_2 = list()
    str_2 = str("")
    nummer_2 = list()
    for i in lnum:
        i = int(i)
        num_2.append(i**2)
    for n in num_2:
        n = str(n)
        nummer_2.append(n)
    print(nummer_2)
    return int(str_2.join(nummer_2))


print(square_digits(num))

"""
1 solution 

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

2 solution
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
"""