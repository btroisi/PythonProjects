#Brandon Troisi
#4/13/16
#tree.py
#3D version

import lsystem as ls
import shapes


class Tree(shapes.Shape):
	'''Contains functions necessary to draw a tree'''
	def __init__(self, distance=1, angle=22.5, color=(0.5,0.4,0.3),iterations=3,
	filename=None):
		'''
		Initializes number of iterations, the L-system from which to draw the tree,
		the distance,the angle the turtle goes, and the color as a part of the shape class
		'''
		shapes.Shape.__init__(self,distance=100,angle=90,color=(0,0,0),istring = '')
		self.iterations=iterations
		self.lsystem=ls.Lsystem(filename)
		self.distance=distance
		self.angle=angle
		self.color=color
		
		
	def setIterations (self,iterations):
		'''
		Sets the number of iterations of the rule in the L-system
		'''
		self.iterations = iterations
		
	def read(self, filename):
		'''
		Reads the base and rules of the L-system from which to draw a tree
		'''
		ls.read('filename')
	
		
	def draw(self,xpos, ypos, scale, orientation=90, roll=0,ptich=0,zpos=0): 
		''''
		Draws a tree at (xpos,ypos), at scale scale with a default value of 1, and
		orientation orientation with a default value at 90 so the tree can grow up
		'''
		self.string= self.lsystem.buildString(self.iterations)
		shapes.Shape.draw(self, xpos, ypos, scale, 90)
		
		
	def test(self,filename):
		'''
		Test function that creates a tree object from the L-system in filename filename
		and creates 5 iterations and draws three different trees at (-200,-200),(-20,30),
		and (140,80). 
		'''
		
		Tree1=Tree(filename=filename)
		Tree1.setIterations(5)
		
	
	
		Tree1.draw(-200,-200)
		Tree1.draw(-20,-30)
		Tree1.draw(140,-80)
		raw_input("Press enter to exit")

def main():
	'''
	Creates an empty tree object and passes the filename systemH.txt into the test 
	function so 3 trees are constructed based on multiple replacements in the L-system
	in the file systemH.txt
	'''
	tree=Tree()
	tree.test('systemH.txt')

if __name__ =='__main__':
	main()
		
		
	
		
	
		