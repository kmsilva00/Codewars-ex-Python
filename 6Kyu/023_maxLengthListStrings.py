# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

def longest_consecXXX(strarr, k):
    leniout = 0
    kout = str()
    for i in range(len(strarr)):
        for j in range(k):
            if i != j:
                if j > len(strarr)+1:
                    j = 0
                out = strarr[j]+strarr[i]
                if len(out) > leniout:
                    leniout = len(out)
                    kout = out
    return kout
        
        
def longest_consec(strarr, k):
    result = ""  # Initialize an empty string to store the result
    if k > 0 and len(strarr) >= k:  # Check if k is positive and the length of strarr is greater than or equal to k
        for index in range(len(strarr) - k + 1):  # Iterate through the range of indices to form consecutive groups of length k, starr - k ( size of iterables), 
            s = ''.join(strarr[index:index+k])  # Concatenate k consecutive strings using list slicing
            print(s)
            if len(s) > len(result):  # Check if the current concatenated string is longer than the current result
                result = s  # Update the result with the longer string

    return result  # Return the longest consecutive concatenation


print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"],3))

# print(longest_consec(["apple","banana","orange"],2))

