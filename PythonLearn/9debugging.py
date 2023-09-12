import pdb

def divide(a, b):
    pdb.set_trace()
    result = a / b
    return result
"""

n (next): Execute the current line and move to the next line of code.
c (continue): Continue execution until the next breakpoint or until the program exits.
s (step): Step into a function (if the current line calls a function).
q (quit): Quit the debugger and terminate the program.
b (break): Set a breakpoint at the current line or a specific line number.
l (list): List the source code around the current line.
p (print): Print the value of a variable or expression.
h (help): Display a list of available commands and their descriptions.

"""

# print(divide(10,2))

import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    result = a / b
    logging.debug(f"Result: {result}")
    return result

