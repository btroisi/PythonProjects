#Brandon Troisi
#2/24/16
#GreenScreenPicExt.py

import sys
import graphics
import display

def changeVeryGreen( pm ):
	'''
	This swaps the all of the green pixels of the picture with differnent colored pixels
	'''
	for i in range(graphics.Pixmap.getWidth( pm )):
		for j in range(0,graphics.Pixmap.getHeight( pm ),30):
			(r, g, b) = pm.getPixel( i,j )
			if g>= 1.3*r and g>b:
				pm.setPixel(i,j,(0,0,255))
	'''
	This draws vertical blue stripes every 30 pixels traveling in the horizontal direction
	(left to right starting from (0,0)) on the green background of the picture.
	'''
	
	for i in range(0,graphics.Pixmap.getWidth( pm ),30):
		for j in range(graphics.Pixmap.getHeight( pm )):
			(r, g, b) = pm.getPixel( i,j )
			if g>= 1.3*r and g>b:
				pm.setPixel(i,j,(255,0,0))
	'''
	This draws horizontal red stripes every 30 pixels traveling in the vertical direction
	(up to down starting from (0,0)) on the green background of the picture. 
	'''
	
	pm.save('MyStripedPic.ppm')
	'''
	Saves result to file named MyStripedPic.ppm
	'''

def main( argv ):
	if len(argv)<2:
		print "Usage : GreenScreenPic.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	changeVeryGreen( pm )
	
if __name__=="__main__":
	main( sys.argv )
	