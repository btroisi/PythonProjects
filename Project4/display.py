# Proj 4
# Stephanie Taylor
# spring 2011

import graphics

# Open a new window, give it the specified title, 
# and display the pixmap 
# Input:
#		 pm : a Pixmap
#		 title : a string
# Output:
#		the window in which the pixmap is displayed
def displayPixmap(pm, title):
	w = pm.getWidth()
	h = pm.getHeight()
	win = graphics.GraphWin(title,w,h)
	# center the image in the window.
	# The first argument to the Image constructor is
	# the point at which we want to place the center of the image
	img = graphics.Image(graphics.Point(w/2.0,h/2.0),pm) 
	img.draw(win)
	return win

