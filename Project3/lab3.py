#Brandon Troisi
#Feb 2016
#lab3.py

import turtle
import random
import sys

def star2( rays, size ):    
    for i in range(rays):
        turtle.setheading( i*360/rays )
        turtle.forward( size )
        turtle.backward( size )

def main():
    N = 20
    M = 40
    if len( sys.argv ) > 2:
        N = int( sys.argv[1] )
        M = int( sys.argv[2] )
    star2(N,M) 
    raw_input('Enter')
    
if __name__ == "__main__":
    main()


    
