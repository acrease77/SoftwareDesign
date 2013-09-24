"""Solution to an exercise in Think Python.

Author: Alexander Crease
"""
def grid_print(x,y):
	print ' + - - - -'*x,'+'
	print ' |        '*x,'|'
	print ' |        '*x,'|'
	print ' |        '*x,'|'
	print ' |        '*x,'|'
	if y-1<=0:
		print ' + - - - -'*x,'+'
	else:
		grid_print(x,y-1)
		
grid_print(2,2)

grid_print(4,4)
