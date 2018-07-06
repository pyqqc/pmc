from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f = open("blocks.csv","r")
data = f.read()
rows = data.split("\n")
xy=0
for zrow in rows:
    if len(zrow)<=0:
        continue
    zblocks = zrow.split(",")
    xy = xy+1
    z=0
    for zblock in zblocks:
        z = z+1

        y = xy%40
        x = xy//40
        x0 = pos.x+x
        y0 = pos.y+y
        z0 = pos.z+z
        blockid = int(zblock)
        mc.setBlock(x0,y0,z0,blockid)
