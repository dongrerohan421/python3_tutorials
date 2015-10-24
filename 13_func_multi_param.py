'''
This program demonstates functions with multiple parameters.
'''

def studentScore (name,score):
	print (name, "Scored ", score, " Marks" )

studentScore("Rohan",94)


# * used to store multiple values in perticular argument
def studentScore (name,*score):
	print(name)
	print(score)

# see *score can store multiple values.
studentScore("Rohan",56,45,78,65)
