from turtle import *

def shapeA():
   right(90)
   backward(100)
   forward(50)
   right(90)
   forward(50)
   left(90)
   forward(50)

def shapeB():
   forward(100)
   backward(50)
   right(90)
   forward(100)

def shapeC():
   shapeA()
   forward( 100 )
   shapeB()


shapeC()
raw_input('Enter to continue')

