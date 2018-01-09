#Brandon Troisi
#2/24/16
#filter.py

import graphics
import display
import sys

def swapRedBlue( pm ):
	'''
	This swaps the all of the blue pixels of the picture with red pixels.
	'''
	for i in range(graphics.Pixmap.getWidth( pm )):
		for j in range(graphics.Pixmap.getHeight( pm )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,(b,g,r))
	pm.save('MyPic.ppm')
	
	
def placePixmap( dest, source, x, y ):
	'''
	Takes a source pixmap and copies it into a second pixmap named dest
	with top left-hand corner at position (x,y).
	'''
	for i in range(graphics.Pixmap.getWidth(source)):
		for j in range(graphics.Pixmap.getHeight(source)):
			(r, g, b) = source.getPixel( i, j )
			dest.setPixel(x+i,y+j, (r, g, b))
			
def grayscale( pm ):
	'''
	Changes picture to grayscale
	'''
	for i in range(graphics.Pixmap.getWidth( pm )):
		for j in range(graphics.Pixmap.getHeight( pm )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,( b, b, b))
	pm.save('MyGrayscale.ppm')
	'''
	Saves result to file named MyGrayscale.ppm
	'''
			
def quarterBlueHalfGreen( pm ):
	'''
	Makes picture so that it makes the blue value 1/4 of its original value,
	makes green pixels half its original value, while the value of the red pixel is
	maintains its value. Makes picture darker.
	'''
	for i in range(graphics.Pixmap.getWidth( pm )):
		for j in range(graphics.Pixmap.getHeight( pm )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,( b/4, g/2, r))
	pm.save('MyQuarterBlueHalfGreen.ppm')
	'''
	Saves result to file named MyQuaterBlueHalfGreen.ppm
	'''

def swapBluetoYellowRedtoPurple( pm ): 
	'''
	Makes picture so that it makes blue values have values
	that produce yellow and red pixels have values that produce purple.
	Makes picture lighter.
	'''	
	for i in range(graphics.Pixmap.getWidth( pm )):
		for j in range(graphics.Pixmap.getHeight( pm )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,( (r+b)/2, g, (b+g)/2))
	pm.save('MyBlueToYellowRedtoPurple.ppm')
	'''
	Saves result to file named MyBluetoYellowRedtoPurple.ppm
	'''
	
def test( argv ):
	'''
	This tells python to only save grayscale image
	'''
	if len(argv)<2:
		print "Usage : show.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	grayscale( pm )
	
	
if __name__=="__main__":
	test( sys.argv )	
	
		
