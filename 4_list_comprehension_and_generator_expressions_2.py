input_list = [1,2,5,6,8,10,15,27,89]

## Define a function which retunrs true if the number is divisible by 5.
def div_by_five (n):
	is_div = False
	if n % 5 == 0:
		is_div = True
	return is_div


## Generator expression to get the filtered list with numbers which are divisble by 5.
# Returns a generator object ( which can be later iterated). 
filtered_list_gen_expr = ( i for i in input_list if div_by_five (i) )

## The above generator expression is equivalent to  the below function and its call.:
def get_filtered_list_generator(inp_list):
	for i in inp_list:
		if (div_by_five (i)):
			yield i

## Calling an generator function to get the generator object.
filtered_list_generator = get_filtered_list_generator (input_list)

# So (filtered_list_generator) && (filtered_list_gen_expr) both are generator objects which are similar to iterator (only more than them).
print ( ' type (filtered_list_gen_expr ) : ' ,  type (filtered_list_gen_expr) )
print ( ' type ( filtered_list_generator) : ' , type (filtered_list_generator)) 
## OUTPUT -> Generator Objects.


# So a generator expression (like a generator function) doesn't actually call the function, but only returns a generator object. 
# By iterating on this generator object we can now call the function (inside generator expression) once for each iteration.
# On the other hand, if this was list comprehension, it would actually run the function for every iteration over there itself, and produce the output
filtered_list_by_lst_comprehension = [ i for i in input_list if div_by_five (i) ]  ## List comprehension.
## The above object is a list containing output of the list comprehension.

## Use of list comprehension is not only restricted to creating a list. 
## Instead we can call any function on an iterable in list comprehension and the entire calculation will be done there itself.
print ( ' ########## Printing via list comprehension ########### ' ) 
[ print (i) for i in filtered_list_gen_expr ] 


####### IMPORTANT NOTE ############
## DIFF :In a list comprehension, the entire loop computation is peformed there itself. 
#but in 
#generator expression, no computation starts as a gen_exp is created, instead every iteration is called once when the generator expression object is iterated upon.
## As a result it is recommended to use list comprehension if we want to iterate on a huge data set (Ex : Infinite scrolling in facebook). 
##	No memory is occupied in generator expression.
###################################


print ( ' ########## Printing via list comprehension ########### ' ) 
[ print (i) for i in filtered_list_by_lst_comprehension]  ## Will actuall execute the print function here only and wil print the list.
# vs
print_obj =  ( print (i) for i in filtered_list_by_lst_comprehension ) ## Will not actually do any computation, will just return a generator object. Iterating on that object will then call print (i) function 1-by-1 for each iteration element.
# So to actually print from the above generator expression we will have to iterate on gen_exp_object.

print ( ' ########## Printing via generator expression ########### ' ) 
for i in print_obj:
	i 	## Mind that since 'i' is already print (i) So we do not need to call print (i) here again.


# In list comprehension, we can call any function for each element of an iterable object.(like print is called here)




################ NESTED LOOPS IN LIST COMPREHENSION ###############
print ('################ NESTED LOOPS IN LIST COMPREHENSION ###############')
for i in range(4):
	for ii in range(2):
		print (i,ii)

# The above nested for loop is eq. to :
[[ print (i, ii) for ii in range(2) ] for i in range(4) ]
## TO write the nested list comprehension, go backwards. Replace the ':' of nested for loops by ']' and balance the brackets.

## Creating list of tuples via this mechanism.
# Output > [  [(0,0) , (0,1)]  ,  [(1,0) , (1,1)] , [(2,0) , (2,1)]  .. and so on. ]


####### METHOD 1 : Creating a list of tuples.
xyz_2_lst_comprehension = [ (i, ii) for ii in range(2)  for i in range(4) ]
# ^ is same as V
xyz_2 = [ ] 
for i in range(4):
	for ii in range(2):
		xyz_2.append((i,ii))
# Output > [  (0,0) , (0,1) , (1,0) , (1,1), (2,0) , (2,1)  .. and so on. ] # A simple list of tuples.
# Op_syntx [  (tuple), (tuple) , (tuple) .. ]


######### METHOD 2 : Creating a list of list of tuples ( Notice the difference in [] brackets 
xyz_3_lst_comprehension = [ [(i, ii) for ii in range(2)]  for i in range(4) ]  # Fist a list of tuples is created for range(2) loop. then this list is appended into another list formed by range(4) loop.
# ^ is same as V
xyz_3 = [] 
for i in range(4):
	xyz_3_internal = []
	for ii in range(2):
		xyz_3_internal.append((i,ii))
	xyz_3.append(xyz_3_internal)
# Output > [  [(0,0) , (0,1)]  ,  [(1,0) , (1,1)] , [(2,0) , (2,1)]  .. and so on. ]
# OP_syntx [  [ list_of_tuple : (tuple), (tuple) ] , [ list_of_tuple : .. and so on ] 






################ NESTED LOOPS IN GENERATOR EXPRESSION ###############
print ( '################ NESTED LOOPS IN GENERATOR EXPRESSION ###############' )


###### METHOD 1: return a tuple every time generator expression is iterated in for loop.
xyz_gen_exp_1 = ( (i, ii) for ii in range(2)  for i in range(4) )
for i in xyz_gen_exp_1 :
	print (i) ### i here is a tuple (i,ii) of the generator expression.



####### METHOD 2 : Confusing
xyz_gen_exp_2 = ( ( (i, ii) for ii in range(2) )  for i in range(4) )
for i in xyz_gen_exp_2 :
	for j in i :
		print (j)





##############################################################################
################################### CONCLUSION ###############################
##############################################################################

#1. List Comprehension 
#	1-A) List comprehension is a short way to generate list. []
#	1-B) Code in [List Comprehension] is executed in that line itself and output if asked is stored in a list.
#	1-C) Any function can be called on an iterable object in a list function syntax ( Ex : [ print (i) for i in <iterable>  ] )
#	1-D) Nested for-looping can also be done in list comprehension. Placements of [brackets] will matter a lot. Introducing a [bracket] adds a 'append' of the list and leads to creating of nested list.
#
######
# ## 2. Generator Expression () ###
#	2-A) Generator expression is a shory way to write a generator function code.
#	2-B) Code in gen_exp is not executed there itself. An generator_object is retunred. It is similat to iterator, only more.
#	2-C) The returned gen_object can then be iterated on, and code inside generator expression is executed once for each iteration.
#	2-D) Can be slower but since no data is stored in memory, it is memory efficient.
#	2-E) Nested for-looping can also be done here. Again placement of (brackets) is important. Placing additional (brackets) will lead to returning of nested generator objects.
#
##############################################################################
##############################################################################
