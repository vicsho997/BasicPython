#how you put multiple statements on one line
#   use ;
import sys; x = 'foo'; sys.stdout.write(x)
print(" ")
print("1" + '\n' + "1")
print("1" + "\+" + "1") #tab??

str = 'hello world'
str1 = str 

x = 11
i = 1


#while (break)
while i < 6:
  print(i)
  if i == 3:
    break #pass, break, continue
  i += 1 
 
    
  #while (continue)
  j = 0
while j < 6:
  j += 1 
  if j == 3:
    continue
  print(j)
  
  
  
#if, elif, else
if (x>10):
    print(str1)
    print(str1[0])
    print(str1[2:5])
    print(str1[2:])
    print(str1 * 2)
    print(str1 + "Test")
elif(x>2):
    print("change x to 3")    
else:
    print ("change x to 0")

print('\n')


list1 = ['pysics', 'chemistry', 1999, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

tuple1 = ('pysics', 'chemistry', 1999, 2000)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("a", "b", "c", "d")

emptyDict = { }
fullDict = {1:3, 2:4, 56:6}

#print(len(fullDict))
print(len([1, 2, 3]))
print([1,2,3]+[4,5,6])
print(['Hi']*4)
print(3 in [1,2,3])



for x in range(6):
  print(x)
else:
  print("Finally finished!") #Print all numbers from 0 to 5, and print a message when the loop has ended:

"""
https://www.javacodegeeks.net/python3/python3-iterator-generator.php
#generator
+
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
"""

#tick - are floating point numbers in units of seconds starting at 12:00am , jan 1, 1970
#time.time() function returns the current system time
import time
import calendar

#local time = time.asctime(time.localtime(time.time()))

 