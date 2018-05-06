from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-21 y=14 z=74 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-21 and pos.y==14 and pos.z==74:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-21,24,74)
            stayed_time=0
    else:
        stayed_time=0
        
     
