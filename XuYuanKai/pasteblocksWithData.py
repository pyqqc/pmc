from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f = open("Church.csv","r")
data = f.read()
rows = data.split("\n")
xy=0
for zrow in rows:
    if len(zrow)<=0:
        continue
    zblocks = zrow.split(",")
    z = 0
    for zblock in zblocks:
        y = xy%50
        x = xy//50
        x0 = pos.x-x
        y0 = pos.y+y
        z0 = pos.z-z
        blockinfo = zblock.split("|")
        blockid = int(blockinfo[0])
        blockdata = int(blockinfo[1])
        mc.setBlock(x0,y0,z0,blockid,blockdata)
        z = z+1
    xy = xy+1

