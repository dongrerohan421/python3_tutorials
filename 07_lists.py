'''
List: It is collection of values.
Syntax: nameOfList = []
List can contain 0 value or n number of values.
Forward index of lists starts from 0 to n.
Backward index starts from -1 to -n.
To add more values to your list: nameOfList.append[value]
Python list can have different types of datatypes in it.
You can add two different list together using extend().
Syntax: nameOfList_1.extend(nameOfList_2)
To remove items from list: nameOfList.remove(value)
'''

name = []
print (name)

name = ["Mark","Adam","Viraf","Ravi","Rohan"]
print (name)


# Forward index.
print ("name[0]: ")
print (name[0])
print ("name[1]: ")
print (name[1])
print ("name[2]: ")
print (name[2])
print ("name[3]: ")
print (name[3])
print ("name[4]: ")
print (name[4])


# Backward index.
print ("name[-1]: ")
print (name[-1])
print ("name[-2]: ")
print (name[-2])
print ("name[-3]: ")
print (name[-3])
print ("name[-4]: ")
print (name[-4])
print ("name[-5]: ")
print (name[-5])


# To add more value to your list.
name.append("Nishant")
print (name)


# Age list.
age = [21,22,26]
print (age)


# Adding two diff. lists together using extend().
name.extend(age)

print (name)

# Remove value from list.
name.remove(21)

print (name,age)

# To find length of list.
print ("Length of name[]:")
print (len(name))

# To find max of list
print ("Max of age[]:")
print (max(age))
