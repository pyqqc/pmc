from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f = open("blocks.csv","w")
for x in range(10):
    for y in range(10):
        for z in range(10):
            block=mc.getBlock(pos.x+x,pos.y+y,pos.z+z)
            mc.setBlock(308-x,2+y,30+z,block)
            f.write(str(block))
            if z < 9:
                f.write(",")
                
        f.write("\n")
f.close()
