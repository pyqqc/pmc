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

mc.setBlock(-9,0,42,block.DIAMOND_BLOCK.id)
for y in range(4):
    for z in range(10):
        mc.setBlock(-9,y,z+37,block.DIAMOND_BLOCK.id)
        mc.setBlock(-19,y,z+37,block.DIAMOND_BLOCK.id)
    for x in range(11):
        mc.setBlock(x-19,y,47,block.DIAMOND_BLOCK.id)
        mc.setBlock(x-19,y,37,block.DIAMOND_BLOCK.id)
for x in range(11):
    for z in range(10):
        if pat[x][z] == "1":
            mc.setBlock(x-19,4,z+37,block.DIAMOND_BLOCK.id)
        else:
            mc.setBlock(x-19,4,z+37,block.GOLD_BLOCK.id)
