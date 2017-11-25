####################################################
# OBJECTIVE :  <Recommended to read the first class function tutorial first.>
# 1.) TO discuss closures
# 2.) Closure vs classes
####################################################


####################################################
# Closure : 
# A function returning another function which was defined in it.
# Return a function without (), if () are added at the end of a function name, that function will be evaluated there itself.
####################################################


def outer_func(greetings):  			# A higher order function (HOF) returning another function.
	greetings_str = greetings 		# A local variable of HOF assigned to argument.	
	def inner_func(name):			# defining an inner function
		print (greetings_str, name)	# Body of inner function.
	return inner_func			# Return inner function from outer function. 
	# Note that inner_func without the () is retunred. If () are written, it will evaluate the inner function here itself.

## Call outer function 
f1 = outer_func('Hello There!')	#f1 here is now a function variable bound to 'inner_func'
f1( 'Ankit' ) 			#Calling f1 calls the inner_function, in whatever state it was.

#In closures the inner function
#	1. Can access the variables of outer function.
#	2. Remembers the state of outer function (i.e variables local to outer function are remembered)
# can nest any number of inner functions.
#	3. Can't return a function which is defined outside the outer func. Can only pass a func defined inside the outer func()
#		Since inner func needs to know the variables local to outer func, it needs acess to them.
#		If the func() was written outside of outer func() we will have to pass those variables as arguments.
#		That is not possible because functionality of inner func() is not affected by arguments / varibales of outer func()

####################################################
## Use case :
####################################################
#	1.  In outer function, use can say that i want this html tag to be associated. (pass the tag as a string argument while calling outer function.
#			Since inner function will remember the tag string, pass another string while calling inner function, on which tag is to be inserted.
#	2. Outer function will accept arguments that should be constant for the calls to subsequent inner functions.
#	3. Inner functions should accept different arguments on which those constant 'things' have to be applied.

# Another use case : 
# Call outer function to form a linear equation
# Call inner function to solve the eqn. for various values of x
def form_linear_eqn (a,b):
	def solve_eqn_for_x (x):
		print ( ' Result : ' , a*x + b ) 
	return solve_eqn_for_x 

eqn = form_linear_eqn (3,2)
eqn(2)
eqn(3)
eqn(4)
####################################################


####################################################
## Closure vs classes
####################################################
#The main idea of closure is that inner function remembers the state of variables in outer function.
#but
#this can also be achieved using classes. 
#Which is preferrable.

#Classes can be a bit slow, closures fast.
#Lesser code has to be written for closure
#Classes are more flexible and scalable.
####################################################

