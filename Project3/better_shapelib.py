import turtle
import random
import sys

def goto(x,y):
	'''
		This moves the turtle to the position (x,y) without drawing anything>
	'''
	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	print 'goto(): going to ', x, y
	
def rectangle(x,y,width,height,fill,color):
	goto(x,y)
	if fill==True:
		'''
			This draws a rectangle at position (x,y)
			with a width specified by the user(via the parameter width)
			and a height specified by the user (via the parameter height)
			and fill in the rectangle with the color the user specifies 
			(via the color parameter). 
		'''
		turtle.begin_fill()
		turtle.color(color)
		for i in range (2):
			turtle.forward(width) 
			turtle.left(90)
			turtle.forward(height)
			turtle.left(90)	
		turtle.end_fill()
		print 'This draws a rectangle of size', width, height, 'and fills it with', color
	
	elif fill==False:
		'''
			This draws a rectangle at position (x,y)
			with a width specified by the user(via the parameter width)
			and a height specified by the user (via the parameter height)
			without filling the rectangle with any color.  
		'''
		for i in range (2):
			turtle.forward(width) 
			turtle.left(90)
			turtle.forward(height)
			turtle.left(90)
		print 'This draws a rectangle of size', width, height
			
			
def triangle(x,y,length,fill,color):
	'''
		This draws an equalateral triangle of size length 
		length in the turtle and starts drawing the triangle of that size
		at coordinate (x,y). 
	'''	
	goto(x,y)
	if fill==True:
		'''
		This fills the triangle with whatever color the user specifiies
		with the color parameter. 
		'''
		turtle.begin_fill()
		turtle.color(color)
		for i in range (3):
			'''
			This tells the turtle to draw a line of length length
			and rotate 120 degreees countercolcwise.
			This command is repeated 3 times to draw a triangle of size length. 
    		'''
			turtle.forward(length)
			turtle.left(120)
		turtle.end_fill()
		print "This draws a triangle of length", length, "pixels at coordinates", x, y,
		"and fills it", color
	
	elif fill==False:
		'''
		This draws a triangle without filling it in with any color. 
		'''
		for i in range (3):
			turtle.forward(length)
			turtle.left(120)
		print "This draws a triangle of length", length, "pixels at coordinate", x, y
			  
	   

def circle(x,y,radius,fill,color):
	'''
	This draws a circle at position (x,y) with a radius specified by the user via the 
	radius parameter. 
	'''
	goto(x,y)
	if fill==True:
		turtle.begin_fill()
		turtle.color(color)
		turtle.circle(radius)
		turtle.end_fill()
	
	elif fill==False:
		turtle.circle(radius)
		
def drawLighthouse(x,y,width,height,scale,fill):
	'''
	This draws a lighthouse at position (x,y) with the width of the base of the lighthouse
	twice as large as the width of the light tower and the height 1.33 times as large
	the height of the light tower. The base is colored tan.
	The middle tower is placed on top of andcentered to the base of the lighthouse 
	and is colored blanched almond. The black rectanglular tower that holds the light is
	placed and centered on top of the middle tower. This light tower is has a width of
	that is 1/2 of the width of the basewidth*scale while its height is 1/4 of the height
	of the base. It also draws a roof, which is an equilateral triangle whose length is 
	equal to the width of the light tower and is directly on top of the light tower.
	Then, a yellow circular light is drawn in the middle of the light tower.  
	This lighthouse should be drawn with these specifications stated above no matter the 
	x and y positions, width, height, and scale. 
	
	'''
	if fill==True:
		rectangle(x,y,width*2*scale,height*2*scale,True,"tan")
		'''
		This draws the rectangular tan base of the lighthouse
		'''
		rectangle(x+0.25*width*scale,y+height*2*scale,width*1.5*scale,height*.7*scale,
		True,"blanched almond")
		'''
		This draws the rectangular blanch almond colored middle tower of the lighthouse.
		'''
		rectangle(x+0.5*width*scale,y+height*2.7*scale,width*scale,scale*height/2,
		True,"black")
		'''
		This draws the part of the lighthouse that holds the light.
		'''
		triangle(x+0.5*width*scale,y+height*3.2*scale,width*scale,True,"red")
		'''
		This draws the red triangular roof of the lighthouse.
		'''
		circle(x+0.98*width*scale,y+height*2.73*scale,height*.2*scale,True,"yellow")
		'''This draws the yellow circular light of the lighthouse
		'''
		turtle.up()
		turtle.forward(100*scale)
		
	elif fill==False:
		'''
		This draws the lighthouse specified above without any color. 
		'''
		turtle.color("black")
		rectangle(x,y,width*2*scale,height*2*scale,False,"White")
		rectangle(x+0.25*width*scale,y+height*2*scale,width*1.5*scale,height*.7*scale,
		False,"White")
		rectangle(x+0.5*width*scale,y+height*2.7*scale,width*scale,scale*height/2,
		False, "White")
		triangle(x+0.5*width*scale,y+height*3.2*scale,width*scale,False, "White")
		circle(x+0.98*width*scale,y+height*2.73*scale,height*.2*scale, False, "White")
		turtle.up()
		turtle.forward(100*scale)
	
def myScene(x,y,scale):
	'''
	This creates the lighthouse on a rock scene from last week and draws
	the scene at position (x,y) and the scale of the scene is specified by the user
	via the scale parameter. 
	'''
	rectangle(x+-350*scale,y+-350*scale,700*scale,150*scale,True,"tan")
	rectangle(x+-350*scale,y+-200*scale,700*scale,150*scale,True,"blue")
	rectangle(x+-350*scale,y+-50*scale,700*scale,400*scale,True,"sky blue")
	rectangle(x+250*scale,y+-50*scale,100*scale,150*scale,True,"gray")
	drawLighthouse(x+285*scale,y+100*scale,30*scale,40*scale,0.8,True)
	circle(x+-220*scale,y+225*scale,50*scale,True,"Yellow")
	turtle.up()
	turtle.forward(-200*scale)
	
def myOtherScene(x,y,scale):
	'''
	This creates the mountain range scene from last week and draws the scene at 
	position (x,y) and the scale of this scene is specified by the user via the 
	scale parameter. 
	'''
	rectangle(x+-400*scale,y+-400*scale,800*scale,800*scale,True,"sky blue")
	'''
	This is what fills the rectanglular sky blue
	'''
	rectangle(x+-400*scale,y+-400*scale,800*scale,300*scale,True,"blue")
	for i in range (30):
		'''
		Draws a mountain range by drawing 30 triangular mountains of random size from
		range 20 to 100 pixels and at random coordinate ranging from (-400,-400) 
		to (100, 100)
	
		'''
		triangle(random.randint(x+-400*scale,x+200*scale),
		random.randint(y+-100*scale,y+100*scale),random.randint(30*scale,200*scale)
		,True,"green")
				
	circle(x+250*scale,y+250*scale,30*scale,True,"yellow")
	'''
	This draws a sun at the upper right hand corner of the sky. 
	'''
	
	turtle.up()
	turtle.forward(100)		

def main()
	drawLighthouse(0,0,30,40,1.0,True)
	raw_input('Press enter to exit')		
	
if __name__== "__main__" :
	main()





    