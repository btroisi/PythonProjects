#Brandon Troisi
#3/2/16
#mycollage.py

import sys
import graphics
import display
import filter
import collage

def main( argv ):
'''
This creates a collage of 5 images with the first element of each innerlist
being the filename of the image you want to include in the collage,
the second and third being the x and y positions of each image depending on its size, 
the fourth being the filter applied to each filter.
The fifth index is the alpha blend of each picture, the sixth is whether you
want to remove the backgound or not and the last one is the pixmap object after the image
is read in. The images included in the collage depend on user input.  
'''
	if len(argv) < 6:
		print len(argv)
		print "Not enough input"
		exit()
			
	clist=[ [argv[1], 0, 0, 'reversepixels', 1.0, False, None],
			[argv[2], 0, 150, 'mirrorvert', 0.7, False,None ],
			[argv[3], 300, 100, 'swapRedBlue', 0.6, False,None],
			[argv[4], 500,-200, 'original', 0.6, True, None],
			[argv[5],400,20,'negative', 0.7,False,None]
			]
	
	collage.readImages( clist )
	dest=collage.buildCollage( clist )
	dest.save( 'testcollage.ppm' )
	
	return
	
	
if __name__ == "__main__":
	main(sys.argv)