import turtle_interpreter as ti
import lsystem as ls

def main()
	window=ti.TurtleInterpreter(800,800)
	x=-50
	y0=10
	for i in range(2,6):
		x+=25
		window.goto(x,y0)
		for a in (22,25,30):
			if a==22:
				y=y0
			else:
				y+=-10
			window.goto(x,y)
			window.place(x,y,90)
			Lsystem2=ls.Lsystem('treesystem2.txt')
			lstr2 = Lsystem2.buildString(i)
			window.drawString(lstr2, 2, a)

if __name__=='__main__'
	main()