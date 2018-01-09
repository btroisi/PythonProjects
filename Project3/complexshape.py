import turtle
import better_shapelib as bsl
import sys
import random

def main():
	x=0
	y=0
	N = 30
	scale=0.3
	skycolor="sky blue"
	mountcolor = "green" 
	moonsuncolor = "yellow"
	
	if len( sys.argv ) > 7:
		x = int( sys.argv[1] )
		y = int( sys.argv[2] )
		N = int( sys.argv[3] )
		scale = float( sys.argv[4] )
		skycolor = str( sys.argv[5] )
		mountcolor = str(sys.argv[6] )
		moonsuncolor = str(sys.argv[7] )
		

        
	
	bsl.rectangle(x+-400*scale,y+-400*scale,800*scale,800*scale,True,skycolor)
	'''
	This is what fills the rectanglular sky blue
	'''
	bsl.rectangle(x+-400*scale,y+-400*scale,800*scale,300*scale,True,"blue")
	for i in range (N):
		'''
		Draws a mountain range by drawing N triangular mountains of random size from
		range 20 to 100 pixels and at random coordinate ranging from (-400,-400) 
		to (100, 100)
	
		'''
		bsl.triangle(random.randint(x+-400*scale,x+200*scale),
		random.randint(y+-100*scale,y+100*scale),random.randint(30*scale,200*scale)
		,True,mountcolor)
				
	bsl.circle(x+250*scale,y+250*scale,30*scale,True,moonsuncolor)
	'''
	This draws a sun at the upper right hand corner of the sky. 
	'''
	
	turtle.up()
	turtle.forward(100)	
	raw_input("Press enter to exit")

if __name__=="__main__":
	main()
	
#brandons-mbp:Project3 Brandon$ python complexshape.py 0 -100 10 0.4 black NavajoWhite4
#BlanchedAlmond
		

	
