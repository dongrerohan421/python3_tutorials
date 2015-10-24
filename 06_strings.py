'''
This program explains Pytho's string
'''

# Escape character usefule to jump over any character.
# Use double back slash to print back slash in your output.

a = 'I am \\single quoted string. Don\'t'
b = "I am \\double quoted string. Don\"t"
c = """I am \\triple quoted string. Don\'t"""

print (a)
print (b)
print (c)

# To calculate length of string use len() function
print ("Lentgth of the string c is: ")
print (len(c))


d = "Hello "
e = "World"
f = 5

# '+' operator can be used as concatenation operator to join multiple strings.

print (d + e)

# Use '*' operator to print letter multiple times
print (d * 10) 

# Use str() to convert integer to string.
print (d + str(f))
