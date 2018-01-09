from turtle import *


print("Hello, welcome to the polygon factory, here we make polygons of all shapes and sizes.")		
distance = int(input("How large would you like the sides of your polygon to be? "))
n = int(input("How many sides would you like your polygon to have? "))
	
for ngon in range( 0, n ):
	forward( distance )
	left ( 360./n )

raw_input('Here is your polygon, have a nice day! (Press enter to leave the polygon factory.)')		
