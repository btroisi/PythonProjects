#Brandon Troisi
#4/19/16
#indoor.py

import lsystem 
import shapes
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
	
	'''Draws tree from L-system in file systemCL.txt'''
	Tree1=tree.Tree()
	Tree1.lsystem.read('systemCL.txt')
	Tree1.setIterations(3)
	Tree1.draw(-130,-70)
	
	'''Draws tree from L-system in filed systemFL.txt'''
	Tree2=tree.Tree()
	Tree2.lsystem.read('systemFL.txt')
	Tree2.setIterations(4)
	Tree2.draw(130,-70)
	
	
	'''Draws rectangular red base of house'''
	rect5=shapes.Rectangle()
	rect5.setDistance(100)
	rect5.setColor('red')
	rect5.draw(-35,-25,0.5,0)
	
	'''Draws black trapezoidal roof'''
	trap1=shapes.Trapezoid()
	trap1.setDistance(30)
	trap1.setColor('black')
	trap1.draw(-36,-25,1.7,0)
	
	'''Draws yellow hexagonal sun oriented at 90'''
	hex1=shapes.Hexagon()
	hex1.setDistance(60)
	hex1.setColor('yellow')
	hex1.draw(-170,65,0.3,90)
	
	'''Draws white parallelogram shaped-window on roof'''
	para1=shapes.Parallelogram()
	para1.setDistance(40)
	para1.setColor('white')
	para1.draw(7,0,0.2,0)
	
	raw_input("Enter to exit")


if __name__=='__main__':
	main()