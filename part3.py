import sys; #x = 'foo'; sys.stdout.write(x)
import time as tm
import calendar as cal

#f(x), defining a function, def function(paramters):
def printMe(str):
    str = "This prints a passed string into this function"
    print(str)
    return

#call printMe function
printMe("Print this")
printMe("This printed again")



#f(x) def is here
def changeMe(myList):
    print("values inside the f(x) before change:", myList)
    myList[2] = 50
    print("values inside the f(x) after change:", myList)
    return
print('\n')

#value- arg is being passed by reference and the reference is being overwritten inside call f(x)
#myList is local to f(x) changing myList with function doesn't change list in f(x) itself only call 
#f(x) def is here
"""
def changeMe(myList):
    myList = [1,2,3,4]
    print("Values inside the f(x)", myList)
    return
"""
#pass reference- maintain references of the passed obj. and appending values in the same obj. reference
#Now you can call changeMe f(x)
myList = [10,20,30]
changeMe(myList)
print("values outside f(x):", myList)
print('\n')

#Global Variable Relationship
#appletest.py 
"""
^^^^
class appleTest()
    def appleTest()
        if appleTest == "appleTest":
            total = apple(10,20)
            print(total)
"""


"""
import appletest as ap
ap.total = apple(10, 20)
print(ap.test)
"""
"""
from appletest import total(10,20)
print(appletest.total)
"""