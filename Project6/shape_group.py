#Brandon Troisi
#shape_group.py
#3/9/16

import time
import random
import graphicsPlus as gr

def steam_init(x,y,scale):
    '''
    Creates a list of objets needed to draw a steam plant at position (x,y) 
    with given scale
    '''
    
    shapes = []
    plant = gr.Rectangle(gr.Point(x,y),gr.Point(x+scale*100,y-scale*30))
    grey = gr.color_rgb(185,185,185)
    plant.setFill(grey)
    shapes.append(plant)
    
    roof = gr.Rectangle(gr.Point(x-scale*1, y-scale*30), gr.Point(x+scale*101,y-scale*40))
    ltbrown = gr.color_rgb(176,133,85)
    roof.setFill(ltbrown)
    shapes.append(roof)
    
    smokestack = gr.Rectangle(gr.Point(x,y),gr.Point(x+scale*10,y-scale*100))
    rstbrwn = gr.color_rgb(136,96,90)
    smokestack.setFill(rstbrwn)
    shapes.insert(0, smokestack)
    
    return shapes
    
def tank_init(x,y,scale):
	'''
	Creates list of objects needed to draw a tank at position (x,y) with given scale
	'''
	
	shapes1=[]
	base = gr.Rectangle(gr.Point(x,y),gr.Point(x+scale*100,y-scale*30))
	green = gr.color_rgb(0,150,0)
	base.setFill(green)
	shapes1.append(base)
	cannonhouse=gr.Rectangle(gr.Point(x+scale*1.1,y-scale*30),
	gr.Point(x+scale*95 ,y-scale*50))
	darkergreen = gr.color_rgb(0,120,0)
	cannonhouse.setFill(darkergreen)
	shapes1.append(cannonhouse)
	cannon=gr.Rectangle(gr.Point(x+scale*95,y-scale*37),gr.Point(x+scale*120,y-scale*45))
	darkestgreen = gr.color_rgb(0,90,0)
	cannon.setFill(darkestgreen)
	shapes1.append(cannon)
	
	return shapes1
	
def vehicle_init(x,y,scale):
	'''
	Creates list of objects needed to draw a tan armored vehicle at posiiton (x,y)
	with given scale
	'''
	shapes2=[]
	vehicle = gr.Rectangle(gr.Point(x*scale+100,y+scale*30),
	gr.Point(x+scale*30,y-scale*1))
	tan = gr.color_rgb(255,239,219)
	vehicle.setFill(tan)
	shapes2.append(vehicle)
	leftwheel=gr.Circle(gr.Point(x+scale*44,y+scale*40),9*scale)
	black = gr.color_rgb(0,0,0)
	leftwheel.setFill(black)
	shapes2.append(leftwheel)
	rightwheel=gr.Circle(gr.Point(x+scale*88,y+scale*40),9*scale)
	rightwheel.setFill(black)
	shapes2.append(rightwheel)
	
	return shapes2
	
def bullet_init(x,y,scale):
	shapes3=[]
	bullet=gr.Rectangle(gr.Point(x+scale*100,y-scale*39),
	gr.Point(x+scale*115,y-scale*44))
	yellowbullet=gr.color_rgb(200,200,0)
	bullet.setFill(yellowbullet)
	shapes3.append(bullet)
	
	return shapes3
	
def explosion_init(x,y,scale):
    shapes4=[]
    explosion=gr.Circle(gr.Point(x+35*scale,y-scale*9),100)
    redexp=gr.color_rgb(255,0,0)
    explosion.setFill(redexp)
    shapes4.append(explosion)
    
    
    return shapes4
    
    

def steam_animation_frame( shapes, frame_num, win ):
    '''
    Draw one frame of a steam plant animation. The animation will
    involve smoke rising out of the chimney.
    shapes is a list containing the graphics objects needed to draw
    the steam plant.
    frame_num is a number indicating which frame of the animation
    it is. win is the GraphWin object containing the scene.
	This animates by creating up to 20 steam circles. Each circle
    creeps up the screen until it gets to the top, when it is
    brought back down to the smokestack so it can be used again.
    '''
    
    p1 = shapes[0].getP1()
    p2 = shapes[0].getP2()
    
    dx = p2.getX() - p1.getX()
    newx = (p1.getX() + p2.getX())*0.5
    newy = p2.getY() - dx*0.5
    
    if frame_num%2 == 0 and len(shapes) < 20:
        c = gr.Circle(gr.Point(newx,newy,),0.4*dx)
        grey = gr.color_rgb(185,185,185)
        c.setFill(grey)
        c.draw(win)
        shapes.append(c)
        
    for item in shapes[3:]:
        item.move(0,-20)
        center = item.getCenter()
        
    	if center.y < 0:
        	mx = newx - center.getX()
        	my = newy - center.getY()
        	item.move(mx,my)
        
def vehicle_animation_frame( shapes2, frame_num, win ):
	'''
	Draws tan vehicle trying to escape from tank
	'''
  
	if frame_num<120:    
		for item in shapes2:
			item.move(17,0)

        
def bullet_animation_frame( shapes3, frame_num, win ):
	'''
	In vehicle's unsuccessful attempt to escape tank, bullet reahces tank
	'''
    
	if frame_num<120:
		for item in shapes3:
			item.move(91,0)
			
def explosion_animation_frame( shapes4, frame_num, win ):
	'''
	After bullet has reached vehicle there is a huge explosion
	'''
	
	for item in shapes4:
		orangeexp=gr.color_rgb(255,165,0)
		item.setFill(orangeexp)
		yellowexp=gr.color_rgb(255,255,0)
		item.setFill(yellowexp)
		         
       
def draw( objlist, win):
    '''
    Draw all fo the objects in objlist in the window
    '''
    for thing in objlist:
        thing.draw(win)
    
def move( objlist, dx, dy ):
    '''
    Draw all of the objects in objlist by dy in x direction
    '''
    for item in objlist:
        item.move(dx,dy)
        
def undraw( objlist ):
    '''
    Undraw all of the objects in list
    '''
    for thing in objlist:
        thing.undraw()
        
def test_steam():
      """ 
      Create a window and plot a scene with a picture 
      of a steam plant in it.
      """
      win = gr.GraphWin( 'title', 400, 400, False )

      steamplant = steam_init( 100, 300, 1.0 )

      draw(steamplant,win)
        
      win.update()

      win.getMouse()
      win.close()
      
      for frame_num in range(100):
        time.sleep( 0.25 )
        steam_animation_frame( steamplant, frame_num, win )
        win.update()
        if win.checkMouse():
            break

