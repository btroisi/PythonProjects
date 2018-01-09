# Bruce Maxwell
# Spring 2013
# lab 11 test function 1
# makes three versions of a pyramid

import turtle_interpreter as it

def main():

    terp = it.TurtleInterpreter()

    pyr = '[F+F+F+[F(135)+(45)^F(90)&F](45)+(45)^F(90)&F]'

    terp.setStyle( 'normal' )
    terp.color( (0.4, 0.5, 0.6) )
    terp.place(0, 0, zpos=0 )
    terp.roll( -90 )
    terp.drawString(pyr, 50, 90 )


    terp.width(2)
    terp.setStyle( 'jitter' )
    terp.color( (0.6, 0.1, 0.7) )
    terp.place(150, 0, zpos=-200)
    terp.drawString(pyr, 70, 90 )

    terp.width(1)
    terp.setJitter( 5 )
    terp.color( (0.2, 0.5, 0.3) )
    terp.place(-230, 0, zpos=50)
    terp.drawString(pyr, 80, 90 )

    terp.hold()

if __name__ == '__main__':
    main()
