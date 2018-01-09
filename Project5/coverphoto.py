import sys
import graphics
import display
import filter
import collage

def main( argv ):
	'''
	This creates a collage of 3 images with the first element of each innerlist
	being the filename of the image you want to include in the collage,
	the second and third being the x and y positions of each image depending on its size, 
	the fourth being the filter applied to each filter.
	The fifth index is the alpha blend of each picture, the sixth is whether you
	want to remove the backgound or not 
	and the last one is the pixmap object after the image is read in. 
	The images that are included in the collage depend on user input. 
	'''
	if len(argv) < 4:
		print len(argv)
		print "Not enough input"
		exit()
			
	clist=[ [argv[1], 300, 100, 'negative', 1.0, False, None],
			[argv[2], 550, 200, 'Original', 0.5, True, None ],
			[argv[3], 150,350, 'reversepixels', 0.7, False, None]
			]
		  
	
	collage.readImages( clist )
	dest=collage.buildCollage( clist )
	dest.save( 'coverphoto.ppm' )
	
	return
	
	
if __name__ == "__main__":
	main(sys.argv)