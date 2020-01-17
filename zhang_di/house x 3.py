from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

x0=pos.x
y0=pos.y
z0=pos.z

def house (x0,y0,z0):
    for y in range(10):
        for x in range(10):
            for z in range(10):
                mc.setBlock(x0+x,y0+y,z0+z,5)
    for x in range(8):
        for y in range(8):
            for z in range(8):
                mc.setBlock(x0+x+1,y0+y+1,z0+z+1,0)

    mc.setBlock(x0+4,y0+3,z0,102)
    mc.setBlock(x0+5,y0+3,z0,102)
    mc.setBlock(x0+4,y0+4,z0,102)
    mc.setBlock(x0+5,y0+4,z0,102)
    mc.setBlock(x0,y0+3,z0+4,102)
    mc.setBlock(x0,y0+3,z0+5,102)
    mc.setBlock(x0,y0+4,z0+4,102)
    mc.setBlock(x0,y0+4,z0+5,102)
    mc.setBlock(x0+9,y0+3,z0+4,102)
    mc.setBlock(x0+9,y0+3,z0+5,102)
    mc.setBlock(x0+9,y0+4,z0+4,102)
    mc.setBlock(x0+9,y0+4,z0+5,102)
    mc.setBlock(x0+4,y0+3,z0+9,102)
    mc.setBlock(x0+4,y0+4,z0+9,102)
    mc.setBlock(x0+5,y0+3,z0+9,102)
    mc.setBlock(x0+5,y0+4,z0+9,102)
    mc.setBlock(x0,y0+1,z0+2,0)
    mc.setBlock(x0,y0+2,z0+2,0)
    mc.setBlock(x0-1,y0+1,z0+2,53)
    mc.setBlock(x0-1,y0,z0+2,17)
    mc.setBlock(x0-2,y0,z0+2,53)
    mc.setBlock(x0+4,y0+1,z0+4,89)
    mc.setBlock(x0+4,y0+1,z0+5,89)
    mc.setBlock(x0+5,y0+1,z0+4,89)
    mc.setBlock(x0+5,y0+1,z0+5,89)
    
    
    for x in range(10):
            for z in range(10):
                mc.setBlock(x0+x,y0,z0+z,17)
                mc.setBlock(x0+x,y0+10,z0+z,24,2)
                mc.setBlock(x0+x,y0+10,z0-1,128)
                mc.setBlock(x0+x,y0+10,z0+10,128)
                mc.setBlock(x0-1,y0+10,z0+z,128)
                mc.setBlock(x0+10,y0+10,z0+z,128)
                mc.setBlock(x0+x,y0+11,z0+z,24)

    for y in range(10):
         mc.setBlock(x0,y0+y,z0,17,2)
         mc.setBlock(x0+9,y0+y,z0,17,2)
         mc.setBlock(x0,y0+y,z0+9,17,2)
         mc.setBlock(x0+9,y0+y,z0+9,17,2)

for i in range(0,51,25):
     house(x0+i,y0,z0)
         
    
    
