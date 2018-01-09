from turtle import *

def shapeD( distance ):
	forward( distance )
	left( 90 )
	forward( distance )
	left( 90 )
	forward( distance )
	left( 90 )
	forward( distance )
	left( 30 )
	forward( distance )
	left( 120 )
	forward( distance )

def shapeE():	
	shapeD( 50 )
	shapeD( 100 )
	shapeD( 150 )
	shapeD( 200 )

shapeE()
	

raw_input('Enter to continue')

