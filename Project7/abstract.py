#Brandon Troisi
#4/5/16
#abstract.py


import sys
import turtle 
import lsystem as ls
import turtle_interpreter as ti


def main():

   
	my_lsys1 = ls.init()
	ls.setBase( my_lsys1, 'F' )
	ls.addRule( my_lsys1, ['F','F-FF+F-FF'] )
	
	lsys1=[ls.getBase( my_lsys1), ls.getRule( my_lsys1, 0)]
							 
 	lstr1 = ls.buildString( my_lsys1, 4 )
 	
	my_lsys2 = ls.init()
	ls.setBase( my_lsys2, 'F' )
	ls.addRule( my_lsys2, ['F', 'F[+F]+F-[F'] )
	
	lsys2 = [ls.getBase( my_lsys2), ls.getRule( my_lsys2,0)]
	
	lstr2 = ls.buildString( my_lsys2, 4)
	
	my_lsys3 = ls.init()
	ls.setBase( my_lsys3, 'F' )
	ls.addRule( my_lsys3, ['F', 'F+[F-]+F[F'] )
	
	lsys3 = [ls.getBase( my_lsys3), ls.getRule( my_lsys3,0)]
	
	lstr3 = ls.buildString( my_lsys3, 4)
	
	
    # draw the lsystem
	turtle.tracer(False)
	turtle.up()
	turtle.goto(100,-200)
	turtle.down()
	turtle.left(90)
	ti.drawString( lstr1, 3, 90 )
	turtle.up()
	turtle.goto(0,100)
	turtle.down()
	ti.drawString( lstr2, 30, 120 )
	turtle.up()
	turtle.goto(-100,60)
	turtle.down()
	ti.drawString( lstr3, 15, 60 )
	
    #wait
	ti.hold()
			
    
    
				
if __name__ == '__main__':
    main()