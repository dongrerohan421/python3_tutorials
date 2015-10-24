'''
This program explains constructor(__init__ ) and destructor(__de__)
Constructor: Initialization of member functions of the class.
__init__: Reserved keyword for constructor.
Destructor: Deletion of member function of the class.
__del__: Reserved keyword for destructor.
'''


# Use of constructor in python.
class person:
	def __init__(self,id):	# Constructor used to initialize the values.
		self.id = id
		print ("Our class is created.")
	def __del__(self):
		print (self.id,"Our class object is destroyed.")
	def setFullName(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName
	def printFullName(self):
		print (self.firstName,self.lastName)

personName = person(5)	# Passing 5 as an id.
personName.setFullName("Rohan","Dongre")
personName.printFullName()
#personName.__del__()
