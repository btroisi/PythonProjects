#Brandon Troisi
#2/10/2016
#lab2.py

import turtle
import random

def goto(x,y):
    '''This will move the turtle to a new x and y location without moving the pen '''
    turtle.up() 
    turtle.goto(x,y)
    turtle.down()
    print 'goto(): going to', x, y

   
def rectangle(x,y,width,height):
	'''
		This draws a rectangle of dimensions width by height in the turtle. 
		
	'''
	goto(x,y)
	turtle.forward(width)
	turtle.left(90)
	turtle.forward(height)
	turtle.left(90)
	turtle.forward(width)
	turtle.left(90)
	turtle.forward(height)
	turtle.left(90)
	print "This draws a rectangle of",width, "by", height, "pixels at coordinates", x, y
	
def triangle(x,y,length):
	'''
		This draws an equalateral triangle of side length 
		length in the turtle.
		Starts drawing triangle at coordinate (x,y). 
	'''	
	goto(x,y)
	for i in range (3):
		'''
		This tells the turtle to draw a line of length length
		and rotate 120 degreees countercolcwise.
		This command is repeated 3 times to draw a triangle of size length. 
    	'''
		turtle.forward(length)
		turtle.left(120)
	print "This draws a triangle of length", length, "pixels at coordinates", x, y
	
def circle(x,y,radius):
	'''
	This draws a circular light in the top block of the lighthouse of radius width*scale.
	'''
	goto(x,y)
	turtle.circle(radius)


def drawLighthouse(x,y,width,height,scale):
	turtle.begin_fill()
	turtle.color("tan")
	rectangle(x,y,width*2*scale,height*2*scale)
	turtle.end_fill()
	#This draws the rectangular tan base of the lighthouse
	turtle.begin_fill()
	turtle.color("blanched almond")
	rectangle(x+0.25*width*scale,y+height*2*scale,width*1.5*scale,height*.7*scale)
	turtle.end_fill()
	#This draws the rectangular black middle part of the lighthouse.
	turtle.begin_fill()
	turtle.color("black")
	rectangle(x+0.5*width*scale,y+height*2.7*scale,width*scale,scale*height/2)
	turtle.end_fill()
	#This draws the part of the lighthouse that holds the light.
	turtle.begin_fill()
	turtle.color("red")
	triangle(x+0.5*width*scale,y+height*3.2*scale,width*scale)
	turtle.end_fill()
	#This draws the red triangular roof of the lighthouse.
	turtle.begin_fill()
	turtle.color("yellow")
	circle(x+0.98*width*scale,y+height*2.73*scale,height*.25*scale)
	turtle.end_fill()
	#This draws the yellow circular light of the lighthouse
	turtle.up()
	turtle.forward(100*scale)
	
	
	
	
	
	
	
	



 