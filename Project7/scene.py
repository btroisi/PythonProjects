#Brandon Troisi
#4/5/16
#scene.py

import sys
import turtle 
import lsystem as ls
import turtle_interpreter as ti

def main():
	'''
	Uses L systems to create scene with light blue sky, green grass,
	a sun in the top right corner, and a tree with brown branches.
	'''	
	my_lsys1 = ls.init()
	ls.setBase( my_lsys1, 'F')
	ls.addRule( my_lsys1, ['F', 'FF+F+FF+F+'] )
	lstr1 = ls.buildString( my_lsys1, 1)
	'''
	Creates L-system that represents a rectangle that is twice as wide as it is high.
	Thus, this L-system can draw both a rectangluar light blue sky and green grass since
	this L-system is iterated once.
	'''
	
	turtle.up()
	turtle.goto(-315,-285)
	turtle.begin_fill()
	turtle.down()
	turtle.color('green')
	ti.drawString(lstr1, 310, 90)	
	turtle.end_fill()
	'''
	Draws rectangular green grass starting at (-315,285)
	'''
	
	turtle.up()
	turtle.goto(-315,25)
	turtle.begin_fill()
	turtle.down()
	turtle.color('lightblue')
	ti.drawString(lstr1,310,90)
	turtle.end_fill()
	'''
	Draws rectangular light blue sky starting at (-315,25)
	'''
	
	turtle.up()
	turtle.goto(250,180)
	turtle.begin_fill()
	turtle.down()
	turtle.color('yellow')
	turtle.circle(50)
	turtle.end_fill()
	'''
	Draws sun at (250,180)
	'''
	
	
	my_lsys2 = ls.init()
	ls.setBase( my_lsys2, 'F' )
	ls.addRule( my_lsys2, ['F','F[+F]F[-F][F]'] )
	'''
	Creates new L-system that draws a tree with multiple branches at (0,-225)
	'''
	
	
	lstr2 = ls.buildString( my_lsys2, 5)
	turtle.setheading(90)
	turtle.up()
	turtle.goto(0,-225)
	turtle.down()
	turtle.color("brown")
	ti.drawString(lstr2, 5, 20)
	'''
	Draws the tree with multiple brown branches starting at (0,-225) and
	the L-system that makes up the tree is iterated 5 times. 
	'''
	ti.hold() #holds the screen open until the user clicks or types 'q' 
	
	
	
if __name__=='__main__':
	main()