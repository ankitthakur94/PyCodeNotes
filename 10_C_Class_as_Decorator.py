#########################################################
## Objective : 
#########################################################
#  Use a class as a decorator
#########################################################


class decorator_class:

	# This is like a constructor in C++
	def __init__ (self, orig_func):
		self.orig_func = orig_func
	
	# __call__ is a standard function name which will be called when a function is decorated with this class.
	def __call__ (self, *args, **kwargs):
		print ( ' Class Decorator called before func ' , self.orig_func.__name__ )

		# Call the original function with arguments  and return the value.
		return (self.orig_func (*args, **kwargs) )
		
		# Here no need to return the wrapper_funcion as we did in function as decorator tutorial.
	
@decorator_class
def print_details (name, age):
	print ( ' Name {} , Age {} '.format (name, age) )


print_details ('Ankit' , 23)

#########################################################
##  Conclusion :
#########################################################
# A class can also be used to decorate a function.
# __call__ methods should be defined in the class. This will be executed when the decorated function is called.
# Interface for the __call__method should be the same as the interface for function to be decorated.
# A class decorator is more flexible, but more code needs to be written for that as compared to a function decorator.
#########################################################



