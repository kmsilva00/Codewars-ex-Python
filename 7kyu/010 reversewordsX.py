a1 = "word"
a = "Somebody Once Told Me"
b = " a b c d "
c = "double  spaces"
d = "The quick brown fox jumps over the lazy dog."

b = list(a)

c = b[::-1]


text1 = d.split(" ")



a0 = ""
a1 = ""
j = 0
for i in range(len(text1)):
    rever = str(list(text1[i])[::-1])
    
    a0 = a0 + rever
    a0 = str(a0)

for i in a0: 
    if i == "[" or i == "'" or i == "]" or i == ",":
        continue
    else:
        a1 = a1+(a0[j])
    j += 1
        
print(a1)