from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
a=0
b=0
class House:
    def __init__(self,data):
        self.x0=data[0]
        self.y0=data[1]
        self.z0=data[2]
    def setpattern(self,datafile):
        self.patterndata = []
        f = open("pattern.csv","r")
        data = f.read()
        rows = data.split("\n")
        for row in rows:
            self.patterndata.append(row.split(","))
        print(self.patterndata)
    def buildwall(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        for x in range(10):
            for y in range(10):
                mc.setBlock(x0+x,y0-1+y,z0,5)
        for x in range(10):
            for y in range(10):
                mc.setBlock(x0+x,y0-1+y,z0+10,5)
        for z in range(10):
            for y in range(10):
                mc.setBlock(x0,y0-1+y,z0+z,5)
        for z in range(10):
            for y in range(10):
                mc.setBlock(x0+10,y0-1+y,z0+z,5)
        for y in range(10):
            mc.setBlock(x0+10,y0-1+y,z0+10,5)
    def buildceiling(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0+x,y0+9,z0+z,45)
    def buildfloor(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        for x in range(10):
            for z in range(10):
                if self.patterndata[x][z] == "1":
                    mc.setBlock(x0+x,y0-1,z0+z,24,2)
                else:
                    mc.setBlock(x0+x,y0-1,z0+z,5)
        
        

house = House([pos.x,pos.y,pos.z])
house.setpattern("pattern.csv")
house.buildwall()
house.buildceiling()
house.buildfloor()
