import re

text = "my email is kmsilva00@gmail.com"
pattern = r"\b\w+@\w+\.\w+\b"


match = re.search(text,pattern)

"""if match:
    print(match.group())
else:
    print("no match")
"""

text1 = "My phone numbers are 123-456-7890 and 987-654-3210."
pattern1 = r"\d{3}-\d{3}-\d{4}"

matches1 = re.findall(pattern1, text1)
# print(matches1)


text2 = "My email is example@email.com"
pattern2 = r"\b\w+@\w+\.\w+\b"

new_text2 = re.sub(pattern2, "REDACTED", text2)
# print(new_text2)

text3 = "The quick brown Fox"
pattern3 = r"fox"
match3 = re.search(pattern, text, re.IGNORECASE)

if match3:
    print("match3 found")
else:
    print("match3 not found")