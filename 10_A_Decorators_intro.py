#########################################################
## Objective : <read first class functions and closures tutorial first >
#########################################################
#	Review of closures
#	Why Decorators
#	Implementing and calling a decorator in 2 ways.
#########################################################



#########################################################
# What are decorators.
#########################################################
# A function accpeting a function as an argument and returning another function is a decorator.
# They are used to add some functionality to an already existing function (orig function), without altering the code of original function.
	# Adding functionality can be to add logging / measure execution time  of orig function etc.
#########################################################



#########################################################
## Review of closures 
# Closure : A function returning a function.
#########################################################

def form_linear_eqn (a,b):		## Outer function to create a linear equation of the form ax +b (a,b can be specified through this outer func)
	def solve_for_x (x):		## Once formed, this eqn can be solved for any value of 'x'.
		print (a*x +b)
	return solve_for_x		## returnig the inner function which remembers local variables of outer func (a,b here) 


eqn = form_linear_eqn (4,5) 	# This creates linear eqn 4x + 5 and returns that.
# eqn here is 'solve_for_x' function for which values of 'a' and 'b' have  been fixed.
eqn(2)			# returns 4*2 + 5 = 13
eqn(3)			# returns 4*3 + 5 = 17
#########################################################


print ( ' ----------- ' )


#########################################################
# Intro to Decorators
# Example 1:
#########################################################


## Original function which we want to decorate.
def print_something ():
	print ( ' Hey I am printing something in original function. ' )

# Call original function.
#print_something ()
# Hey I am printing something in original function


# Till here things are normal.

# But what if we want to do something  extra in the original function, without changing the functionality of original function.
# say we want to print something extra before executing the original function.
# For this we use a decorator function.

def decorator_function (original_func):

	def wrapper_function ():
		print ( ' Before executing original function : ' , original_func.__name__ )		# Print the extra something from wrapper.
		print ( ' Printing something extra from decorator\'s wrapper. ' )			# Print the extra something from wrapper
		original_func()										# Now execute the original function.		

	return wrapper_function								# Return the wrapper, waiting to be executed by caller of decorator.


# Pass the original functio 'print_something' to the decorator function.
# It will return a new function, which does what was our objective earlier (i.e print something extra then execute original function)
decorated_print_func = decorator_function (print_something)

# Call the decorated_print_function to execute what was intended.
decorated_print_func ()

## OUTPUT >
# Before executing original function : print_something	> First the print statement inside wrapper function is executed.
# Printing something extra from decorator\'s wrapper. 	> print statement inside wrapper function is executed. 
# Hey I am printing something in original function. 	> The our original function is executed.


# So we have done some extra work before calling our original function, without altering its code.
#########################################################

print ( ' ----------- ' )


#########################################################
# Alternate (recommended and most frequently used) way of adding a decorator to a function.
#########################################################

@decorator_function				# Recommended way to specify a decorator.
def say_hello ():				# Original function to decorate.
	print ( ' Hello There ' )

say_hello  ()					# Call the original function, but now it has been decorated.
## OUTPUT :
# Before executing original function :  say_hello
# Printing something extra from decorator's wrapper.
# Hello There


#  So instead of decorating the 'say_hello' function like the following way V . We have used @decorator_function before the 'say_hello' function.
#decorated_say_hello = decorator_function (say_hello)
#decorated_say_hello ()





#########################################################
 #### CONCLUSION
#########################################################
 # We sew how a simple decorator works.
 # We explore advanced decorators in the next tutorial
#########################################################





