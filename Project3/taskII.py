import turtle
import better_shapelib as bsl
import sys

def Museum():
	'''
	This creats a museum scene which draws two framed "paintings". The "paintings" are
	the two scenes from last week. 
	'''
	turtle.color("brown")
	bsl.rectangle(-250,-50,300,300,False,"White")
	'''
	This draws a brown square frame of300 pixels drawn at (-250,-50) 
	around the lighthouse scene
	'''
	bsl.myScene(-100,100,0.4)
	'''
	This draws the lighthouse scene at position (-100,100) and
	the scene is drawn at 0.4 times its original size. 
	'''
	turtle.color("black")
	bsl.rectangle(113,13,175,175,False,"White")
	'''
	Then it draws a black square frame of 175 pixels at position (113,13) around th
	'''
	bsl.myOtherScene(200,100,0.2)
	'''
	This draws the mountain range scene at position (200,100) and the scene is drawn
	at 0.2 times its original size. 
	'''

def DayNight():
'''
This uses sys.argv to allow the user to input a statement that will dictate certain 
aspects of the lighthouse scene so that it either produces a scene of what the lighthouse
image would look like during the day or at night. 
'''
	if len( sys.argv ) > 1:
		TOD = str(sys.argv[1]) #asks user for time of day
		'''
		These varable definitions specify initial x and y coordinates at which various
		aspects of the lighthouse scene will be drawn at and will specify the scale at 
		which everything in the scene is drawn via the scene parameter. 
		'''
		x=-100
		y=0
		scale=0.7
		
		if TOD=="Day":
			'''
			This creates the lighthouse scene to reflect daytime, so it makes
			the sky sky blue and draws a sun high up in the sky. 
			'''
			bsl.rectangle(x+-350*scale,y+-350*scale,700*scale,150*scale,True,"tan")
			bsl.rectangle(x+-350*scale,y+-200*scale,700*scale,150*scale,True,"blue")
			bsl.rectangle(x+-350*scale,y+-50*scale,700*scale,400*scale,True,"sky blue")
			bsl.rectangle(x+250*scale,y+-50*scale,100*scale,150*scale,True,"gray")
			bsl.drawLighthouse(x+285*scale,y+100*scale,30*scale,40*scale,0.8,True)
			bsl.circle(x+-220*scale,y+225*scale,50*scale,True,"Yellow")
			turtle.up()
			turtle.forward(-200*scale)
		elif TOD=="Night":
			'''
			This creates the lighthouse to reflect nighttime, so it makes the sky purple
			and draws a moon lower in the sky.  
			'''
			bsl.rectangle(x+-350*scale,y+-350*scale,700*scale,150*scale,True,"tan")
			bsl.rectangle(x+-350*scale,y+-200*scale,700*scale,150*scale,True,"blue")
			bsl.rectangle(x+-350*scale,y+-50*scale,700*scale,400*scale,True,"purple")
			bsl.rectangle(x+250*scale,y+-50*scale,100*scale,150*scale,True,"gray")
			bsl.drawLighthouse(x+285*scale,y+100*scale,30*scale,40*scale,0.8,True)
			bsl.circle(x+-220*scale,y+150*scale,50*scale,True,"salmon")
			turtle.up()
			turtle.forward(-200*scale)	
	
def main():
	'''
	This specifies the aspect of the code that should be executed. 
	'''
	DayNight()
	raw_input("Press enter to exit")

if __name__=="__main__":
	'''
	This specifies that the only scene the turtle should be drawing is the lighthouse
	scene during that day or at night.
	'''
	main()
	