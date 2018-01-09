#Brandon Troisi
#2/12/15

import shapelib
import random
import turtle

'''
	This imports all of the functions defined in the shapelib file.
	One function includes the rectangle function, 
	which draws rectangles of various sizes and at various locations.  
	Another function imported from the shapelib file is the triangle function, 
	which draws an equilateral triangle of various sizes and at various locations. 

	the light function which draws a yellow circular light. All of these
	functions were imported into the function drawLighthouse.
	 
'''

def sky(x,y,width,height):
		shapelib.rectangle(x,y,width,height)
	
'''
	Draws the outline of sky by drawing a rectangle of 400 by 400 with lower left hand 
	corner starting at coordinates (-100,-100)
'''
	
def coast1():
	'''
	This draws a mountain range
	'''
	
	turtle.begin_fill()
	turtle.color("sky blue")
	sky(-350,-350,800,800)
	'''
	This is what fills the rectanglular sky blue
	'''
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color("blue")
	shapelib.rectangle(-400,-400,800,300)
	turtle.end_fill()
	for i in range (30):
		'''
		Draws a mountain range by drawing 30 triangular mountains of random size from
		range 20 to 100 pixels and at random coordinate ranging from (-400,-400) 
		to (100, 100)
	
		'''
		turtle.begin_fill()
		turtle.color("green")
		shapelib.triangle(random.randint(-400,200),random.randint(-100,100)
		,random.randint(30,200))
		turtle.end_fill()
		
	
	
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color("yellow")
	shapelib.circle(200,250,20)
	'''
	This draws a sun at the upper right hand corner of the sky. 
	'''
	turtle.end_fill()
	turtle.up()
	turtle.forward(100)
	
def coast2():
	turtle.begin_fill()
	turtle.color("tan")
	shapelib.rectangle(-350,-350,700,150)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color("blue")
	shapelib.rectangle(-350,-200,700,150)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color("sky blue")
	sky(-350,-50,700,700)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color("gray")
	shapelib.rectangle(210,-50,100,150)
	turtle.end_fill()
	shapelib.drawLighthouse(240,100,30,40,0.8)
	turtle.begin_fill()
	turtle.color("yellow")
	shapelib.circle(-220,175,50)
	turtle.end_fill()
	turtle.up()
	turtle.forward(-100)
	
	
	
coast2()


	


'''
shapelib.drawLighthouse(-50,-100,30,40,1.0)
shapelib.drawLighthouse(50,100,50,60,0.3)
shapelib.drawLighthouse(100,50,70,80,0.5)
'''


raw_input('Press enter to exit')