#####################################################
#OBJECTIVE :
#####################################################
#	Decorate a function with arguments and return value.
#####################################################


# We have seen how to decorate a function such that we can do something extra before / after the function execution and not alter the code of the function.




#####################################################
# Lets decorate such a function accepting arguments.
#####################################################



def decorator_func (orig_func):

	# Since we return this wrapper function from the decorator function, its interface should be exactly same as orig_func
	# So we need to accept whatever agruments orig_func was accepting in this wrapper func()
	def wrapper_func(*args, **kwargs):

		print ( ' wrapper executed before original function ' , orig_func.__name__ ) 
		# Execute the orig func with arguments.
		orig_func (*args, **kwargs)
		
	return wrapper_func 


@decorator_func
def add_nums_and_print (a,b):
	print ( ' Adding {} and {} = {} '.format(a,b,(a+b)) )

# Since the wrapper aceepts *args and **kwargs, we can normally call our function 'add_nums_and_print' which is now decorated.
add_nums_and_print (2,3)
add_nums_and_print (132,432)
#####################################################




#####################################################
# Now lets decorate a function which accepts arguments and retunrs a value also.
#####################################################


def decorator_func_2 (orig_func):

	# Since we return this wrapper function from the decorator function, its interface should be exactly same as orig_func
	# So we need to accept whatever agruments orig_func was accepting in this wrapper func()
	def wrapper_func(*args, **kwargs):

		print ( ' wrapper executed before original function ' , orig_func.__name__ ) 

		# Execute the orig func with arguments and also return whatever original function was returning.
		to_return = orig_func (*args, **kwargs)
		
		# This will be returned when the wrapper function will be executed.
		# And wrapper function will the executed when the original function (decorated) will be executed
		return to_return 
		
	return wrapper_func 

@decorator_func_2
def get_average (nums_list):
	sum = 0
	for i in nums_list:
		sum += i
	
	avg = sum/len(nums_list)

	return avg



avg = get_average ([4,6,1,5,8,6])
print ( ' Average : ' , avg )

avg = get_average ([42,423,534])
print ( ' Average : ' , avg )

avg = get_average ([442,454,653])
print ( ' Average : ' , avg )








#####################################################
## Conclusion
#####################################################
# In a decorator function, we return a wrapper function.
# The function which has been decorated with this decorator, when that funcion will be called, internally actually the returned wrapper will be called.
# So the interface (arguments and return value) of wrapper should be exactly same as the original function to be decorated.
#####################################################
