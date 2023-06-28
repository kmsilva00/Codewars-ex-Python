        # test.assert_equals(remove_exclamation_marks("Hello World!"), "Hello World")
        # test.assert_equals(remove_exclamation_marks("Hello World!!!"), "Hello World")
        # test.assert_equals(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
        # test.assert_equals(remove_exclamation_marks(""), "")
        # test.assert_equals(remove_exclamation_marks("Oh, no!!!"), "Oh, no")

def remove_exclamation_marks(s):
    return s.replace("!","")
            


print(remove_exclamation_marks("Hi! Hello!"))


def remove_exclamation_marksAnotherSol(s):
    """ return s.replace('!', '') """
    new_s = ''
    for i in s:
        if i != '!':
            new_s += i
    return new_s