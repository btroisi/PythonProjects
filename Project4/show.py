#Brandon Troisi
#2/24/16
#show.py

import graphics
import display
import sys


def main (argv):
	if len(argv)<2:
		print "Usage : show.py filename"
		exit()
		
	file = argv[1]
	pm = graphics.Pixmap(file)
	
	print pm.getHeight(), ", ", pm.getWidth()
	
  	
	wn = display.displayPixmap(pm, file)
	wn.getMouse()
	
	
		
if __name__=="__main__":
	main(sys.argv)
	