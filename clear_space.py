from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()

stayed_time=0

size=int(input("size?"))

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for y in range(size):
        for x in range(size):
            for z in range(size):
                mc.setBlock(x+pos.x,y+pos.y,z+pos.z,block.AIR.id)
