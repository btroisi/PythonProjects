#Brandon Troisi
#4/6/16
#turtle_interpreter.py
#version 2

import turtle
import random
import sys

class TurtleInterpreter:

    def __init__(self, dx=800, dy=800 ):
        turtle.setup()
        turtle.tracer(False)
        
        
    def drawString(self, dstring, distance, angle ):
		""" 
		Interpret the characters in string dstring as a series
      	of turtle commands. Distance specifies the distance
      	to travel for each forward command. Angle specifies the
      	angle (in degrees) for each right or left command. The list of 
      	turtle supported turtle commands is:
      	F : forward
      	- : turn right
      	+ : turn left
      	[ : save position, heading
      	] : restore position, heading
      	< : saves color
      	> : restore color
      	g : set color to green
      	y : set color to light yellow
      	r : set color to light red
      	B : set color to brown
      	L : draws a filled in semicircular leaf
      	f : fills in shape
      	n : ends filling in shape
      	R : set color to brightest red possible
      	b : set color to black
      	s : set color to light blue
      	"""
		stack=[]
		colorstack=[]
		for c in dstring:
			turtle.tracer(False)
			if c=='F':
				turtle.forward(distance)
			elif c =='+':
				turtle.left(angle)
			elif c=='-':
				turtle.right(angle)
			elif c =='[':
				stack.append(turtle.position())
				stack.append(turtle.heading())
			elif c == ']':
				turtle.up()
				turtle.setheading(stack.pop())
				turtle.goto(stack.pop())
				turtle.down()
			elif c == 'B':
				turtle.color('brown')
			elif c == '<':
				colorstack.append(turtle.color()[0])
			elif c == '>':
				turtle.color(colorstack.pop())
			elif c == 'g':
				turtle.color((0.15,0.5,0.2))
			elif c == 'y':
				turtle.color((0.8,0.8,0.3))
			elif c == 'r':
				turtle.color((0.7,0.2,0.3))
			elif c == 'L':
				turtle.fill(True)
				turtle.circle(distance,180)
				turtle.fill(False)
			elif c == 'f':
				turtle.fill(True)
			elif c == 'n':
				turtle.fill(False)
			elif c == 'R':
				turtle.color('red')
			elif c == 'b':
				turtle.color('black')
			elif c == 's':
				turtle.color('lightblue')
        	     
    
    
    def hold(self):
      """ holds the screen open until the user clicks or types 'q' """

      # have the turtle listen for events
      turtle.listen()

      # hide the turtle and update the screen
      turtle.ht()
      turtle.update()

      # have the turtle listen for 'q'
      turtle.onkey( turtle.bye, 'q' )
      # have the turtle listen for a click
      turtle.onscreenclick( lambda x,y: turtle.bye() )

      # start the main loop until an event happens, then exit
      turtle.mainloop()
      exit()
      
    def place(self, xpos, ypos, angle=None):
    	'''
    	This places the turtle at a certain position (xpos,ypos) and if the value of 
    	angle is not equal to none, the turtle is oriented that angle.
    	'''
        turtle.up()
        turtle.goto(xpos,ypos)
        if angle!=None:
            turtle.setheading(angle)
        turtle.down()
    
	def orient(self, angle):
		'''
		Orients turtle in a certain direction
		'''
		turtle.setheading(angle)
    
    def goto(self, xpos,ypos):
    	'''
    	This moves the turtle to position (xpos,ypos) without drawing anything
    	'''
        turtle.up()
        turtle.goto(xpos,ypos)
        turtle.down()
    
    def color(self, color):
    	'''
    	Sets the color for which the turtle to draw
    	'''
        turtle.color(color)
    
    def width(self, w):
    	'''
    	Sets the width of the line turtle draws to w
    	'''
        turtle.width(w)
    
    def sun(self, x, y, r):
    	'''
    	Creates a yellow circular sun at position (x,y) with radius r
    	'''
    	turtle.fill(True)
    	self.color('yellow')
    	self.place(x,y,0)
    	turtle.circle(r)
    	turtle.fill(False)   
 	
      