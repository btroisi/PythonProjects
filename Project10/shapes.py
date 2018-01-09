#Brandon Troisi
#4/13/16
#shapes.py
#version2

import turtle_interpreter as ti

class Shape:
	'''
	Represents a shape that can be drawn in turtle
	'''

	def __init__(self, distance = 100, angle = 90, color = (0,0,0), istring = ' ',
	style='normal',jitterSigma=2,width=1,dotSize=10):
		'''
		Initializes distance, angle, color, and the string from which to draw the shape
		'''
		self.distance=distance
		self.angle=angle
		self.color=color
		self.string=istring
		self.style=style
		self.jitterSigma=jitterSigma
		self.width=width
		self.dotSize=dotSize
		
	def setStyle(self, style):
	    self.style=style
	    
	def setJitter(self, jitterSigma):
	    self.jitterSigma=jitterSigma
	    
	def setWidth(self, width):
	    self.width=width
	    
	def setDotSize(self, dotSize):
		self.dotSize=dotSize
		
	def setColor(self, c):
		''' Sets the color of the turtle'''
		self.color=c
		
	def setDistance(self, d):
		'''Sets the distance'''
		self.distance=d
		
	def setAngle(self, a):
		'''Sets the angle for the turtle to turn'''
		self.angle=a
	
	def setString(self, s):
		'''Sets the string from which to draw the string'''
		self.string=s
		
	def draw(self, xpos, ypos, scale=1.0, orientation=0):
		'''Draws the shape at (xpos,ypos) at scale scale and orientation orientation'''
		interp=ti.TurtleInterpreter()
		interp.place(xpos,ypos,orientation)
		interp.setStyle(self.style)
		interp.setJitter(self.jitterSigma)
		interp.width(self.width)
		interp.color(self.color)
		interp.drawString(self.string,scale*self.distance,self.angle)
		
		
class Square(Shape):
	'''Represents a square'''
	
	def __init__(self, distance=100, color=(0,0,0)):
		'''Initializes the distance, angle, color, and string necessary to draw a square'''
		Shape.__init__(self, distance, 90, color, 'F-F-F-F')
		
class Triangle(Shape):
	'''Represents a filled in triangle'''
	
	def __init__(self, distance=100, color=(0,0,0)):
		'''
		Initializes the distance, angle, color, and string necessary to draw 
		a filled in triangle
		'''
		Shape.__init__(self, distance, 120, color, '{F+F+F+}')

class TriangleU(Shape):
	'''Represents a triangle that is not filled in'''

	
	def __init__(self, distance=100, color=(0,0,0)):
		'''
		Initializes the distance, angle, color, and string necessary to draw a
		triangle not filled in
		'''
		Shape.__init__(self, distance, 120, color, 'F+F+F+')
		
class Hexagon(Shape):
	'''
	Represents a filled in hexagon
	'''
	def __init__(self, distance=100, color = (0.5,0.4,0.3)):
		'''
		Initializes the distance, angle, color, and string necessary to draw a 
		filled in hexagon
		'''
		Shape.__init__(self, distance, 60, color, '{F-F-F-F-F-F}')
		
class Trapezoid(Shape):
	'''Represents a filled in trapezoid'''
	def __init__(self, distance=100, color = (0.4,0.4,0.3)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a filled in trapezoid
		'''
		Shape.__init__(self, distance, 60, color, '{FF++F+F+F}')
		
class Parallelogram(Shape):
	'''Represents a filled in parallelogram'''
	def __init__(self, distance=100, color = (0.5,0.6,0.7)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a filled in parallelogram
		'''
		Shape.__init__(self, distance, 60, color, '{FF--F-FF--F-}')

class Rectangle(Shape):
	'''Represents a filled in rectangle'''
	def __init__(self, distance=100, color = (0.5,0.6,0.7)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a filled in rectangle
		'''
		Shape.__init__(self, distance, 90, color, '{FF-F-FF-F-}')



		
def test():
	'''
	Draws a red outlined square at (0,0) with distance 67.5 oriented at 0, 
	a black trapezoid at (-30,0) with bottom base 132 and top base 66 oriented at 0.
	Draws yellow hexagon at (20,130) of distance 72 oriented at 90. Draws two 
	parallelograms, the green one is at (-31,-71) oriented at 90 with the bottom 
	base of a distance 70 with other sides a distance 35. The blue parallelogram is at 
	(69,71) with the same size and orientation as the previous one. Draws two triangles 
	with distance 66 oriented at 60. The purple one is at (-30,0) and the orange one is
	at (103,0). Draws a gray rectangle at (-200,150) oriented at 45 degrees with the 
	length 160 and width 80. 
	
	'''
	square1=Square()
	square1.setDistance(90)
	square1.setColor('Red')
	square1.draw(0,0,0.75,0)
	
	hex1=Hexagon()
	hex1.setDistance(80)
	hex1.setColor('Yellow')
	hex1.draw(20,130,0.9,90)
	
	trap1=Trapezoid()
	trap1.setDistance(110)
	trap1.setColor('Black')
	trap1.draw(-30,0,0.6,0)
	
	para1=Parallelogram()
	para1.setDistance(50)
	para1.setColor('Green')
	para1.draw(-31,-71,0.7,90)
	
	para2=Parallelogram()
	para2.setDistance(50)
	para2.setColor('Blue')
	para2.draw(69,-71,0.7,90)
	
	tri1=Triangle()
	tri1.setDistance(110)
	tri1.setColor('Purple')
	tri1.draw(-30,0,0.6,60)
	
	tri2=Triangle()
	tri2.setDistance(110)
	tri2.setColor('Orange')
	tri2.draw(103,0,0.6,60)
	
	rect1=Rectangle()
	rect1.setDistance(100)
	rect1.setColor('Gray')
	rect1.draw(-200,-150,0.8,45)
	
	
	
	
	raw_input('Press enter to exit')


if __name__=='__main__':
	test()
	
		

		