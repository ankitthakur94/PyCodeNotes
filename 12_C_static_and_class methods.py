## Objective ##
# Explore 
# 	class methods vs regular method of a class.
# 	static methods

## Theory : 
# Class methods are like class variables. They are not tied to any specific instance. So they are like static functions in C++.

# Changing something
class Organization:

	# A class member ( static data member ) 
	affiliation = ''

	def __init__ (self, name, year):

		self.name = name
		self.year = year

	def display_info (self):
		print ( ' Name : {} , Year : {} '.format(self.name, self.year) )


	# To define a class method ( static method ) use @classmethod decorator.
	# It eliminates the passing of 'self' ( which internally points to the class instance using which this method has been called )
	# Since this is a static method, it should not be tied to any instance, instead to the whole class.
	# So instead of self we the function must accept 'class name' as first argument.
	# The decorator makes this change of 'self' -> 'class name'  as first argument for class method.
	# 	Like 'self' is a standard convention for function accepting class instance as first argument, 'cls' is standard convention for functions accepting class name as first argument.
	# This is possibly another use of the decorator where we can change the interface of a function.
	@classmethod
	def set_affiliation(cls, affiliation ):
		cls.affiliation = affiliation

	def get_affiliation (self):
		return self.affiliation



org1 = Organization ('org1', 1991)
org2 = Organization ('org2', 1992)
org3 = Organization ('org3', 1993)


org1.display_info ()
org2.display_info ()
org3.display_info ()

Organization.set_affiliation('GLOBAL_DOT_ORG')

print ( ' org1 affiliation : ' , org1.get_affiliation() )








#####################################################################
#  Class methods as alternative constructors.
#####################################################################























