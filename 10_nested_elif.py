'''
This program explains nested if else.
'''

name = input("Name: ?")

# Example of elif:
if name == "Mark":
	print ("The name entered is ", name)
elif name == "Adam":
	print ("The name entered is ", name)
elif name == "Viraf":
        print ("The name entered is ", name)
elif name == "Ravi":
        print ("The name entered is ", name)
elif name == "Nishant":
        print ("The name entered is ", name)
else:
        print ("The name entered is not valid.")


# Example of nested if:
name = "animal"
animalName = "dog"

if name == "animal":
	if animalName == "dog":
		print (animalName, " is valid animal.")
	else:
		print (animalName, " is not valid animal.")
	print ("Name entered is animal.")
else:
	print ("The name entered is not valid.")
