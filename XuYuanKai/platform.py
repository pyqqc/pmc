from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
for x in range (200):
    for z in range(20):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,1)
