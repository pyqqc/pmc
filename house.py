from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()

stayed_time=0

#-15,0,42
pat=[]
f=open("pattern.csv",'r')
data=f.read()
rows=data.split('\n')
for row in rows:
    pat.append(row.split(","))

print(pat)

xx0=-29
yy0=0
zz0=59
My_houses=[]
class house():
    def __init__(self, data):
        self.data = data
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                if pat[x][z] == "0":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GLASS.id)
                elif pat[x][z] == "2":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)
                    
                else:
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD_BLOCK.id)

    def build_house(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        mc.setBlock(x0,y0,z0,block.DIAMOND_BLOCK.id)
        for y in range(4):
            for z in range(10):
                mc.setBlock(x0,y,z+z0-5,block.DIAMOND_BLOCK.id)
                mc.setBlock(x0-10,y,z+z0-5,block.DIAMOND_BLOCK.id)
                if z==5 and y<=1:
                    mc.setBlock(-9,y,z+z0-5,block.AIR.id)
                    mc.setBlock(x0-10,y,z+z0-5,block.AIR.id)
        for x in range(11):
                mc.setBlock(x0-10+x,y,z0+5,block.DIAMOND_BLOCK.id)
                mc.setBlock(x0-10+x,y,z0-5,block.DIAMOND_BLOCK.id)
                if x==5 and y<=1:
                    mc.setBlock(x+x0-10,y,z0+5,block.AIR.id)
                    mc.setBlock(x+x0-10,y,z0-5,block.AIR.id)
        for x in range(11):
            for z in range(11):
                if pat[x][z] == "0":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)
                elif pat[x][z] == "2":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)
                    mc.setBlock(x0-10+x,5,z+z0-5,block.TORCH.id)
                else:
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD_BLOCK.id)

for f in range(10):
    mh=house([xx0,yy0,zz0])
    My_houses.append(mh)
    mh.build_house()
    xx0=xx0+20

My_houses[0].roof()
