#Brandon Troisi
#2/24/16
#OceanScene.py

import sys
import graphics
import display



def placePixmapinOcean( dest, source ):
	'''
	Takes a source pixmap and copies it into a second pixmap named dest.
	'''
	for i in range(graphics.Pixmap.getWidth(source)):
		for j in range(graphics.Pixmap.getHeight(source)):
			(r, g, b) = source.getPixel( i, j )
			if g<=2.3*r and g<1.7*b and r>=0.7*b:	
				dest.setPixel(i,j, (r, g, b))

			
def main( argv ):
	if len(argv)<2:
		print "Usage : GreenScreenPic.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	source=graphics.Pixmap( file ) 
	dest=graphics.Pixmap('WoodsScene.ppm')
	placePixmapinOcean(dest,source)
	dest.save('MeInWoods.ppm')
	

	
if __name__=="__main__":
	main( sys.argv )
	
	
	