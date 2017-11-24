a = [2,4,6,8]
b = [1,3,5,7]
c = ['a' , 'b', 'c' , 'd']

############################################################
## Zips up the contents of the 3 lists element-by-element and stores them in i,j,k
############################################################
print ( ' -------- Standard zip on lists ------------- ' )
for (i,j,k) in zip(a,b,c):
	print (i,j,k)
####OUTPUT -> 
# 2 1 a
# 4 3 b 
# 6 5 c
# 8 7 d
############################################################



############################################################
## Here 'i' will a 3-tuple. (<element_of_a> , <element_of_b> , <element_of_c>)
############################################################
print ( ' ----------- zip returning a tuple -------------- ' )
for i in zip(a,b,c):
	print (i)
####OUTPUT -> 
# (2, 1, 'a')
# (4, 3, 'b')
# (6, 5, 'c')
# (8, 7, 'd')
############################################################



############################################################
## If the number of elements in lists to zip are unequal, then only minimum common number of elements will be zipped.
############################################################



############################################################
## Zip on other iterables.
############################################################
print ( ' ----------- zipping sets --------- ' )
a = {2,4,6,8}
b = {1,3,5,7}
c = {'a' , 'b', 'c' , 'd'}


for (i,j,k) in zip(a,b,c):
	print (i,j,k)

####OUTPUT ->  Since we are iterating on set, order of insertion is not the same as order of print.
# 8 1 a
# 2 3 c
# 4 5 d
# 6 7 b
############################################################



############################################################
## Zip on mixed iterables works fine as well.
############################################################
print ( ' ----------- zipping list - set - tuple --------- ' )
a = [2,4,6,8]
b = {1,3,5,7}
c = ('a' , 'b', 'c' , 'd')


for (i,j,k) in zip(a,b,c):
	print (i,j,k)

####OUTPUT ->  Since we are iterating on set, order of insertion is not the same as order of print.
# 2 1 a
# 4 3 b
# 6 5 c
# 8 7 d
############################################################


############################################################
## CONCLUSION ##
############################################################
#1. Zip can be called to zip various iterables (list/tuple/set) element-by-element.
#2. If number of elements in itrables are unequal, first minimum number of elements are zipped. Rest not taken into account.
#3. Mixed iterables can also be zipped. 
############################################################

