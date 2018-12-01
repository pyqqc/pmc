from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()

def stick(X,Z,a):
    for y in range(256):
        mc.setBlock(X,189-y,Z,a)
    time.sleep(0.1)   

def square(X,Z,L,a):
    for x in range(2*L+1):
        stick(X-L+x,Z-L,a)
        stick(X-L+x,Z+L,a)
    for z in range(2*L+1):
        stick(X-L,Z-L+z,a)
        stick(X+L,Z-L+z,a)
        
def empty(X,Z,L):
    stick(X,Z,7)
    for l in range(L):
        square(X,Z,1+l,7)
        square(X,Z,l,0)
        print(l)
    square(X,Z,L,0)
    
empty(pos.x,pos.z,100)
