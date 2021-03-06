from swampy.TurtleWorld import *
world=TurtleWorld()
bob=Turtle()
bob.delay=0

def hilbert_a(t,n):
    a=3.0
    if n<a:
        fd(t,n)
        return    
    lt(t)
    hilbert_b(t,n/a)
    fd(t,a)    
    rt(t)
    hilbert_a(t,n/a)
    fd(t,a)
    hilbert_a(t,n/a)
    rt(t)
    fd(t,a)
    hilbert_b(t,n/a)
    lt(t)

def hilbert_b(t,n):
    a=3.0
    if n<a:
        fd(t,n)
        return    
    rt(t)
    hilbert_a(t,n/a)
    fd(t,a)
    lt(t)
    hilbert_b(t,n/a)
    fd(t,a)
    hilbert_b(t,n/a)
    lt(t)
    fd(t,a)
    hilbert_a(t,n/a)
    rt(t)

hilbert_a(bob,1200)
wait_for_user()
    
