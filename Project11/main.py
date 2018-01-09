import shapes
import turtle_interpreter as ti


def drawSquare(event=None):
	
	s=shapes.Square()
	
	terp=ti.TurtleInterpreter()
	(x,y,z) = terp.window2turtle(event.x, event.y)
	s.draw(x,y,1)
	
def main():
	terp=ti.TurtleInterpreter()
	terp.setRightMouseCallback(drawSquare)
	
if __name__=='__main__':
	main()
	raw_input('Enter to continue')