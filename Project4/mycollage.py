import sys
import graphics
import display
import filter
import collage

def main( argv ):
	if len(argv) < 6:
		print "Not enough input"
		exit()
	
	
	clist=[ [argv[1], 0, 0, 'swapRedBlue', 1.0, False, None],
			[argv[2], 150, 150, 'grayscale', 0.5, False, None ]
			[argv[3], 200, 0, 'swapBluetoYellowRedtoPurple', 0.2, False, None]
			[argv[4], 0,-150, 'quarterblueHalfGreen', 0.4, True, None]
			[argv[5],-175,175,'swapRedBlue', 0.7,False,None]
	
	collage.readImages( clist )
	dst=collage.buildCollage( clist )
	dst.save( 'testcollage.ppm' )
	
	return
	
	
if __name__ == "__main__"
	main(sys.argv)