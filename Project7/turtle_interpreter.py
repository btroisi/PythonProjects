#Brandon Troisi
#3/30/2016
#turtle_interpreter.py

import turtle
import sys
import lsystem as ls

def drawString( dstring, distance, angle ):
    '''
    Interprets the characters in string dstring as a series
	of turtle commands. Distance specifies the distance
	to travel for each forward command. Angle specifies the
	angle (in degrees) for each right or left command. The list of 
	turtle supported turtle commands is:
	F : forward
	- : turn right
	+ : turn left
	[ : save position, heading
	] : restore position, heading
	R : Draws a red leaf by drawing a half circle filled red of radius 5
	O : Draws an orange leaf by drawing a half circle filled orange of radius 3
	Y : Draws a yellow leaf by drawing a half circle filled yellow of radius 2
	B : Draws a brown line
    '''
    stack=[]
    for c in dstring:
        if c=='F':
            turtle.forward(distance)
        elif c =='+':
            turtle.left(angle)
        elif c=='-':
            turtle.right(angle)
        elif c =='[':
            stack.append(turtle.position())
            stack.append(turtle.heading())
        elif c == ']':
            turtle.up()
            turtle.setheading(stack.pop())
            turtle.goto(stack.pop())
            turtle.down()
        elif c == 'R':
        	turtle.begin_fill()
        	turtle.color('red')
        	turtle.circle(5,180)
        	turtle.end_fill()
        elif c == 'O':
        	turtle.begin_fill()
        	turtle.color('orange')
        	turtle.circle(3,180)
        	turtle.end_fill()
        elif c == 'Y':
        	turtle.begin_fill()
        	turtle.color('yellow')
        	turtle.circle(2,180)
        	turtle.end_fill()
        elif c == 'B':
        	turtle.color('brown')
        
            
    turtle.update()
            
def hold():
      """ holds the screen open until the user clicks or types 'q' """

      # have the turtle listen for events
      turtle.listen()

      # hide the turtle and update the screen
      turtle.ht()
      turtle.update()

      # have the turtle listen for 'q'
      turtle.onkey( turtle.bye, 'q' )
      # have the turtle listen for a click
      turtle.onscreenclick( lambda x,y: turtle.bye() )

      # start the main loop until an event happens, then exit
      turtle.mainloop()
      exit()

def main(argv):
    '''
    Draws something in the turtle window using the L system that is in a file that 
    is entered on the command line. The second and third input is respectively what 
    distance the turtle should go forward and the angle the turtle should turn.
    '''
    
    if len(argv) < 4:
        print 'usage: %s <lsystem filename> <distance> <angle>' % (argv[0])
        exit()

    
    lsys = ls.createLsystemFromFile( argv[1] )

    
    lstr = ls.buildString( lsys, 3 )

    dist = float( argv[2] )
    angle = float( argv[3] )

    
    turtle.tracer(False)
    turtle.left(90)
    drawString( lstr, dist, angle )
    
    
    hold()


if __name__ == "__main__":
    main( sys.argv )


        