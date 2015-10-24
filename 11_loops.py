'''
Loop is piece of program that executes again and again.
'''

a = 0	# initiallization
while a<5:	# Condition
	print (a)	#statements
	a += 1	# similar as a=a+1 


a = 1
s = 0
print ("Enter numbers to add the sum.")
print ("Enter 0 to quit.")

while a != 0:
	print ("Current sum is: ", s)
	a = float(input("Number?:"))
	a = float(a)
	s += a
print ("Total sum: ",s)


# For loop:
b = [3,5,9,7,4,1,2,3,6,5,6]
for num in b:
	print (num)
