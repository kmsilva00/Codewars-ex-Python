"""

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
Note: In COBOL, it should return "found the needle at position 6"

"""
haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
#


#
# def find_needle(haystack):
#     for i in haystack:
#         #print(haystack.index(i))
#         if haystack.index("needle") == "needle":
#            return " found the needle at position {}".format(haystack.index(i))
#
# print(find_needle(haystack))
# #
#
# def find_needle(haystack):
#     for index,value in enumerate(haystack):
#         if value == "needle":
#            return " found the needle at position {}".format(index)

        # haystack.indexOf("needle")
#
def find_needle(haystack):
    if "needle" in haystack:
        return f"found the needle at position {haystack.index('needle')}"

# print(haystack.index("needle"))
# def find_needle(haystack):
#     try:
#         # if "needle" in haystack:
#         return f" found the needle at position {haystack.index('needle')}"
#     except Exception:
#         return None
#
# print(find_needle(haystack))