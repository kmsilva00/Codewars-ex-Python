s = "abbca"

def is_palindromeNoCasing(s):
    return True if s.lower()[::] == s.lower()[::-1] else False


def is_palindrome(s):
    return s.lower()



def is_palindromeSol(s):
    return s.lower() == s[::-1].lower()

print(is_palindrome(s))

print(is_palindromeNoCasing(s))