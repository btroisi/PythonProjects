#Brandon Troisi
#2/24/16
#OceanScene.py

import sys
import graphics
import display


def placePixmapinOcean( dest, source ):
	'''
	Takes the pixels that are not part of the green screen from the file GreenScreen.ppm
	and places them into a picutre called OceanBackground.ppm. This places the pixels
	that make up the picture of only me from the green screen picture 
	into an ocean background.
	'''
	for i in range(graphics.Pixmap.getWidth(source)):
		for j in range(graphics.Pixmap.getHeight(source)):
			(r, g, b) = source.getPixel( i, j )
			if g<1.2*b or g<=1.1*r or g<70:
				(r, g, b) = source.getPixel( i, j )
				dest.setPixel(i,j, (r, g, b))

			
def main( argv ):
	if len(argv)<2:
		print "Usage : GreenScreenPic.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	source=graphics.Pixmap( file ) 
	dest=graphics.Pixmap('OceanBackground.ppm')
	placePixmapinOcean(dest,source)
	dest.save('MeInOcean.ppm')
	
	
	
if __name__=="__main__":
	main( sys.argv )
	
	
	