#Brandon Troisi
#3Dscene.py


import shapes



def stack(x,y,z,distance,color,style):
	'''
	Creates a stack of cubes at position (x,y,z) with color color and style style. The
	first cube has a size of distance and the size of the cube decreases by 1/2 until it 
	reaches 50.
	'''
	s=shapes.cube()
	if distance<50:
		return
	else:
		s.setDistance(distance)
		s.setStyle(style)
		s.setColor(color)
		s.draw(x, y, 1.0, 0,0,0,z)
		distance=distance*0.5
		stack(x+distance,distance+y+distance,z+distance,distance,color,style)
		
def mon(x,y,z,scale,color,style):
	'''
	Creates a monument at position (x,y,z) with color color and style style. 
	'''
	m=shapes.monument()
	m.setColor(color)
	m.setStyle(style)
	m.draw(x,y,scale,0,0,0,z)


def scene():
	'''
	Creates a scene with a stack of 3 blue cubes that are drawn in normal size at
	(0,-300,-100) whose sizes are 200,100, and 50 as you go up the stack. Also draws a tan 
	monument on top of the smallest cube in the first stack. Next a stack of 2 red cubes 
	are drawn in size jitter at(-200,-300,0), the size of those cubes are from bottom to
	top 150 and 75. On top of that stack, a yellow monument is drawn in style jitter.
	Then draws a single green cube of size 99 in style jitter3 at (-350,-300,0). Draws
	a purple monument on top of this cube in style jitter3. The scale at which the 
	monument was drawn went 4,3,2 as a stack of 3, 2, and 1 cubes were drawn. 
	'''
	stack(0,-300,-100,200,'blue','normal')
	mon(150,50,0,4,'tan','normal')
	stack(-200,-300,0,150,'red','jitter')
	mon(-90,-75,-50,3,'yellow','jitter')
	stack(-350,-300,0,99,'green','jitter3')
	mon(-270,-200,-50,2,'purple','jitter3')

if __name__=='__main__':
	scene()
	raw_input('Press enter to exit')