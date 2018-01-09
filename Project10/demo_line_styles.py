#Brandon Troisi
#demo_line_styles.py

import turtle_interpreter as ti
import shapes 
import random
import turtle

def main():
	""" 
	Draws one normal triangle, two jittered triangles, and a dotted triangle. The 
	style for each triangle is controlled by user input
	
	"""

	terp = ti.TurtleInterpreter()
	t = shapes.TriangleU()
	
	'''First triangle is drawn in whatever style user inputs '''
	print("Hello welcome to the triangle factory, this produces four triangles in the following styles normal, normal1, jitter, jitter3, and dot")
	
	answer1=raw_input("What style would you like for the first triangle: " )
	t.setStyle(answer1)

	
	for i in ('jitter', 'jitter3'):	
		'''
		If the user chooses the style to be jitter or jitter 3
		the jitter value for each side is controlled by user input
		'''
		if answer1 == i:
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			t.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			t.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			t.setJitter(jitteranswer3)
			
	
		
	
	#Draws triangle of size 100 at (-200,-100)
	t.draw(-200,-100,1)

	'''Second triangle is drawn in whatever style user inputs '''
	answer2=raw_input("What style would you like for the second triangle: ")
	t.setStyle( answer2 )
	
	for i in ('jitter', 'jitter3'):	
		'''
		If the user chooses the style to be jitter or jitter 3
		the jitter value for each side is controlled by user input
		'''
		if answer2 == i:
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			t.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			t.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			t.setJitter(jitteranswer3)
	
	
	
	#Draws triangle of size 100 at (-200,100)				
	t.draw(-200,100,1)

	'''Third triangle is drawn in whatever style user inputs '''
	answer3=raw_input("What style would you like for the third triangle: ")
	t.setStyle( answer3 )
	for i in ('jitter', 'jitter3'):	
		'''
		If the user chooses the style to be jitter or jitter 3
		the jitter value for each side is controlled by user input
		'''
		if answer3 == i:
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			t.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			t.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			t.setJitter(jitteranswer3)
	
	
	
	#Draws triangle of size 100 at (100,-100)	
	t.draw(100,-100,1)
	
	
	'''Fourth triangle is drawn in whatever style user inputs '''
	answer4=raw_input("What style would you like for the fourth triangle: ")
	t.setStyle( answer4 )
	
	for i in ('jitter', 'jitter3'):	
		'''
		If the user chooses the style to be jitter or jitter 3
		the jitter value for each side is controlled by user input
		'''
		if answer4 == i:
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			t.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			t.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			t.setJitter(jitteranswer3)
	
	
	#Draws triangle of size 100 at (100,100)
	t.draw(100, 100, 1)
	
	
	
	

	terp.hold()
	
	

if __name__ == "__main__":
	main()