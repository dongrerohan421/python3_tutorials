'''
Inheritance: It allows us to define class in terms of another class, which makes it easier to create and maintain an application.

You can inherit multiple classes in your child class.
Syntax: class Child (Parent1,Parent2,...):
'''

# Parent class is superclass
class Parent:
	value1 = "This is value 1"
	value2 = "This is value 2"


# Child class is subclass.
class Child (Parent):
	pass


# create instance of parent class.
parent_ = Parent()
print (parent_.value1)
print (parent_.value2)

# Create instance of child class.
child_ = Child()
print (child_.value1)
print (child_.value2)
