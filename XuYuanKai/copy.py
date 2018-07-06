from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
for x in range(10):
    for y in range(10):
        for z in range(10):
            block=mc.getBlockWithData(308+x,2+y,30+z)
            mc.setBlock(308-x,2+y,30+z,block)
            print(block)
            

