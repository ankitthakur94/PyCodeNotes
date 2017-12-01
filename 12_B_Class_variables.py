## Objective :
# 	Class instance variables vs Class variables.
###########################################


###########################################
## Class varaibles :
###########################################
# Same for each instance of the class ( not tied to any class instance )
# Kind of like static varibles in C++
###########################################



class Organization :

	## Class variables :
	num_organizations = 0

	def __init__ (self, name, year):

		self.name = name	
		self.year = year
		
		# We access the class variables not via self, instead via the class's  name.
		# Since class variable is same for all instances of the class, and self refers to the instance of the class on which method is called, it makes no sense to use self here.
		Organization.num_organizations += 1

	def display_info (self):
		print ( ' Name : {} , Year : {} '.format(self.name, self.year) )


org1 = Organization ('org1', 1991)
org2 = Organization ('org2', 1992)
org3 = Organization ('org3', 1993)


org1.display_info ()
org2.display_info ()
org3.display_info ()

## We can access the class variable from any of the class instance or directly via class name also.
# Value for the class variable will be the same, no matter how is it accessed.
# A general tradition is to access via class name, not class instance.
print ( ' Num of organizations as per class : ', Organization.num_organizations )
print ( ' Num of organizations as per org1 : ', org1.num_organizations )
print ( ' Num of organizations as per org2 : ', org2.num_organizations )
print ( ' Num of organizations as per org3 : ', org3.num_organizations )





##### CONCLUSION : ##########
# A class variable is not tied to any instance of the class, it holds the same value for every instance.
# Can be accessed via class name (recommended) / instance name.




