from vpython import *
import math

canvas(width=1800,height=1000,center=vector(6,0,0), background=color.black)
wall=box(pos=vector(0,1,0), size=vector(0.2, 3, 2), color=color.yellow)
floor=box(pos=vector(6, -0.6, 0), size=vector(14, 0.2, 4), color=color.yellow)
Mass= box(pos=vector(12, 0, 0), velocity=vector(0, 0, 0), size=vector(1, 1, 1), mass=2.0, color=color.red)
pivot=vector(0,0,0)
spring= helix(pos=pivot, axis=Mass.pos-pivot, radius=0.4, constant=1.5, thickness=0.1,coils=20, color=color.white)
eq=vector(9,0,0)
t=0
dt=0.01
T = text(text='HORIZONTAL SPRING MASS SYSTEM', pos=vector(0,5,0), color=color.green, height=0.5)
print(T)
S = text(text='Mass=2 kg \nSpring Constant=1.5', pos=vector(0,4,0), color=color.green, height=0.3)
print(S)


while (t<500):
    rate(100)
    acc=(eq-Mass.pos)*(spring.constant/Mass.mass)
    Mass.velocity=Mass.velocity+acc*dt
    Mass.pos=Mass.pos+Mass.velocity*dt
    spring.axis=Mass.pos-spring.pos
    t = t+dt
