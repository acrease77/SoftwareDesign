from swampy.TurtleWorld import *
from math import pi

world=TurtleWorld()
bob=Turtle()

def koch(t,x):
    bob.delay=0
    if x<3:
        fd(t,x)
        return
    angle=60
    koch(t,x/3.0)
    lt(t,angle)
    koch(t,x/3.0)
    rt(t,2*angle)
    koch(t,x/3.0)
    lt(t,angle)
    koch(t,x/3.0)

def snowflake(t,length,sides):
    for i in range(sides):
        koch(t,length)
        rt(t,360.0/sides)

snowflake(bob,500,3)
wait_for_user()

