'''
This progam show how to use built in Python's functions.
'''

# use pow() to get exponential.
print (pow(2,3))

# Command to list Python's nuilt in funcions
print ("Built in functions list: ")
print (dir(__builtins__))

# abs(): absolute function
print (abs(18.666))

print (len ("Let's get high"))

# use help() to know about built in functions
print ("getattr(): ")
print (help(getattr))

# Built in Modules.
# import math module and sqrt()

import math
print (math.sqrt(9))

# Declare variable for your Module Function
squareRoot = math.sqrt
print (int(squareRoot(16)))
