#Brandon Troisi
#2/24/16
#GreenScenePic.py

import sys
import graphics
import display

def changeVeryGreen( pm ):
	'''
	This changes the background to a grayish-red color
	'''
	for i in range(graphics.Pixmap.getWidth( pm )):
		for j in range(graphics.Pixmap.getHeight( pm )):
			(r, g, b) = pm.getPixel( i, j )
			if g>=r and g>b:
				pm.setPixel(i,j,(r,r,b))
	
	pm.save('MyAlteredPic.ppm')
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
	