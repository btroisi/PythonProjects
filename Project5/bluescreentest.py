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
			if b<r or b<=1.1*g or b<100:
				(r, g, b) = source.getPixel( i, j )
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
	dest.save('PhrasantInOcean.ppm')
	
	
	
if __name__=="__main__":
	main( sys.argv )