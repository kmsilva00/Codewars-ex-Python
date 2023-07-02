# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    if not names:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + str(" likes this")
    if len(names) == 2:
        return names[0] + str(" and ") + names[1] + str(" like this")
    if len(names) == 3:
        return names[0] + str(", ") + names[1] + str(" and ") + names[2] + " like this"
    if len(names) > 3:
        return names[0] + str(", ") + names[1] + str(" and ") + str(len(names)-2) + " others like this"
    
    
def likessol (names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
    
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)