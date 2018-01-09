import turtle_interpreter as ti
import lsystem as ls

def main():
	'''
	Draws 3 rows and 2 columns of 2 different trees. From left to right, the number of
	iterations of the trees that are defined by the L-system in treesystem1.txt and 
	treesystem2.txt of the L-system goes from 4 to 6 and from top to bottom, 
	the angle of the L-system in treesystem1.txt is 22 and 30. The angle of the L-system
	in treesystem2.txt is 25 and 35. For each tree whose L-system was defined in 
	treesystem1.txt, each tree is spaced 200 pixels apart in the x direction and 150 
	pixels in the y direction.For each tree whose L-system was defined in treesystem2.txt,
	each tree was spaced 100 m in the x direction and 150 m in the y direction.
	
	'''
	window=ti.TurtleInterpreter(1200,1200)
	x1=-400
	y01=0
	for i in range(4,7):
		x1+=200
		window.goto(x1,y01)
		for a in (22,30):
			if a==22:
				y1=y01
			else:
				y1+=-150
			window.place(x1,y1,90)
			Lsystem1=ls.Lsystem('treesystem1.txt')
			lstr1 = Lsystem1.buildString(i)
			window.drawString(lstr1, 2, a)
						
	x2=-250
	y02=y01
	for i in range(4,7):
		x2+=100
		window.goto(x2,y02)
		for a in (25,35):
			if a==25:
				y2=y02
			else:
				y2+=-150
			window.place(x2,y2,90)	
			
			Lsystem2=ls.Lsystem('treesystem2.txt')
			lstr2 = Lsystem2.buildString(i)
			window.drawString(lstr2, 1, a)
	window.hold()
	

if __name__=='__main__':
	main()