#Brandon Troisi
#test.py
#3/9/16

import time
import random
import graphicsPlus as gr

def main():
    win = gr.GraphWin("Press a key", 400, 400, False)
    shapes = []
    c = gr.Circle(gr.Point(250, 250, 10))
    c.draw(win)
      
    shapes.append(c)
      
    while True
        time.sleep(0.5)
        for thing in shapes:
            dx=random.randInt(-10,10)
            dy = random.randInt(-10,10)
            thing.move(dx,dy)
        
        win.update()
        
        if win.checkMouse()
            break
            
    win.close()    


if __name__ == "__main__":
    main()
