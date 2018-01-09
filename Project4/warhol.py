#Brandon Troisi
#2/24/16
#warhol.py

import graphics
import display
import sys
import filter


def warhol( file ):

	'''
	This creates a warhol style collage that saves four images of a lake in different
	filter effects. The filter effecs are the ones defined in the filter file.
	'''

	pmap=graphics.Pixmap(file) #image read in one pixmap
	map1=pmap.clone() #makes four copies of it
	map2=pmap.clone()
	map3=pmap.clone()
	map4=pmap.clone()
	
	
	filter.swapRedBlue(map1)
	filter.grayscale(map2)
	filter.quarterBlueHalfGreen(map3)
	filter.swapBluetoYellowRedtoPurple(map4)
	'''
	Sets each clone to different filter.
	'''
	
	source=graphics.Pixmap(file)
	dest = graphics.Pixmap( graphics.Pixmap.getWidth(source) * 2, 
	graphics.Pixmap.getHeight(source)*2 )
	
	filter.placePixmap(dest, map1, 0, 0)
	filter.placePixmap(dest,map2, 0, graphics.Pixmap.getHeight(source))
	filter.placePixmap(dest,map3, graphics.Pixmap.getWidth(source), 0)
	filter.placePixmap(dest, map4, graphics.Pixmap.getWidth(source), 
	graphics.Pixmap.getHeight(source))
	'''
	Sets filtered pixmap to different positions on second pixmap created by
	placePixmap function. 
	'''
	
	dest.save("Bigfile.ppm")	
	'''
	Saves result to file named Bigfile.ppm
	'''

def main( argv ):
	if len(argv)<2:
		print "Usage : show.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap( file )
	warhol( file )
	
if __name__=="__main__":
	main( sys.argv )
	