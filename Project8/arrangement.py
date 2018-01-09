#Brandon Troisi
#arrangement.py

import lsystem as ls
import turtle_interpreter as ti

def main():
	'''
	This draws an arrangement of 4 trees, a house, a sky, grass, and a sun.
	There are two trees to the left of the house and two trees to the right. 
	The two trees to the left, from left to right are the tree defined by the 
	L-system in the systemFL.txt file iterated 5 times and the tree defined by 
	L-system in the the systemDL.txt file iterated 3 times. The two trees to the
	right of the house from left to right are the tree defined by the L-system in 
	in the systemGL.txt file and iterated 9 times the tree defined by the L-system in the 
	systemDL.txt file iterated 5 times. The house has a square red base, a triangular 
	black roof, a yellow door, and a square window. The sky and grass are rectangles that 
	fill the top and bottom half of the window respectively. The sun was drawn at position 
	(200,190) with a radius of 35. 
	
	'''
	
	'''
	Draws the sky
	'''
	window=ti.TurtleInterpreter(800,800)
	window.place(-400,0,0)
	window.drawString('fsFF+F+FF+F+n', 400, 90)
	
	'''
	Draws the tree defined by the L-system in the system.DL file at (-100,0) where the  
	rules were iterated 3 times at an angle of 22 degrees
	'''
	window.place(-100,0,90)
	window.color('brown')
	Lsystem1=ls.Lsystem('systemDL.txt')
	lstring1=Lsystem1.buildString(3)
	window.drawString(lstring1,10,22)
	
	'''
	Draws the tree defined by the L-system in the system.GL file at (100,0) where the 
	rules were iterated 9 times at an angle of 22 degrees
	'''
	window.place(100,0,90)
	Lsystem2=ls.Lsystem('systemGL.txt')
	lstring2=Lsystem2.buildString(9)
	window.drawString(lstring2, 2, 30)
	
	'''
	Draws the tree defined by the L-system in the system.FL file at (-200,0) where the 
	rules were iterated 5 times at an angle of 22 degrees
	'''
	window.place(-200,0,90)
	Lsystem3=ls.Lsystem('systemFL.txt')
	lstring3=Lsystem3.buildString(5)
	window.drawString(lstring3, 2, 22)
	
	'''
	Draws the tree defined by the L-system in the system.GL file at (200,0) where the 
	rules were iterated 5 times at an angle of 22 degrees
	'''
	window.place(200,0,90)
	Lsystem4=ls.Lsystem('systemDL.txt')
	lstring4=Lsystem4.buildString(5)
	window.drawString(lstring4, 2, 22)
	
	'''
	Draws the red base of the house
	'''
	window.place(-15,0,0)
	window.drawString('fRF+F+F+F+n',44,90)
	
	'''
	Draws the black roof of the house
	'''
	window.place(-15,44,0)
	window.drawString('fbF+F+F+n', 44, 120)
	
	'''
	Draws the yellow door of the house
	'''
	window.place(1.5,0,0)
	window.drawString('fyF+FF+F+FF+n', 10, 90)
	
	'''
	Draws the black window above the door
	'''
	window.place(1.5, 25, 0)
	window.drawString('fbF+F+F+F+n', 10, 90)
	
	'''
	Draws the grass
	'''
	window.place(-400,-400,0)
	window.drawString('fgFF+F+FF+F+n',400,90)
	
	'''
	Draws the sun at (200,190) with radius 35
	'''
	window.sun(200,190,35)
	
	window.hold()
	
if __name__=='__main__':
	main()