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

x0=-29
y0=0
z0=59
def house():
    mc.setBlock(x0,y0,z0,block.DIAMOND_BLOCK.id)
    for y in range(4):
        for z in range(10):
            mc.setBlock(x0,y,z+z0-5,block.DIAMOND_BLOCK.id)
            mc.setBlock(x0-10,y,z+z0-5,block.DIAMOND_BLOCK.id)
            if z==5 and y<=1:
                mc.setBlock(-9,y,z+z0-5,block.DOOR_WOOD.id)
                mc.setBlock(x0-10,y,z+z0-5,block.DOOR_WOOD.id)
        for x in range(11):
            mc.setBlock(x0-10+x,y,z0+5,block.DIAMOND_BLOCK.id)
            mc.setBlock(x0-10+x,y,z0-5,block.DIAMOND_BLOCK.id)
            if x==5 and y<=1:
                    mc.setBlock(x0-10,y,z0+5,block.DOOR_WOOD.id)
                    mc.setBlock(x0-10,y,z0-5,block.DOOR_WOOD.id)
        for x in range(11):
            for z in range(10):
                if pat[x][z] == "1":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)
                else:
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD_BLOCK.id)


for f in range(10):
    house()
    x0=x0+20
