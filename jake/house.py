from mcpi.minecraft import Minecraft

import csv
mc=Minecraft.create()
pos=mc.player.getTilePos()


size=20


def house(size):
    mc.setBlocks(pos.x+3,pos.y+1,pos.z,pos.x+3+size,pos.y+5,pos.z+size,1)
    mc.setBlocks(pos.x+3,pos.y+3,pos.z,pos.x+3+size,pos.y+3,pos.z+size,89)
    mc.setBlocks(pos.x+4,pos.y+1,pos.z+1,pos.x+2+size,pos.y+4,pos.z+size-1,0)
    mc.setBlock(pos.x+3,pos.y+2,pos.z+round(size/2),0)
    mc.setBlock(pos.x+3,pos.y+1,pos.z+round(size/2),0)
    mc.setBlock(pos.x+3,pos.y+1,pos.z+round(size/2)-1,0)
    mc.setBlock(pos.x+3,pos.y+2,pos.z+round(size/2)-1,0)
    mc.setBlocks(pos.x+3,pos.y,pos.z,pos.x+3+size,pos.y,pos.z+size,17)
    for x in range(5):
        for z in range(5):
            mc.setBlock(pos.x+x+round(size/2+1),pos.y,pos.z+z+round(size/2-1.5),int(pattern[4-x][z])+17)
    

    

f=open("python.mc.csv",'r')
pattern = list(csv.reader(f))
#print(pattern)
house(size)





#pos.x=pos.x+15
#size=size+6


#house(size)

    

    

