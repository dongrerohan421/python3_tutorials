'''
--> Python is OOP language.
--> Class is an extensible program code template for creating objects providing initial values of states and implementaions of behavior.
--> every function in class called as method of that class.
--> Always use self as an argument in every class member function.
--> self is just a pointer to the class instance.
'''

# self poits to class itsef. It points to bject of class.
class person:
	def setFullName(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName

	def printFullName(self):	# self is by default member function.
		print (self.firstName,"",self.lastName)


# Create instance or object of the class.
personName = person()

# Call the class methods using instance of the class.
personName.setFullName("Rohan","Dongre")
personName.printFullName()

