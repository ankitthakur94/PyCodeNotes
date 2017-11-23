#### Objective
# 1. Explore various ways to concat strings
#	1.A) Using + 
#		- concat_str = string1 + string2 + string 3
#		- Most readable, Less efficient, Creates copies, Not-scalable, Not-Recommended
#
#	1.B) Using ,
#		print ( string1, string2, string3)
#		- Can be used in print
#		- Can use it casually
#		- Quite readable.
#
#	2.C) Using Join
#		 General Syntax : <string_to_join_with>.join( <any_iterable> )		
#		 Common Use-case Syntax : <string_to_join_with>.join( [ string1, string2, string3] )
#		- Quite efficient, Scalable, Recommended (specially to concat 2/more stringso)
#		- Join can be used to join any iterable with a string b.w each element.
#
# 2. String formatting
#	- Recommended way to string formatting is to use "<string>".format(<arguments>)
################	


names = ['Ankit', 'Karan', 'Madhur', 'Aniket' ]

print ( ' ------- Regular String Concatenation using +  <Not Recommended> ---------' )
for name in names:
	print ( 'Hello , ' + name)

print ( ' -------- String Concatenation using Join. --------- ' )
for name in names:
	print ( ' , '.join(['Hello', name]))

print ( ' -------- Print a list without for loop using join. --------' ) 
print (' ,'.join(names))


print ( ' ---- Example for string formatting (In the right way)------ ' ) 
who = 'Ankit'
how_many = '12'
what = 'Apples'
print ( ' {0} bought {1} {2} today !'.format (who,how_many,what) )

