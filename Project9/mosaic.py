#Brandon Troisi
#4/19/16
#mosaic.py

import lsystem
import shapes


def tile(x,y,scale):
	'''
	Draws a square tile of unit length 1, which then is modified based on the scale
	Draws a set of triangles inside this square that is scale by scale in size with 
	lower left corner at (x,y). This creates scale by scale triangles in a square. 
	'''
	Square1=shapes.Square(1)
	Square1.draw(x,y,scale)
	
	x0=x
	y0=y
	for i in range (10):
		x0=x+i*scale/10
		for j in range(10):
			y0=y-j*scale/10-scale/10
			Triangle1=shapes.Triangle(1)
			Triangle1.setColor('blue')
			Triangle1.draw(x0,y0,scale/10)	
	
	
def mosaic(x,y,scale,Nx,Ny):
	'''
	Draws array of tiles Nx by Ny, where each tile is of size scale by scale and lower 
	left corner is at (x,y).
	'''


	for i in range(Nx):
		x0=x+i*scale
		for j in range(Ny):
			y0=y+j*scale*1.02
			tile(x0,y0,scale)
			
def tile2(x,y,scale):
	'''
	Draws an unfilledtriangle tile of unit length 1, which then is modified based 
	on the scale. Draws a set of triangles inside this square that is of size scale 
	with the lower left corner at (x,y). This creates a series of red triangles in a 
	triangle. 
	'''
	Triangle1=shapes.TriangleU(1)
	Triangle1.draw(x,y,scale)
	
	
	for i in range (10):
		shift=0
		numTriangles=10-i
		for j in range(numTriangles):
			if scale%20==0:			
				x0=x+i*scale/10+shift
				y0=y+j*scale/11.5
				Triangle1=shapes.Triangle(1)
				Triangle1.setColor('red')
				Triangle1.draw(x0,y0,scale/10)
				shift+=scale/20
			else:			
				x0=x+i*scale/10+shift
				y0=y+j*scale/11.59
				Triangle1=shapes.Triangle(1)
				Triangle1.setColor('red')
				Triangle1.draw(x0,y0,scale/10)
				shift+=scale/20
					
	
if __name__=='__main__':
	mosaic(-200,-200,50,5,4)
	tile2(-70,-45,120)
	tile2(-200,-45,120)
	
	raw_input('Enter to exit')