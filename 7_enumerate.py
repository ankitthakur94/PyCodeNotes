### OBJECTIVE ###
# enumerate function usage
# Basically provides a counter while iterating on an iterator.
# Outputs a tuple (index_counter, element_from_iterable) 

example = [ 'ankit' , 'karan' , 'aniket' , 'madhur' , 'vishu' ]

print ( ' ---------- Using traditional method ------ ' )
## Below is the traditional way of implementing a counter for a list.
for i in range(len(example)):
		print (i, example[i])
		#print (<index> , element@index)


# To solve the above problem, use enumerate.
print ( '---------- using enumerate ----------- ' ) 
for (index, value) in enumerate(example) :
	print (index, value)


# Also can use list comprehension to shorten this example
[ print (index, value) for (index, value) in enumerate(example) ] 


print ( ' ------- Enumerating over a dict --------- ' )
# Enumerating over a dict gives a tuple of (index , key)
example_dict = { 'p1 ' : 'ankit' , 'p2' : 'karan' , 'p3' : 'aniket' , 'p4' : 'madhur' , 'p5' : 'vishu' }

for (index, key) in enumerate(example_dict):
	print (index, key)
	## since this is a dictionary, the order of print will not be the same as order of insertion.


## CONCLUSION ####
# 1. whenever u want a counter for a loop for any iterable, use enumerate.
################
		

