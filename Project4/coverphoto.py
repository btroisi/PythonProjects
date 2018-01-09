import sys
import graphics
import display
import filter
import collage

def main( argv ):
	if len(argv) < 6:
		print len(argv)
		print "Not enough input"
		exit()
			
	clist=[ [argv[1], 0, 0, 'swapRedBlue', 1.0, False, None],
			[argv[2], 0, 150, 'quarterBlueHalfGreen', 0.5, False, None ],
			[argv[3], 300, 100, 'grayscale', 0.6, True, None]
		  ]
	
	collage.readImages( clist )
	dest=collage.buildCollage( clist )
	dest.save( 'testcollage.ppm' )
	
	return
	
	
if __name__ == "__main__":
	main(sys.argv)