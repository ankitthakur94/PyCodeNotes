## Objective ##
# Explore 
# 	class methods vs regular method of a class.
# 	static methods

## Theory : 
# Class methods are like class variables. They are not tied to any specific instance. So they are like static functions in C++.
# But note that they are not exactly static methods. Sure they do not take 'self' (the class instance) as first argument, but they do take 'cls' The class name as first argument.

# Changing something
class Organization:

	# A class variable
	affiliation = ''

	def __init__ (self, name, year):

		self.name = name
		self.year = year

	def display_info (self):
		print ( ' Name : {} , Year : {} '.format(self.name, self.year) )


	# To define a class method  use @classmethod decorator.
	# It eliminates the passing of 'self' ( which internally points to the class instance using which this method has been called )
	# Since this is a class method, it should not be tied to any instance, instead to the whole class.
	# So instead of self we the function must accept 'class name' as first argument.
	# The decorator makes this change of 'self' -> 'class name'  as first argument for class method.
	# 	Like 'self' is a standard convention for function accepting class instance as first argument, 'cls' is standard convention for functions accepting class name as first argument.
	# This is possibly another use of the decorator where we can change the interface of a function.
	@classmethod
	def set_affiliation(cls, affiliation ):
		cls.affiliation = affiliation

	@classmethod
	def get_affiliation (cls):
		return cls.affiliation



org1 = Organization ('org1', 1991)
org2 = Organization ('org2', 1992)
org3 = Organization ('org3', 1993)


org1.display_info ()
org2.display_info ()
org3.display_info ()

# The class function can be directly accessed from class name.
Organization.set_affiliation('GLOBAL_DOT_ORG')

print ( ' org1 affiliation : ' , org1.get_affiliation() )








#####################################################################
#  Class methods as alternative constructors.
#####################################################################

# Since class methods do not require the class instance to be implicitly passed, and can be called directly from class name, they are commonly used as alternate constructors.

class Organization:

	# A class member ( class variable)
	affiliation = ''

	def __init__ (self, name, year):

		self.name = name
		self.year = year

	def display_info (self):
		print ( ' Name : {} , Year : {} '.format(self.name, self.year) )


	@classmethod
	def set_affiliation(cls, affiliation ):
		cls.affiliation = affiliation

	@classmethod
	def get_affiliation (cls):
		return cls.affiliation


	# Create a class method which will act as a constructor.
	# One can create an organization instance using this method by passing a name-year string separated by a hyphen.
	@classmethod
	def from_string (cls, org_str):
		# Parse the string, split using hypen.
		name , year = org_str.split('-')
		# call the constructor and return the instance created.
		return cls (name,year)



org1 = Organization.from_string('some_organization-1990')
org1.display_info()







#######################################################
## Static Methods
#######################################################
# normal methods require class instance (self) as first argument
# CLass methods require class name (cls) as first argument
# Static methods do not require any such thing. They are like normal non-class functions.
# THey are kept in the class becauze of some logical connection to class
# They are generally used to define Utils class.

class Organization:

	# A class member ( class variable)
	affiliation = ''

	def __init__ (self, name, year):

		self.name = name
		self.year = year

	def display_info (self):
		print ( ' Name : {} , Year : {} '.format(self.name, self.year) )


	@classmethod
	def set_affiliation(cls, affiliation ):
		cls.affiliation = affiliation

	@classmethod
	def get_affiliation (cls):
		return cls.affiliation


	@classmethod
	def from_string (cls, org_str):
		# Parse the string, split using hypen.
		name , year = org_str.split('-')
		# call the constructor and return the instance created.
		return cls (name,year)

	@staticmethod
	def len_of_organization_name (str):
		return len(str)

org1 = Organization ('org_new', 2000)
# Calling a staic method
print ('org1.len : ', Organization.len_of_organization_name('org_new'))


####### CONCLUSION ###############
# Class methods are like similar to static methods in C++
#	which do not require the class instance 'self' to be passed.
#	but
#	do require the class name 'cls' to be passed. So they are not totally static
# A decorator @classmethod is placed on top of a class method.
# This converts a function's signature (i.e changes from accepting self to accepting the class name 'cls' )

# It is not rigid that class methods can only access class variables, so it is varying
# Recommended to stick to this rule
# Class methods can also be used to create alternate constructors.

# Static methods neither require self or cls.
# They are like normal functions but placed in a class because of some logical connection
###################################################

