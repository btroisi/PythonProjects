#Brandon Troisi
#scene.py
#3/17/15

import time
import graphicsPlus as gr
import shape_group as sg

def saveFrame( basename, win, frame ):
    win.postscript( file="%s_%000d.ps"%(basename,frame), colormode='color')

def main():
	""" 
	Creates a window and plots a scene with a tank blowing up a vehicle
	"""
	win = gr.GraphWin( 'title', 500, 500, False )
 
	tank = sg.tank_init( 10, 400, 1.0 )
	
	vehicle = sg.vehicle_init( 300, 350, 1.0 )
	
	bullet = sg.bullet_init( 10, 400, 1.0 )
	
	explosion = sg.explosion_init( 350, 400, 1.0 )
	
	sg.draw(bullet,win) 
	sg.draw(tank,win)
	sg.draw(vehicle,win)
	
	
	
	t = 0
	while t<3: 
		'''
		Draws the vehicle moving to the right and the bullet hitting the car
		'''
		t+=1
		time.sleep( 0.25 )
		sg.vehicle_animation_frame( vehicle, t, win )
		sg.bullet_animation_frame( bullet, t, win )
		win.update()
		if win.checkMouse():
			break
	sg.draw(explosion,win)
		
	while 4>t>=3:
		'''
		Draws the vehicle exploding
		'''
		t+=1
		sg.undraw(bullet)
		sg.undraw(vehicle)
		win.update()
		sg.explosion_animation_frame( explosion, t, win)
		win.update()
		if win.checkMouse():
			break
			
	while t>=4:
		'''
		Undraws the explosion
		'''
		t+=1
		sg.undraw(explosion)	
		if win.checkMouse():
			break	
	
    saveFrame( 'project6testmovie', win, t )     
	win.update()
 
	win.getMouse()
	win.close()

if __name__ == "__main__":
    main()


        
