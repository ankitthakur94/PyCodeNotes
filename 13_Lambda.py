#############################################################
## Objective :
#############################################################
#  Explore lambda functions / map / filter / reduce
#############################################################


#############################################################
# Theory
#############################################################
# Lambdas a are used to create short anonymous functions.
# They are present o support functional programming
# In functional programming,  functions are passed to other functions.
    # Ex : in Tkinter the Click function accepts another function. This will be executed when click is performed.
# In python there are 2 ways to create functions :
#   1) def          2) lambda
#############################################################


#############################################################
# General syntax :
#############################################################
# <optional variable name> = lambda <arg1> , <arg2> ,.. <argn> : <return expression>
# Ex :  lambda x,y : x + y
#############################################################


add_func = lambda x,y : x + y
sub_func = lambda x,y : x - y


#############################################################
# Map
# Takes in a list and a function and applies that function on all the elements of that list and returns the modified list
# Function to be passes can be a lambda function defined there itself, a lambda function variable and a normal python function.
# Syntax :
#   new_list = list ( map ( <func> , <orig_list> ) )
# Works also for set / tuples
#############################################################

num = list (range(1,10))
print (' Original list ' , num)

square_func = lambda x : x*x
new_nums_list = list(map(square_func, num))
print ( ' New list ', new_nums_list)


#############################################################
# Filter
#############################################################
#  Used to filter out some elements from a list
# Takes in a list and a function returning a bool.
# Applies the function to all the elements on the list
# Returns a new list having elements which satisfy criteria (from function)
# Syntax :
#   new_list = list ( filter ( <func> , <orig_list> ) )
# Works also for set / tuples
#############################################################

# Using a closure to return a function
def max_value (max) :

    def is_greater_than (x) :
        if (x > max) :
            return True
        else :
            return False

    return is_greater_than


is_greater_than_20 = max_value(20)

filtered_list = list ( filter ( is_greater_than_20, new_nums_list))
print ( ' filtered_list  : ' , filtered_list)




#############################################################
# Reduce
#############################################################
# Accepts a list and a function and returns a single value
# The interface of the function should be such that it accepts 2 argumets and returns a single value
# reduce applies the function on first 2 elements of the list, then applies the func to the result and 3rd element and so on.
# f (  f ( f (e1, e2) , e3 ) , e4 )  .. and so on.
#############################################################

## Example : Multiply all elements in a list

num = list (range(1,10))
from functools import reduce
result = reduce ( (lambda x,y : x*y) , num)
print ( ' result :  ', result )


#############################################################
## Conclusion :
#############################################################
# Use lambdas to create small anonymous functions
# They are present to support  functional programming in python
# map : applies a function to all elements in a list and returns a new list
# filter : applies a function to all elements and returns a new list with only those elements for this function returned true
# reduce : not recommended to use this.

# In many scenarios map / filter etc  can also be implemented by list comprehension also
#############################################################








