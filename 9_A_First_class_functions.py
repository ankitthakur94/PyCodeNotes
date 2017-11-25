######################################################
## OBJECTIVE ###
######################################################
#To explore what are first-class functions and what are higher order functions.
#
# -> First class functions :
#	 - A programming language is said to have first class functions if the functions can be treated like first-class citizens.
#	 	i.e.
#           Functions can be :
#	 	- Used as parameters to other functions
#		- Assigned to variables
#		- passed as return values from other functions (CLOSURES)
#		- Stored in data structs such as lists/tuple etc.
#		- If a function accepts a functions as an arguemnt, as also returns a function < (DECORATOR)
#
#		in general  if the functions can be treated as normal objects like int / str etc.
#
#	- Since first-class functions are a concept to language,
#		In python all functions are first class functions.
#	
#
#- > Higher order functions :
#	- A function 
#		- accepting a function as argument
#		( This is relatvely simple to understand)
#	or
#		- Returning a function as return value.
#		( A bit tricky )
#	is a higher order function.
######################################################


######################################################
# Assigning a function to a variable.
######################################################

def square (n):
	return n*n


sq_result = square(5)  	# This calls and executes the function. Retunrs square of 5 i.e 25.
sq_func = square	# This does not call the funcion. Just assigns the function name to a variable, making that variable callable like the original function.

print (sq_result)
## OUTPUT -> 25 as expected

print (sq_func)
## OUTPUT -> A function object

print (sq_func(5)) 	# Calls the variable sq_func like a function.
## OUTPUT -> 25
######################################################



######################################################
# Passing a function as an argument to another function ( higher order function)
######################################################

## A higher order function acceptiong a function as an arguemnt.
def transform_list(func_to_apply, list_):
	''' Apply a function to all the elements of a list and return a new list . 
	I am an higher order function since i accept a function as arguemnt.''' 
	new_list = []
	for i in list_:
		value = func_to_apply(i)
		new_list.append(value)
	return new_list


orig_list = [1,2,3,4,5]
# Call the higher order function with a funcion and list.
squared_list = transform_list ( square, orig_list )
print (squared_list) 

## We can pass any function (like here square ) to the higher order function.
## Note that square function is written without (), since pass square() will execute the function and make no sense.

######################################################



























