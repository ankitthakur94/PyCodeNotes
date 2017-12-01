#################################################
# Objective : 
# 	Create a simple class.
#	Create member variables of that class, from outside
#	Write a __init__ method.
#################################################

# Create an empty class
class Organization_1 :
	pass

# Creat a class instance and specify its name.
org1 = Organization_1 ()
org1.name = 'Change_dot_org' 	# This dynamically creates a member variable .name for the class instance org1. 

# Note that .name here is created specifically for org1 instance of the class, not for the entire class.
# This 'misfeature' is provided by many scripting languages where you can create class instance specific variables.

org2 = Organization_1 ()
org2.year = 1995
# As mentioned earlier, .year is now specific to org2 instance only.

print ( ' org1.name = ' , org1.name ) 		# Fine 
#print ( ' org2.name = ' , org2.name )		# Error  since org2 has no name attribute.



###################################################
# Using a constructor (__init__)
###################################################


class Organization_2:

	# __init__ is a maethod called when an instance of the class is created.
	# BY default the instance variable is the first argument which is passed to the class method (not only for __init__ , but for any class method )
	# generally it is called 'self' but we can use any name we want
	def __init__ (self, name, year):

		self.name = name	# See that no need to explicitly specify the member variable first and then assign. This statement will create data member 'name' and assign it.
		self.year = year

	def display_info (self):
		print ( ' Name : {} , Year : {} '.format(self.name, self.year) )

org1 = Organization_2 (name = 'change_dot_org', year = 1991)
org1.display_info ()

# Another way to call member functions is by using name of the class itslef.
Organization_2.display_info (org1)		# Same as org1.display_info ()

# Actually this is how internally calls to member functions are made.



## Conclusion : 
# __init__ method acts like constructor.
# While calling a member function of a class via a class instance variable, implicitly the instance varible is passed as the first argument to the function.
# So every class's function's first argument should be 'self' 
# However 'self' is just a convention, we can choose any name instead of self.

###########################################


















