#Brandon Troisi
#3/2/16
#collage.py

import graphics
import display
import filter
import sys

IDXFilename = 0
IDXXoffset = 1
IDXYoffset = 2
IDXeffect = 3
IDXalpha = 4
IDXNoBkg = 5
IDXPixmap = 6
'''
These initializing variables represent each element in the inner list in the collage list 
called clist. 
'''
def readImages( clist ):
	'''
	This reads all of the images defined in clist. 
	'''
	for picParams in clist:
		filename=picParams[IDXFilename]
		source=graphics.Pixmap(filename)
		picParams[IDXPixmap]=source

def getImageSize( clist ):
	'''
	This gathers the size of each image defined in clist. 
	'''
	rows = 0
	cols = 0
	for picParams in clist:
		x0=picParams[IDXXoffset]
		y0=picParams[IDXYoffset]
		source=picParams[IDXPixmap]
		dx=x0+source.getWidth()
		if dx>cols:
			cols=dx
		dy=y0+source.getHeight()
		if dy>rows:
			rows=dy
	return (cols, rows) 

def buildCollage( clist ):
	'''
	This is what builds a collage with any ppm picture saved in the project 5 folder. 
	In the collage you can make it as big as you want, apply any filter you want, move 
	each image to a certain position in the collage, and use the alpha blend feature
	to blend pictures together any way you want. 
	'''
	(cols, rows) = getImageSize( clist )
	dest = graphics.Pixmap(cols,rows)
	for picParams in clist:
		filename=picParams[IDXFilename]
		x0=picParams[IDXXoffset]
		y0=picParams[IDXYoffset]
		filter=picParams[IDXeffect]
		alpha=picParams[IDXalpha]
		noBkg=picParams[IDXNoBkg]
		source=picParams[IDXPixmap]
	
	'''
	This assigns the filename to the first element of each inner list in clist, 
	the x offset of the image to the second, y offset of the image to the third, 
	the filter effect to the fourth, alpha blend to the fifth,
	wether to remove the background to the sixth, and pixmap source after image
	is read to the seventh. 
	'''	
		
		
		if filter == 'swapRedBlue':
			filter.swapRedBlue(source)
		elif operator == 'grayscale':
			filter.grayscale(source)
		elif filter == 'quarterBlueHalfGreen':
			filter.quarterBlueHalfGreen(source)
		elif filter == 'swapBluetoYellowRedtoPurple':
			filter.swapBluetoYellowRedtoPurple(source)
		elif filter == 'negative':
			filter.negative(source)
		elif filter == 'mirrorhoriz':
			filter.mirrorhoriz(source)
		elif filter == 'mirrorvert':
			filter.mirrorvert(source)
		elif filter == 'reversepixels':
			filter.reversepixels(source)
		'''
		These series of if statemtents are what applies a certain filter to a certain type
		of
		'''
		
		if noBkg == True:
			filter.placePixmapNoBkg(dest,source,x0,y0,alpha,'blue')
		else:	
			filter.placePixmap(dest,source,x0,y0,alpha)

		'''
		This if/else statment either removes the background of the image if noBkg is true
		and does nothing to the background otherwise. 
		'''
	
	return dest

				
def test( argv ):
	'''
	This is a test function to see that the every function other than the buildcollage 
	function works properly. 
	'''
	
	clist = [ 
	[ 'cupcakes.ppm', 0, 0, 'swapRedtoBlue', 0.8, False, None ],
	[ 'FallFoliage.ppm', 200, 150, 'original', 0.8, False, None ] 
	]

	for picParams in clist:
		print '----------------------'
		print 'filename:', picParams[IDXFilename]
		print 'X Offset:', picParams[IDXXoffset]
		print 'Y Offset:', picParams[IDXYoffset]
		print 'filter:', picParams[IDXeffect]
		print 'alpha:', picParams[IDXalpha]
		print 'PixmapObject:', picParams[IDXPixmap]
	
	readImages( clist )
	
	for picParams in clist:
		print picParams[IDXFilename]
		print picParams[IDXPixmap].getWidth()
		print picParams[IDXPixmap].getWidth()
	
	(cols,rows) = getImageSize( clist )
	print cols,rows

def main( argv ):
	'''
	This creates a collage with 2 images depending on user input. 
	'''
	
	if len(argv) < 3:
		print "Not enough input"
		exit()
	
	
	clist=[ [argv[1], 0, 0, 'swapRedBlue', 1.0, False, None],
			[argv[2], 150, 150, 'grayscale', 0.5, False, None ]]
			
	readImages( clist )
	dest= buildCollage( clist )
	dest.save( 'testcollage.ppm' )
	
	
	return
					  
if __name__ == "__main__":
	main( sys.argv )
	
	
	


	