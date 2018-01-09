#Brandon Troisi
#4/5/16
#extension.py

import turtle
import random
import lsystem as ls
import turtle_interpreter as ti
import better_shapelib as bsl

def main():
	'''
	Imports mountain scene from project 3 and adds three equally sized trees, one with
	red leaves, one with orange leaves, and another one with yellow leaves. 
	The size of the leaves from largest to smallest are red, orange, and yellow.
	From left to right the trees have red, orange, and yellow leaves. 
	The trees are spaced 200 pixels from each other in the x direction. The branches are
	brown.
	'''
	bsl.myOtherScene(0,0,0.8)
	'''
	Draws mountain scene from Project 3 at 0.8 times its original size
	'''
	
	
	my_lsys1 = ls.init()
	ls.setBase( my_lsys1, 'F' )
	ls.addRule( my_lsys1, ['F','F FF-[-F+F+FRB]+[+F-F-FRB]'] )
	'''
	Creates L system that draws tree with red leaves and brown branches
	'''
	
	my_lsys2 = ls.init()
	ls.setBase( my_lsys2, 'F' )
	ls.addRule( my_lsys2, ['F','F FF-[-F+F+FOB]+[+F-F-FOB]'] )
	'''
	Creates L system that draws tree with orange leaves and brown branches
	'''
	
	my_lsys3 = ls.init()
	ls.setBase( my_lsys3, 'F' )
	ls.addRule( my_lsys3, ['F','F FF-[-F+F+FYB]+[+F-F-FYB]'] )
	'''
	Creates L system that draws tree with yellow leaves and brown branches.
	'''
	
	
	lstr1 = ls.buildString( my_lsys1, 2)
	lstr2 = ls.buildString( my_lsys2, 2)
	lstr3 = ls.buildString( my_lsys3, 2)
	turtle.setheading(90)
	x=-400
	for i in (lstr1,lstr2,lstr3):
		x+=200
		turtle.up()
		turtle.goto(x,-80)
		turtle.down()
		turtle.color("brown")
		ti.drawString(i, 5, 20)
	'''
	Draws each tree with red, orange, and yellow leaves in that order with the trees
	spaced 200 pixels apart in the x direction starting at (-400,-80). For each tree,
	the L-system that makes up each tree is iterated 2 times. 
	'''
	
	ti.hold() #holds the screen open until the user clicks or types 'q' 
	
if __name__=='__main__':
	main()