#Brandon Troisi
#4/20/16
#turtle_interpreter.py
#version4

import turtle
import random
import sys

class TurtleInterpreter:
	'''
	Contains all the functions necessary to interpret turtle commands from a string
	'''

	initialized=False

	def __init__(self, dx=800, dy=800 ):
		'''Initializes the turtle'''
		self.style = 'normal'
		self.jitterSigma = 2
		
		if TurtleInterpreter.initialized:
			return
		TurtleInterpreter.initialized = True
		turtle.setup()
		turtle.tracer(False)
		self.dotSize=5
	
	def setStyle(self, s):
		'''Sets the style for which the turtle should draw the object'''
		self.style = s
		
	def setJitter(self, j):
		'''Sets the jitter for which the turtle should draw each line in a shape'''
		self.jitterSigma = j
		
	def setDotSize(self,dotSize):
		'''Sets the dotsize for when you want to draw a line with dotted circles'''
		self.dotSize=dotSize
		
	def forward(self, distance):
		'''Tells the turtle how to draw something depending on the style called'''
		if self.style == 'normal':
			'''If the style is normal, turtle draws the shape normally'''
			turtle.forward(distance)
			
		if self.style == 'normal1':
			'''
			If the style is normal1, turtle draws the shape normally, but with
			random line segment widths
			''' 
			
			 
			turtle.forward(distance)
			curwidth=turtle.width()
			turtle.width(curwidth + random.randint(2,5))
			
		
		elif self.style == 'jitter':
			'''
			If the style is jitter, turtle draws line starting at position (x0,y0)
			to a random short distance from the desired destination (xf,yf)
			'''
			(x0,y0)=turtle.position()
			turtle.up()
			turtle.forward(distance)
			(xf,yf)=turtle.position()
			curwidth=turtle.width()
			
			
			jx = random.gauss(0, self.jitterSigma)
			jy = random.gauss(0, self.jitterSigma)
			kx = random.gauss(0, self.jitterSigma)
			ky = random.gauss(0, self.jitterSigma)
			
			turtle.width(curwidth + random.randint(0,2))
			turtle.goto(x0+jx, y0+jy)
			turtle.down()
			turtle.goto(xf+kx, yf+ky)
			turtle.up()
			turtle.goto(xf,yf)
			turtle.width(curwidth)
			turtle.down()
		
		elif self.style == 'jitter3':
			'''
			If the style is jitter3, turtle draws line starting at random short distance
			from intitial position (x0,y0) to a random short distance 
			from the desired destination (xf,yf)
			'''
			for i in range (3):
				(x0,y0)=turtle.position()
				turtle.up()
				jxi = random.gauss(0,self.jitterSigma)
  				jyi = random.gauss(0,self.jitterSigma)
  				turtle.goto( x0+jxi, y0+jyi )
  				turtle.forward(distance)
  				(xf,yf)=turtle.position()
  				curwidth=turtle.width()
  				
  				
  				jxf = random.gauss(0, self.jitterSigma)
				jyf = random.gauss(0, self.jitterSigma)
				kxf = random.gauss(0, self.jitterSigma)
				kyf = random.gauss(0, self.jitterSigma)
			
				turtle.width(curwidth + random.randint(0,2))
				turtle.goto(x0+jxf, y0+jyf)
				turtle.down()
				turtle.goto(xf+kxf, yf+kyf)
				turtle.up()
				turtle.goto(xf,yf)
				turtle.width(curwidth)
				turtle.down()
				turtle.up()
				turtle.goto(x0,y0)
				turtle.down()
			turtle.goto(xf+kxf, yf+kyf)
				
				
				
				
		elif self.style == 'dot':
			'''
			If the style is dot, it draws a line segment as dots. The size of the dots
			depends on user input
			'''
			dotsize=int(raw_input("What would you like the size of the dot to be: "))
			for i in range(int(distance/(4*dotsize))):
				turtle.circle(dotsize)
				turtle.up()
				turtle.forward(4*dotsize)
				turtle.down()
				
		
			
		
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
		{ : fills in shape
		} : ends filling in shape
		R : set color to brightest red possible
		b : set color to black
		s : set color to light blue
		! : decreases width of line by 1 every time until width reaches 1
		( : tells turtle to begin save the value of whatever is called in here and use it to
			go forward or rotate certain angle
		) : Corresponds with (, which tells turtle to stop saving the value of whatever 
			is called in here and use it to go forward or rotate certain angle. For example,
			F(x) tells the turtle to go forward distance x. This makes it so we can change
			the amount to go forward or rotate easily.
		"""
		modstring=''
		modval=None
		modgrab=False
		stack=[]
		colorstack=[]
		
		for c in dstring:
			if c == '(':
				modstring=''
				modgrab=True
				continue
			elif c == ')':
				modval=float(modstring)
				modgrab=False
				continue
			elif modgrab == True:
				modstring+=c
				continue
			if c=='F':
				if modval == None:
					self.forward(distance)
				else:
					self.forward(distance*modval)
			elif c =='+':
				if modval==None:
					turtle.left(angle)
				elif modval!=None:
					turtle.left(modval)
			elif c=='-':
				if modval==None:
					turtle.right(angle)
				elif modval!=None:
					turtle.right(modval)
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
			elif c == '{':
				turtle.fill(True)
			elif c == '}':
				turtle.fill(False)
			elif c == 'R':
				turtle.color('red')
			elif c == 'b':
				turtle.color('black')
			elif c == 's':
				turtle.color('lightblue')
			elif c == '!':
				if modval == None:
					w=turtle.width()
					if w>1:
						turtle.width(w-1)
				else:
					turtle.width(modval)
			modval=None
		turtle.update()
	
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
	
	def width(self,w):
		'''
		Sets the width of the line turtle draws to w
		'''
		turtle.width(w)
	
		 