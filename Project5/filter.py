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
	for i in range(pm.getWidth( )):
		for j in range(pm.getHeight( )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,(b,g,r))
	pm.save('MyPic.ppm')
	
	
def placePixmap( dest, source, x, y,alpha ):
	'''
	Takes a source pixmap and copies it into a second pixmap named dest
	with top left-hand corner at position (x,y).
	'''
	for i in range(source.getWidth()):
		for j in range(source.getHeight()):
			(r1, g1, b1) = source.getPixel( i, j )
			(r2, g2, b2) = dest.getPixel( x+i, y+j )
			rnew = r1*alpha + (1.0-alpha)*r2
			gnew = g1*alpha + (1.0-alpha)*g2
			bnew = b1*alpha + (1.0-alpha)*b2
			dest.setPixel(x+i,y+j, (rnew, gnew, bnew))
			
def grayscale( pm ):
	'''
	Changes picture to grayscale
	'''
	for i in range(pm.getWidth( )):
		for j in range(pm.getHeight( )):
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
	for i in range(pm.getWidth( )):
		for j in range(pm.getHeight(  )):
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
	for i in range(pm.getWidth(  )):
		for j in range(pm.getHeight(  )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,( (r+b)/2, g, (b+g)/2))
	pm.save('MyBlueToYellowRedtoPurple.ppm')
	'''
	Saves result to file named MyBluetoYellowRedtoPurple.ppm
	'''
def negative( pm ):
	'''
	Creates a photo with only negatives in it
	'''
	for i in range(pm.getWidth(  )):
		for j in range(pm.getHeight(  )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,( 255-r, 255-g, 255-b))
	'''
	Saves result to file name MyNegativeImage.ppm
	'''
	pm.save("MyNegativeImage.ppm")
	
def mirrorhoriz( pm ):
	'''
	Reflects left side of image to right
	'''
	width=pm.getWidth()
	height=pm.getHeight()
	for i in range(0,width/2):
		for j in range(0,height):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,(r,g,b))
			pm.setPixel(width-i-1,j,(r, g, b))
	
	pm.save("MyreflectedhorizontalImage.ppm")

	
def mirrorvert( pm ):
	'''
	Reflects top part of image to bottom
	'''
	width=pm.getWidth()
	height=pm.getHeight()
	for j in range(0,height/2):
		for i in range(0,width):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,(r,g,b))
			pm.setPixel(i,height-j-1,(r, g, b))
	
	pm.save("MyreflectedverticalImage.ppm")
	
def reversepixels( pm ):
	for i in range(pm.getWidth(  )):
		for j in range(pm.getHeight(  )):
			(r, g, b) = pm.getPixel( i, j )
			pm.setPixel(i,j,( g,b,r))
	
	pm.save("MyReversedPixels.ppm")

def placePixmapNoBkg( dest, source, x, y,alpha, bkgcolor):
	'''
	For a picture with a peson in front of a very blue or very green background, 
	it only saves the pixels that are not part of that background.
	'''
	for i in range(source.getWidth()):
		for j in range(source.getHeight()):
			(r, g, b) = source.getPixel( i, j )
			if bkgcolor == 'green':
				if g<1.2*b or g<=1.1*r or g<70:
					(r, g, b) = source.getPixel( i, j )
					dest.setPixel(i,j, (r, g, b))
					'''
					Only saves pixels that are not part of green background
					'''
			if bkgcolor == 'blue':
				if b<r or b<=1.1*g or b<100:
					(r, g, b) = source.getPixel( i, j )
					dest.setPixel(i,j, (r, g, b))
			 		'''
			 		Only saves pixels that are not part of blue background.
			 		'''
		
def test( argv ):
	'''
	This tells python to only save negative image
	'''
	if len(argv)<2:
		print "Usage : show.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	reversepixels( pm )
	
	
if __name__=="__main__":
	test( sys.argv )	
	
		
