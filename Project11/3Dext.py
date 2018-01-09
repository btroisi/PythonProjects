#Brandon Troisi
#3Dext.py


import shapes
import turtle_interpreter as ti
import turtleTk3D as turt



def wallception(x,y,z,distance,color,style):
	'''
	Creates a series of cubes within cubes at (x,y,z) starting with size distance and 
	the sizes of the cubes decrease by 1/2 its original size every iteration unitl the 
	size of the cube is 50 pixels. The series of cubes is drawn with style style and with
	color color
	'''
	s=shapes.cube()
	if distance<50:
		return
	else:
		s.setDistance(distance)
		s.setStyle(style)
		s.setColor(color)
		s.draw(x, y, 1.0, 0,0,0,z)
		wallception(x,y,z,distance/2,color,style)

def octtower(x,y,z,distance,pitch,color,style):
	'''
	This creates a leaning stack of octagons at (x,y,z) with initial size distance and 
	initial pitch pitch. With each new octagon that is drawn, the ptich is decreased by
	10 every time until the pitch is 30 dgreees and the size decreases by 0.9 with every
	octagon drawn until the distance is 1. The tower stops drawing either when the pitch
	is less than 30 or when the distance is less than one, whichever occurs first. 
	'''
	oct=shapes.ocube()
	if pitch<30 or distance<1:
		return
	else:
		oct.setDistance(distance)
		oct.setStyle(style)
		oct.setColor(color)
		oct.setPitch(pitch)
		oct.draw(x, y, 1.0, 0,0,pitch,z)
		octtower(x,y,distance+z+distance*.9,distance*.9,pitch-10,color,style)

def bullet(x,y,style,color):
	'''
	Creates diamond shaped bullets at (x,y,0) with style style and with color color
	'''
	d=shapes.diamond()
	d.setStyle(style)
	d.setColor(color)
	d.draw(x,y,1)
	
def drawmon(event=None):
	'''
	This draws a monument when you hit control and hit the right key pad or the
	right mouse click ,depending on the computer used, at the specific position you perform
	either command on. Works best before you rotate the scene. 
	'''
	terp=ti.TurtleInterpreter()
	m=shapes.monument()
	(x,y,z) = terp.window2turtle(event.x, event.y)
	m.draw(x,y,1)
	
def main():
	'''
	This attaches the draw monument function to the command control right click on a laptop
	or the right mouse click.
	'''
	terp=ti.TurtleInterpreter()
	terp.setRightMouseCallback(drawmon)
	


def scene():
	'''
	This draws a series of blue cubes in style jitter3 at (-300,0,0) starting with
	size 200 and the size of each cube is reduced in half until the size gets to 50, 
	draws a green tower of octagons at (200,0,0) where the base octagon is of size 50 and the initial pitch
	is 90. The size of the octagons continue to decrease and the pitch continues to decrease
	until the pitch is 30. The style of the octagonal tower is drawn with a normal style.
	Then a plain black 2D triangle is placed at (200,40,0), near the 
	smallest octagon of the tower drawn normal style. Then five bullets are drawn from the 
	largest base of the octagonal tower, following a parabolic path until the last bullet
	reaches the corner of the smallest cube. From the beginning to the end of the path
	the color of the bullets are orange, red, blue, green, and purple. From the beginiing 
	to the end of the path, the styles of each bullet are normal, normal, jitter, jitter3,
	and jitter
	'''
	t=shapes.TriangleU()
	wallception(-300,0,0,200,'blue','jitter3')
	octtower(200,0,0,50,90,'green','normal')
	bullet(0,115,'normal','red')
	bullet(100,90,'normal','orange')
	bullet(-200,80,'jitter3','green')
	bullet(-80,110,'jitter','blue')
	bullet(-300,0,'jitter','purple')
	t.draw(200,40,0.25)
	
	
		
if __name__=='__main__':
	scene()
	main()
	raw_input('Press enter to exit')
