

from mcpi.minecraft import Minecraft

import csv
mc=Minecraft.create()
pos=mc.player.getTilePos()

f=open("mcHouse.csv",'r')
csvreader=csv.reader(f)
mcHouse_data=list(csvreader)


f=open("python.mc.csv",'r')
pattern = list(csv.reader(f))



class mchouse:
    def __init__(self, data):
        self.data = data
        self.length=int(data[0][0])
        self.wide=int(data[0][1])
        self.height=int(data[0][2])
        

    def house(self):
        x=self.length
        z=self.wide
        y=self.height
        mc.setBlocks(pos.x+3,pos.y+1,pos.z,pos.x+3+x,pos.y+y,pos.z+z,1)
        mc.setBlocks(pos.x+3,pos.y+3,pos.z,pos.x+3+x,pos.y+y-2,pos.z+z,89)
        mc.setBlocks(pos.x+4,pos.y+1,pos.z+1,pos.x+2+x,pos.y+y-1,pos.z+z-1,0)
        mc.setBlock(pos.x+3,pos.y+2,pos.z+round(z/2),0)
        mc.setBlock(pos.x+3,pos.y+1,pos.z+round(z/2),0)
        mc.setBlock(pos.x+3,pos.y+1,pos.z+round(z/2)-1,0)
        mc.setBlock(pos.x+3,pos.y+2,pos.z+round(z/2)-1,0)
        mc.setBlocks(pos.x+3,pos.y,pos.z,pos.x+3+x,pos.y,pos.z+z,17)
        for a in range(5):
            for c in range(5):
                mc.setBlock(pos.x+a+round(x/2+1),pos.y,pos.z+c+round(z/2-1.5),int(pattern[4-a][c])+17)

myhouse=mchouse(mcHouse_data)
myhouse.house()
