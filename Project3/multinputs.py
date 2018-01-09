import turtle
import better_shapelib as bsl
import sys
import random

def MountScene():
	'''
	This allows the user to use the command prompt to control several aspects of the scene
	including position, number of mountains drawn in the scene, scale of the scene,
	the color of the sky, the color of the mountains, and the color of the sun or moon
	at the top of the scene. The below variable definitions set default values for these
	parameters in case the user forgets to input anything into the command prompt.  
	'''
	x=0
	y=0
	N = 30
	scale=0.3
	skycolor="sky blue"
	mountcolor = "green" 
	moonsuncolor = "yellow"
	
	if len( sys.argv ) > 7:
		x = int( sys.argv[1] ) #Allows user to input x coordinate of the scene.
		y = int( sys.argv[2] ) #Allows user to input y coordinate of the scene.
		N = int( sys.argv[3] ) #Allows user to choose number of mountains in scene
		scale = float( sys.argv[4] ) #Allows user to choose scale of scene.
		skycolor = str( sys.argv[5] ) #Allows user to choose color of sky.
		mountcolor = str(sys.argv[6] ) #Allows user to choose color of mountains in scene.
		moonsuncolor = str(sys.argv[7] ) #Allows user to choose color of moon or sun.
		
	
	bsl.rectangle(x+-400*scale,y+-400*scale,800*scale,800*scale,True,skycolor)
	'''
	This is what fills the rectanglular sky the color the user specifies
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
	This draws a sun/moon at the upper right hand corner of the sky and colors it
	in whatever color the user specifies. 
	'''
	
	turtle.up()
	turtle.forward(100)	
	raw_input("Press enter to exit")

def main():
	'''
	Defines the part of the code that should be run
	'''
	MountScene()
	
if __name__=="__main__":
	'''
	This only executes the code defined in the main function. 
	'''
	main()
	

		

	
