from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f = open("blocksWithData.csv","w")
xl = 3
yl = 3
zl = 3
for x in range(xl):
    for y in range(yl):
        for z in range(zl):
            block=mc.getBlockWithData(pos.x-x,pos.y+y,pos.z-z)
            mc.setBlock(308-x,2+y,30+z,block)
            print(block.id)
            print(block.data)
            f.write(str(block.id)+"|"+str(block.data))
            if z < 2:
                f.write(",")
                
        f.write("\n")
f.close()
