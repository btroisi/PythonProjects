#Brandon Troisi
#2/10/2016
#lab2.py

import turtle
import random

def goto(x,y):
    '''This will move the turtle to a new x and y location without moving the pen '''
    turtle.up() 
    turtle.goto(x,y)
    turtle.down()
    print 'goto(): going to', x, y



def block( x, y, width, height ):
    '''
       Draws a rectangle of the given width and height
       with lower left corner at location (x,y)
    '''
    goto( x, y )
    print 'block(): drawing block of size', width, height
    turtle.forward( width )
    turtle.left( 90 )
    turtle.forward( height)
    turtle.left( 90 )
    turtle.forward(width)
    turtle.left( 90 )
    turtle.forward( height )
    turtle.left( 90 )
   

def bunchOfBlocks( x, y, scale ):
    '''
      This draws several stacked blocks at location x, y
      The bottom block is the largest
      Middle block is not as large as bottom block, but not as small as top block
      Top block is smallest
    '''
    print 'bunchOfBlocks(): drawing blocks at location', x, y
    
    
    block( x, y, 45*scale, 90*scale )
    block( x+15*scale, y+90*scale, 15*scale, 30*scale )
    block( x+20.5*scale, y+120*scale, 5*scale, 15*scale )



for i in range( 10 ):  
    '''
    Draws several stacks of 3 blocks at random x, y coordinates 
    Draws these stacks of random size
    This is repeated 10 times
    '''
    bunchOfBlocks(  random.random( )*600 - 300, 
                    random.random( )*600 - 300,
                    random.random( )*2 + .05
                    ) 
                                    


raw_input('Press enter to continue')