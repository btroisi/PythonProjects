#Brandon Troisi
#4/5/16
#grid.py

import sys
import turtle 
import lsystem as ls
import turtle_interpreter as ti

def main():
	'''
	Draws a 3 by 3 grid of trees. From left to right, the number of iterations
	of the L-system goes from 1 to 3 and from top to bottom, the angle of the L-system is 
	22, 40, and 60.
	'''
	
	my_lsys = ls.init()
	ls.setBase( my_lsys, 'F' )
	ls.addRule( my_lsys, ['F','F FF-[-F+F+F]+[+F-F-F]'] )
	'''
	Creates an L system that can draw a tree.
	'''
	
	x=-400
	y0=100
	for i in range(1,4):
		x+=200
		turtle.up()
		turtle.goto(x,y0)
		turtle.down()
		for a in (22,40,60):
			if a==22:
				y=y0
			else:
				y+=-150
			turtle.up()
			turtle.goto(x,y)
			turtle.down()
			turtle.setheading(90)
			lstr = ls.buildString( my_lsys, i)
			ti.drawString(lstr, 5, a)
	ti.hold()

						
if __name__=='__main__':
	main()