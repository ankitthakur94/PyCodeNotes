### Objective : Introduction to List Comprehension and Generators and Generator Expressions ###


### Generators are functions with a 'yield' statement (Return can also be present)

###############################################################
############  CREATING A FUNCTION TO GENERATE LIST OF NUMS ####
###############################################################

def GetListOfNums (max):
	nums_list = []
	for i in range(max):
		nums_list.append(i)
	return nums_list

nums_list_ = GetListOfNums (5)
print ( " Printing List of nums " ) 
print ( nums_list_ ) 
###############################################################


###############################################################
############  CREATING A LIST COMPREHENSION ###################
###############################################################

## Create a list comprehension
## Use of square brackets is important []. If () are used, it becomes generator expresion.
nums_list = [ i for i in range(5) ]
print ( " Using List Comprehension " ) 
print ( nums_list )

# The statement is a list comprehension and is equivalent to :
nums_list = []
for i in range(5):
	nums_list.append(i)
###############################################################


###############################################################
############  CREATING A GENERATOR FUNCTION ###################
###############################################################

### Define a Generator Function which will generate numbers from 0 to max.
def NumberGenerator (max):
	start = 0
	while (start <= max):
		yield start
		start += 1
	return

### Create a number generator object.
### Function execution will not start right now.
### It will start when a next() function is called on generator_object.
### Function execution pauses as it reaches yield statement and value after that is returned. When the 'next' is again called on generator object, execution continues from the line following yield statement. ( State of the  function like local vars etc. is preserved)
### This helps us avoid saving numbers in memory.
nums = NumberGenerator (5)

print ( ' Printing using Generator Function ' )
for num in nums:
	print ( num ) 
###############################################################




###############################################################
############  CREATING A GENERATOR EXPRESSION  ################
###############################################################

# A generator expression is a short way of creating a generator function ( as shown previosuly )

## Create a generator expression object.
## Now we can iterate on this object
nums_generator = ( i for i in range(5))

print ( " Printing using Generator expression object " ) 
for num in nums_generator:
	print (num)
###############################################################



########################################
############  CONCLUSION ###############
########################################

# List Comprehension is a short way to create a list.
# since a list is created, use this when you need to store elements in the memory.

# Generator Expression is a short way to create generator function.
# An iterable object is created on which we can iterate. 
# Elements are not stored in memory.
########################################
########################################
