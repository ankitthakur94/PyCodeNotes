#########################################################
## Objective : 
#########################################################
# Implement decorators with arguments
#########################################################

# Remember a closure, which is a function accepting some arguments and returning a function.
# Example usage : form a linear eqn of the form a*x + b
# Outer function accpets a and b and returns inner function.
# Inner function remembers a and b (which are now fixed) and accepts (x) and evaluated eqn for given x

# In decorators we intend to execute something before a function, but without changing the code of the function.
# The extra something which is to be executed is fixed in decorator itself.
# Below is an example where we print something extra before executing the original function.

# Writing a simple log_decorator.
def log_decorator (orig_func):

	def log_wrapper (*args, **kwargs):
		print ( ' Logging for function : ', orig_func.__name__ )			# Extra something to do (print something)
		return (orig_func (*args, **kwargs) )

	return log_wrapper


@log_decorator
def compute_sum_1 (a,b):
	[ i for i in range (9999999) ]
	return (a+b)

print ( ' ----  Using standard way of decorator  ---- ' )
sum = compute_sum_1 (3,5)
print ( ' Sum = {}'.format (sum) )



## But what if we want that extra something to be specified from outside and not harcode in the decorator itself.
## Say we will pass the string 'Logging for function ..' from outside to the decorator.
# For that we use wrap the decorator a level further.

def top_decorator (str_to_print):
	def log_decorator (orig_func):

		def log_wrapper (*args, **kwargs):
			print ( str_to_print , orig_func.__name__ )			# Extra something to do (print something)
			return (orig_func (*args, **kwargs) )

		return log_wrapper

	return log_decorator		# Another level of return. We return the log_decorator function.

# Now lets decorate a function using the above nested decorator set
def compute_sum_2 (a,b):
	[ i for i in range (9999999) ]
	return (a+b)

# Manually writing the decorator flow

# First call the  top_decorator with string to be printed as argument.
# It returns the log_decorator function
decorated_with_str = top_decorator ( 'Logging for function passed from outside : ' )
# Now Pass original function to decorate ( compute_sum_2 )  to the above variable  and get the wrapper function back.
decorated_compute_sum_2 = decorated_with_str (compute_sum_2)


print ( ' ----  Passing string from outside to a decorator  ---- ' )
sum = decorated_compute_sum_2 (3,5)
print ( ' Sum = {}'.format (sum) )

# OUTPUT
# ----  Passing string from outside to a decorator  ----
#Logging for function passed from outside :  compute_sum_2
# Sum = 8

# so we can see that we can pass an argument to the decorator



##### Writing the flow in the form it is typically used -> 

@top_decorator ( ' Logging for passed from outside the standard way ' )
def compute_sum_3 (a,b):
	[ i for i in range (9999999) ]
	return (a+b)

print ( ' ----  Passing string from outside to a decorator in the standard way  ---- ' )
sum = compute_sum_3 (3,5)
print ( ' Sum = {}'.format (sum) )


# This way we can even pass a function to top_decorator which we want to be executed before / after the original function.
# So a decorator can act as a general function executor ( accepting functions at various nested levels and executing them in the flow



## Conclusion :
# Decorators can also accept arguments. They must be nested in a function further.

