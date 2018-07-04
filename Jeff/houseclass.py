from mcpi.minecraft import Minecraft
import time
import csv

mc=Minecraft.create()

stayed_time=0



class house:
    def __init__(self, data):
        self.x0 = data[0]
        self.y0 = data[1]
        self.z0 = data[2]
        self.housedata=[]
    def set_csv(self,csvname):
        f=open(csvname,"r")        
        csvreader=csv.reader(f)
        self.housedata=list(csvreader)    
    def buildwall(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
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
        yaxis=[3,4,5,6,7,8]
        for f in yaxis:
            for z in range(17-2*f):
                mc.setBlock(x0+(f-4),y0+f,z0+z+(f-4),53,0)
                mc.setBlock(x0+(13-f),y0+f,z0+z+(f-3),53,1)
            for x in range(17-2*f):
                mc.setBlock(x0+x+(f-3),y0+f,z0+(f-4),53,2)
            for x in range(17-2*f):
                mc.setBlock(x0+x+(f-4),y0+f,z0+(13-f),53,3)

housen=[]
for houseid in range(10):
    housen.append(house([235+15*houseid,19,-183]))
    


for house in housen[0:3]:
    house.set_csv("F_floor.csv")
    
for house in housen[3:7]:
    house.set_csv("L_floor.csv")
for house in housen[7:]:
    house.set_csv("R_floor.csv")
for house in housen:
    house.buildwall()   
    house.buildfloor()
    house.buildroof()
    house.buildbase()

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-22~-24 y=8~10 z=-40~-42 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x>=-24 and pos.x<=-22 and pos.z>=-42 and pos.z<=-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0

