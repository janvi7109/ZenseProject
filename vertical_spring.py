from vpython import *

canvas(center=vector(6,0,0), height=1000, width=1800, background=color.black)
Mass = box(pos=vector(6, -12, 0), velocity=vector(0, 0, 0), size=vector(1, 1, 1), mass=2.5, color=color.red)
wall = box(pos=vector(6, 2, 0), size=vector(3, 0.3, 2.5), color=color.yellow)
pivot = vector(6,2,0)
spring = helix(pos=pivot, axis=Mass.pos-pivot, radius=0.3, constant=2, thickness=0.2, coils=25, color=color.white)
equilibrium_pos=vector(6, -9, 0)
t=0
dt=0.01
T = text(text='VERTICAL SPRING MASS SYSTEM', pos=vector(0,7,0), color=color.green, height=0.7)
print(T)
S = text(text='Mass = 2.5kg \nSpring Constant = 2', pos=vector(0,5,0), color=color.green, height=0.5)
print(T)
while(t<600):
    rate(100)
    acc = (equilibrium_pos-Mass.pos)*(spring.constant/Mass.mass)
    Mass.velocity=Mass.velocity+acc*dt
    Mass.pos=Mass.pos+Mass.velocity*dt
    spring.axis=Mass.pos-spring.pos
    t = t+dt
