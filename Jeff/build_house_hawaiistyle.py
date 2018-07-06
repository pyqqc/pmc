from mcpi.minecraft import Minecraft
import binvox_rw
import time
import csv
import mcpi.vec3 as vec3
import mcpi.block as block

class House:
    def __init__(self,data,mc):
        self.mc=mc
        self.x0 = data[0]
        self.y0 = data[1]
        self.z0 = data[2]
        self.housedata=[]    
    def buildwall(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        mc=self.mc
        for y in range(5):    
            for x in range(10):
                mc.setBlock(x0+x,y0-2+y,z0,17)

            for z in range(9):
                mc.setBlock(x0,y0-2+y,z0+z,17)

            for x in range(9):
                mc.setBlock(x0+x,y0-2+y,z0+9,17)

            for z in range(10):
                mc.setBlock(x0+9,y0-2+y,z0+z,17)

        for y in range(3):
            for x in range (2):
                mc.setBlock(x0+3+x,y0-1+y,z0,0)

        for x in range(10):
            mc.setBlock(x0+x,y0+2,z0,89)

        for z in range(9):
            mc.setBlock(x0,y0+2,z0+z,89)
        
        for x in range(9):
            mc.setBlock(x0+x,y0+2,z0+9,89)

        for z in range(10):
            mc.setBlock(x0+9,y0+2,z0+z,89)
            
    def buildfloor(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        mc=self.mc
        for z in range(10):   
            for x in range(10):
                mc.setBlock(x0+x,y0-2,z0+z,5)
        for z in range(len(self.housedata)-1):
            for x in range(len(self.housedata[0])-1):
                if self.housedata[z][x]=="1":
                    mc.setBlock(x0+3+x,y0-2,z0+3+z,35)
                else:
                    mc.setBlock(x0+3+x,y0-2,z0+3+z,5)
    def buildbase(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        mc=self.mc
        for x in range(10):
            mc.setBlock(x0+x,y0-2,z0,98)

        for z in range(9):
            mc.setBlock(x0,y0-2,z0+z,98)
        
        for x in range(9):
            mc.setBlock(x0+x,y0-2,z0+9,98)

        for z in range(10):
            mc.setBlock(x0+9,y0-2,z0+z,98)

        for x in range(2):
            mc.setBlock(x0+3+x,y0-2,z0-1,53,2)
    def buildroof(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        mc=self.mc
        yaxis=[3,4,5,6,7,8]
        for f in yaxis:
            for z in range(17-2*f):
                mc.setBlock(x0+(f-4),y0+f,z0+z+(f-4),53,0)
                mc.setBlock(x0+(13-f),y0+f,z0+z+(f-3),53,1)
            for x in range(17-2*f):
                mc.setBlock(x0+x+(f-3),y0+f,z0+(f-4),53,2)
            for x in range(17-2*f):
                mc.setBlock(x0+x+(f-4),y0+f,z0+(13-f),53,3)
    def buildall(self):
        self.buildwall()
        self.buildfloor()
        self.buildbase()
        self.buildroof()
