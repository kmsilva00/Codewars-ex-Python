a = "Somebody Once Told Me"
b = " a b c d "
c = "double  spaces"
d = "The quick brown fox jumps over the lazy dog."

def reverse_words(text):
    text = str(text)
    r_text = ""
    for i in range(len(text)+1):
        try:
            r_text = r_text + text[len(text)-i]
        except:
            continue
    return r_text
        
print(reverse_words(d))