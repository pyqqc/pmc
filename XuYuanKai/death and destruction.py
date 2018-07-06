
from mcpi.minecraft import Minecraft
import time
import mcpi.vec3 as vec3


mc=Minecraft.create("192.168.0.155",4711)
pos=vec3.Vec3(1,15,102)
a=0
b=0

x0=pos.x
y0=pos.y
z0=pos.z

def nuke (x0,y0,z0):
    for y in range(10):
        for x in range(10):
            for z in range(10):
                mc.setBlock(x0+x,y0+y,z0+z,46)
    for x in range(1):
            for z in range(1):
                mc.setBlock(pos.x+x+a,pos.y+11,pos.z+z,51)




for b in range(1000):
    if a <= 140:
        nuke(x0+a,y0,z0)
        a = a+14
