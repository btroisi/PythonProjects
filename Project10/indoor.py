#Brandon Troisi
#indoor.py

import shapes
import turtle_interpreter as ti
import tree

def main():
	'''
	Draws a painting of a house with two trees, a hexagonal sun, 
	a parallelogram window, and grass
	'''

	'''Draws the frame of the painting'''
	rect1=shapes.Rectangle()
	rect1.setColor('brown')
	rect1.draw(-200,100,2.1,0)
	
	'''Draws the light blue sky inside frame of painting'''
	rect2=shapes.Rectangle()
	rect2.setColor('lightblue')
	rect2.draw(-190,95,2.0,0)
	
	'''Draws left half of green grass'''
	rect3=shapes.Rectangle()
	rect3.setDistance(100)
	rect3.setColor('green')
	rect3.draw(-190,-5,1.0,0)
	
	'''Draws right half of green grass'''
	rect4=shapes.Rectangle()
	rect4.setDistance(100)
	rect4.setColor('green')
	rect4.draw(10,-5,1.0,0)
	
	'''
	Draws tree from L-system in file lsys1.txt in whateverstyle the user inputs
	'''
	
	print("Hello, welcome to the painting: Here you can paint a scene with trees, a house, a sun, and a window any way you want")
	
	Tree1=tree.Tree()
	Tree1.lsystem.read('lsys1.txt')
	Tree1.setIterations(3)
	answer1=raw_input("What style would you like for the first tree: " )
	Tree1.setStyle(answer1)
	for i in ('jitter', 'jitter3'):	
		if answer1 == i:
			'''
			If the style user input is either jitter or jitter 3 the tree
			is drawn in that style with whatever jitter value user inputs
			'''
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first tree: "))
			Tree1.setJitter(jitteranswer1)
	
	
	
	
	Tree1.draw(-130,-70,1)
	
	'''
	Draws tree from L-system in file sysTree3.txt, in whatever style the user inputs
	
	'''
	Tree2=tree.Tree()
	Tree2.lsystem.read('sysTree3.txt')
	Tree2.setIterations(4)
	answer2=raw_input("What style would you like for the second tree: " )
	Tree2.setStyle(answer2)
	for i in ('jitter', 'jitter3'):	
		if answer2 == i:
			'''
			If the style user input is either jitter or jitter 3 the tree
			is drawn in that style with whatever jitter value user inputs
			'''
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the second tree: "))
			Tree1.setJitter(jitteranswer1)
	
	Tree2.draw(130,-40,1)
	
	
	'''Draws rectangular red base of house in whatever style user inputs'''
	rect5=shapes.Rectangle()
	rect5.setDistance(100)
	rect5.setColor('red')
	answer3=raw_input("What style would you like for the house: " )
	rect5.setStyle(answer3)
	for i in ('jitter', 'jitter3'):	
		if answer3 == i:
			'''
			If the style user inputs is either jitter or jitter 3 jitter for all sides
			of house drawn is controlled by user input
			'''
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			rect5.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			rect5.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			rect5.setJitter(jitteranswer3)
			jitteranswer4 = float(raw_input("What would you like the jitter to be for the fourth side: "))
			rect5.setJitter(jitteranswer4)
	rect5.draw(-35,-25,0.5,0)
	
	'''Draws black trapezoidal roof in whatever style user inputs'''
	trap1=shapes.Trapezoid()
	trap1.setDistance(30)
	trap1.setColor('black')
	answer4=raw_input("What style would you like for the roof: " )
	trap1.setStyle(answer4)
	for i in ('jitter', 'jitter3'):	
		if answer4 == i:
			'''
			If the style user inputs is either jitter or jitter 3 jitter for all sides
			of roof drawn is controlled by user input
			'''
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			trap1.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			trap1.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			trap1.setJitter(jitteranswer3)
			jitteranswer4 = float(raw_input("What would you like the jitter to be for the fourth side: "))
			trap1.setJitter(jitteranswer4)
			
	trap1.draw(-36,-25,1.7,0)
	
	'''Draws yellow hexagonal sun oriented at 90 in whatever style user inputs'''
	hex1=shapes.Hexagon()
	hex1.setDistance(60)
	hex1.setColor('yellow')
	answer5=raw_input("What style would you like for the sun: " )
	hex1.setStyle(answer5)
	for i in ('jitter', 'jitter3'):	
		if answer5 == i:
			'''
			If the style user inputs is either jitter or jitter 3 jitter for all sides
			of sun drawn is controlled by user input
			'''
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side: "))
			hex1.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			hex1.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			hex1.setJitter(jitteranswer3)
			jitteranswer4 = float(raw_input("What would you like the jitter to be for the fourth side: "))
			hex1.setJitter(jitteranswer4)
			jitteranswer5 = float(raw_input("What would you like the jitter to be for the fifth side: "))
			hex1.setJitter(jitteranswer5)
			jitteranswer6 = float(raw_input("What would you like the jitter to be for the sixth side: "))
			hex1.setJitter(jitteranswer6)
		
	
	hex1.draw(-170,65,0.3,90)
	
	'''Draws white parallelogram shaped-window on roof in whatever style user inputs'''
	para1=shapes.Parallelogram()
	para1.setDistance(40)
	para1.setColor('white')
	answer6=raw_input("What style would you like for the window: " )
	para1.setStyle(answer6)
	for i in ('jitter', 'jitter3'):	
		if answer6 == i:
			'''
			If the style user inputs is either jitter or jitter 3 jitter for all sides
			of the paralellogram shaped window drawn is controlled by user input
			'''
			jitteranswer1 = float(raw_input("What would you like the jitter to be for the first side : "))
			para1.setJitter(jitteranswer1)
			jitteranswer2 = float(raw_input("What would you like the jitter to be for the second side: "))
			para1.setJitter(jitteranswer2)
			jitteranswer3 = float(raw_input("What would you like the jitter to be for the third side: "))
			para1.setJitter(jitteranswer3)
			jitteranswer4 = float(raw_input("What would you like the jitter to be for the fourth side: "))
			para1.setJitter(jitteranswer4)
	para1.draw(7,0,0.2,0)
	
	raw_input("Enter to exit")


if __name__=='__main__':
	main()