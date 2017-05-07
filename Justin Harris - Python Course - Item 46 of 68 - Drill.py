"""
    Version: Python 3.6.1
    Author: Justin C. Harris followed the tutorial on http://www.wikihow.com/Create-a-Very-Simple-Program-in-Python
    Reason: The Tech Academy - Python Course - Item 46 of 68 - Drill
"""

"""
    1. Start IDLE and use the Python range() function with one parameter to display the following:
        0
        1
        2
        3

    2.  Use the Python range() function with 3 parameters to display the following:
        3 2 1 0
        When this is working show it to your instructor.

    3.  Use the Python range() function with 3 parameters to display the following:
        8 6 4 2
        When this is working show it to your instructor.
"""

def exOne(pStop):
    for x in range(pStop):
        print(x)

def exTwoAndThree(pStart, pStop, pStep):
    printList = [x for x in range(pStart, pStop, pStep)]
    print(*printList)

exOne(4)
print("\n")
exTwoAndThree(3, -1, -1)
exTwoAndThree(8, 1, -2)

