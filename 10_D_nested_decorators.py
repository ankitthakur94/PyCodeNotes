#################################################################
### Objective  :
#################################################################
# See how nested decorators work.
# Why use wraps from functools
#################################################################

def log_decorator (orig_func):

	def log_wrapper (*args, **kwargs):
		print ( ' Logging for function : ', orig_func.__name__ )
		return (orig_func (*args, **kwargs) )

	return log_wrapper

import time
def time_decorator (orig_func):

	def time_wrapper (*args, **kwargs):
		start_at = time.time()
		to_return = orig_func (*args, **kwargs) 
		time_taken = time.time () - start_at
		print ( ' Time Taken for function {} = {} : '.format (orig_func.__name__, time_taken) )
		return to_return

	return time_wrapper

# Decorate the function with 2 decorators.
# decorated_original_func = log_decorator (time_decorator (original_func ))
# No Order of execution of these decorators is most probably alphabetic.
@log_decorator
@time_decorator
def compute_sum_1 (a,b):
	[ i for i in range (9999999) ]
	return (a+b)

print ( ' ----  Using standard way of decorator  ---- ' )
sum = compute_sum_1 (3,5)
print ( ' Sum = {}'.format (sum) )

#OUTPUT  (First time_decorator is executed, then log_decorator 
# Logging for function :  time_wrapper					< But what is this ? Function name should be compute_sum_1		
# Time Taken for function compute_sum_1 = 0.7640435695648193 :
# Sum = 8

# We see that in the log_decorator, function name is being printed as : time_wrapper instead it should be compute_sum_1 
# we now manually write the code of using decorator instead of using @ way

#################################################################
def compute_sum_2 (a,b):
	[ i for i in range (9999999) ]
	return (a+b)

print ( ' ------ Using manual decorator ----- ' )

# The below notations of @ can be translated as :
# @log_decorator
# @time_decorator

# Use time decorator first. time_decorator gets the original function to decorate, so it prints this functions name from within.
time_decorated_compute_sum_2 = time_decorator (compute_sum_2)
# We can see that time_decorated_compute_sum_2.__name__ will give time_wrapper function as output which we pass to log_decorator.

# using log decorator second.
# log_decorator gets an already decorated function (time_wrapper) to decorate. So it does not know about the original function name
time_n_log_decorated_compute_sum_2  = log_decorator (time_decorated_compute_sum_2 )

# Now we can see that log_decorator does not receive the original function as it is. It receives a decorated function which internally is 'time_wrapper'
# So it prints the wrapper function name.
sum = time_n_log_decorated_compute_sum_2 (3,5)
print ( ' Sum = {}'.format (sum) )






#################################################################


## How to get the real name of original function (in our case compute_sum_2) for both the decorators.
## use functools
## from functools import wraps
## and wraps our wrappers in decorators with this wraps.

# Ex  usage of wraps

from functools import wraps

def log_decorator (orig_func):
	
	# Decorate the wrapper so that orig_func.__name__ works correctly  (gives name of original function, even when nested decorators are used).
	@wraps (orig_func)
	def log_wrapper (*args, **kwargs):
		print ( ' Logging for function : ', orig_func.__name__ )
		return (orig_func (*args, **kwargs) )

	return log_wrapper

import time
def time_decorator (orig_func):
	
	# Decorate the wrapper so that orig_func.__name__ works correctly  (gives name of original function, even when nested decorators are used).
	@wraps (orig_func)
	def time_wrapper (*args, **kwargs):
		start_at = time.time()
		to_return = orig_func (*args, **kwargs) 
		time_taken = time.time () - start_at
		print ( ' Time Taken for function {} = {} : '.format (orig_func.__name__, time_taken) )
		return to_return

	return time_wrapper

@log_decorator
@time_decorator
def compute_sum_3 (a,b):
	[ i for i in range (9999999) ]
	return (a+b)

print ( ' ----  Using wraps from functools to get the real function name  ---- ' )
sum = compute_sum_3 (3,5)
print ( ' Sum = {}'.format (sum) )

## OUTPUT 
# ----  Using wraps from functools to get the real function name  ----
# Logging for function :  compute_sum_3							< Correct function name even with nested decorator.
# Time Taken for function compute_sum_3 = 0.8010456562042236 :				< -- here too 
# Sum = 8






#################################################################
# Conclusion :
#################################################################
# Multiple levels of decorators can be nested over 1 function.
# 	@ deco1
# 	@ deco2
# 	def orig_func (..) : ...
# The above decoration is same as :
# docrated_orig_func = deco1 ( deco1 (orig_func) )
# 
# order of executin is alphabetic most probably.
# use wraps from functools to get original function name.
#################################################################


