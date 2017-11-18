
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

