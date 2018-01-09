#Brandon Troisi
#4/13/16
#shapes.py
#version3

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
	
	def setRoll(self, r):
		'''Sets the roll'''
		self.roll=r
		
	def setYaw(self, y):
		'''Sets the yaw'''
		self.yaw=y
	
	def setPitch(self, p):
		'''Sets the pitch'''
		self.pitch=p
		
	def setString(self, s):
		'''Sets the string from which to draw the string'''
		self.string=s
		
	def draw(self, xpos, ypos, scale=1.0, orientation=0,roll=0,pitch=0,zpos=0):
		'''Draws the shape at (xpos,ypos,zpos) at scale scale and orientation orientation'''
		interp=ti.TurtleInterpreter()
		interp.place(xpos,ypos,orientation,roll,pitch,zpos)
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
		
class cube(Shape):
	'''Represents a cube'''
	def __init__(self, distance=10, color = (0.5,0.6,0.7)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a cube
		'''
		Shape.__init__(self, distance, 90, color, 'F+F&F+F+F&F&F&F+F+F&F&F+F+F&F+F')

class ocube(Shape):
	'''Represents an octagonal box'''
	def __init__(self, distance=10, color = (0.5,0.6,0.7)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a cube
		'''
		Shape.__init__(self, distance, 45, color, 'F+F+F+F+F+F+F+F+F+(90)&F(90)^F+F+F+F+F+F+F+F+F+F[(90)^F]+F[(90)^F]+F[(90)^F]+F[(90)^F]+F[(90)^F]+F[(90)^F]+F[(90)^F]+F[(90)^F]')
	


class monument(Shape):
	'''Represents a monument with tall rectangular base and prism shaped top'''
	def __init__(self, distance=10, color = (0.5,0.6,0.7)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a cube
		'''
		Shape.__init__(self, distance, 90, color, 'F+(90)(5)F+F+&F(90)^(90)(5)F(90)^F+F+F+F(90)+F^(5)F(90)+F^F+(5)F(-5)F^F+[F+F+F+[F(135)+(45)^F(90)&F](45)+(45)^F(90)&F]')
 

class diamond(Shape):
	'''Represents a diamond'''
	def __init__(self, distance=10, color = (0.5,0.6,0.7)):
		'''
		Initializes the distance, angle, color, and string necessary 
		to draw a diamond
		'''
		Shape.__init__(self, distance, 90, color, '[F+F+F+[F(135)+(45)^F(90)&F](45)+(45)^F(90)&F]-(180)&[F+F+F+[F(135)+(45)^F(90)&F](45)+(45)^F(90)&F]')	 



		
def test():
	'''
	Draws monument with jitter style of size 90 at (200,-150,0) octagonal box
	of size 100 at (-200,-200,0) with normal style, a cube of size 100 with normal style
	at (-200,100,0), and a diamond of size 100 with jitter3 style at (-350,250,0).Alhough
	it is not necessary to include 4 zeros after the scale parameter when the draw
	function was called, I wanted to be sure that the roll, pitch, z value,
	and orientation were 0 without having to scroll up to the draw funciton to check its
	default values.
	
	'''
	
	
	monument1=monument()
	monument1.setDistance(10)
	monument1.setStyle('jitter')
	monument1.draw(200,-150,9,0,0,0,0)
	
	oct1=ocube()
	oct1.setDistance(10)
	oct1.draw(-200,-200,10,0,0,0,0)
	
	cube1=cube()
	cube1.setDistance(10)
	cube1.draw(-200,100,10,0,0,0,0)
	
	d=diamond()
	d.setStyle('jitter3')
	d.setDistance(10)
	d.draw(-350,250,10,0,0,0,0)
	
	
	
	
	
	raw_input('Press enter to exit')


if __name__=='__main__':
	test()
	
		

		