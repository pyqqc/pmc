from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f = open("Church.csv","w")
xl = 50
yl = 50
zl = 50
for x in range(xl):
    for y in range(yl):
        for z in range(zl):
            block=mc.getBlockWithData(pos.x-x,pos.y+y-2,pos.z-z)
            mc.setBlock(308-x,2+y,30+z,block)
            print(block.id)
            print(block.data)
            f.write(str(block.id)+"|"+str(block.data))
            if z < 49:
                f.write(",")
                
        f.write("\n")
f.close()
