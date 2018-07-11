from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()


mc=Minecraft.create()
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
                mc.setBlock(pos.x+x+a,pos.y+1,pos.z+z,152)




for c in range(1000):
    if a <= 100:
        if b <= 100:
            bomb(x0+a*2,y0,z0+b*2)
            time.sleep(0.1)

