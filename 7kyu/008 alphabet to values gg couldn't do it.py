"""

Given a string "abc" and assuming that each letter in the string has a value equal to its position in the alphabet, our string will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.

You will be given a list of strings and your task will be to return the values of the strings as explained above multiplied by the position of that string in the list. For our purpose, position begins with 1.

nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.

"abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is multiplied by 1 while the value at position 2 is multiplied by 2.

Input will only contain lowercase characters and spaces.

Good luck!

If you like this Kata, please try:

String matchup

Consonant value

"""
# list_ = ["codewars","abc","xyz"] #[88,12,225]
# test = "a"
#
#
# #a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z == 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
#
# # print(list(map(chr, range(ord('a'), ord('z')+1))))
#
# import itertools
#
# i = iter(["a", "a", "b", "c", "b"])
# j = iter([1,2,3,4,5])
# k = list(zip(i, j))
# print(k)
#
#
# a = list()
# for i in range(1,27):
#     a.append(i)
# print(a)
# b = list(map(chr, range(ord('a'), ord('z')+1))) # letters from a to z
# print(b)
# print(len(a))
# print(len(b))
#
# a1 = iter([a])
# b1 = iter([b])
#
# for v,b in a1,b1:
#
#
#
#
#
# #
# # def name_value(my_list):
# #     xx = str()
# #     alph = dict()
# #     for strings in test:
# #         for xx in strings:
# #             return alpha()
# #
# #
#


# https://www.codewars.com/kata/598d91785d4ce3ec4f000018/solutions

