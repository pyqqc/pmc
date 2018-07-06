from mcpi.minecraft import Minecraft
import time
import mcpi.vec3 as vec3


mc=Minecraft.create("192.168.0.155",4711)
pos=vec3.Vec3(1,15,102)
a=0
b=0
c=0
x0=pos.x
y0=pos.y
z0=pos.z

def bomb (x0,y0,z0):
    for y in range(1):
        for x in range(1):
            for z in range(1):
                mc.setBlock(x0+x,y0+y,z0+z,46)
    for x in range(1):
            for z in range(1):
                mc.setBlock(pos.x+x+a,pos.y+1,pos.z+z,46)




for c in range(1000):
    if a <= 500:
        if b <= 500:
            bomb(x0+a,y0+b,z0)
            a = a+5
            b = b+5
            time.sleep(0.1)

