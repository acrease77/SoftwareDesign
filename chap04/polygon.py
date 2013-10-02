from swampy.TurtleWorld import *
from math import pi

world=TurtleWorld()

bob=Turtle()

bob.delay=.01

def square(t,length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob,5)

def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)

polygon(bob,100,8)

def circle(t,r):
    circ=2*pi*r
    n=360
    len=circ/n
    for i in range(n/2):
        fd(t,len)
        lt(t,360/n)

circle(bob,40)       

def arc(t,r,angle):
    circ=2*pi*r
    n=360
    len=circ/n
    for i in range(360*angle/n):
        fd(t,len)
        lt(t,360/n)
    
arc(bob,40,90)


