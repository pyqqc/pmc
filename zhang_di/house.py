from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
a=0
b=0

x0=pos.x
y0=pos.y
z0=pos.z
w0=pos.x+20
l0=pos.y
h0=pos.z


def house (x0,y0,z0,w0,l0,h0):
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
    for x in range(10):
            for z in range(10):
                mc.setBlock(pos.x+x+a,pos.y,pos.z+z,17)
    for x in range(10):
            for z in range(10):
                mc.setBlock(pos.x+x+a,pos.y+10,pos.z+z,24,2)
    for v in range(15):
        for b in range(15):
            for n in range(15):
                mc.setBlock(w0+v,l0+b,h0+n,1)
    for d in range(13):
        for f in range(13):
            for g in range(13):
                mc.setBlock(w0+d,l0+f,h0+g,0)
    mc.setBlock(w0+4,l0+3,h0,20)
    mc.setBlock(w0+5,l0+3,h0,20)
    mc.setBlock(w0+4,l0+4,h0,20)
    mc.setBlock(w0+5,l0+4,h0,102)
                
                

house(x0,y0,z0,w0,l0,h0)



