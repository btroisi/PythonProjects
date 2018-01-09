def swapveryBlue( pm ):
	'''
	This swaps the all of the blue pixels of the picture with red pixels
	'''
	for i in range(graphics.Pixmap.getWidth( file )):
		for j in range(graphics.Pixmap.getHeight( file )):
			(r, g, b) = pm.getPixel( i, j )
			if g>= 2*r and g>b:
				file.setPixel(i,j,(r,r,b))
	convert GreenScreen.jpg GreenScreen.ppm
	file.save('MyAlteredPic.ppm')




def main( argv ):
	if len(argv)<2:
		print "Usage : show.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	warhol( file )
	
if __name__=="__main__":
	main( sys.argv )
	