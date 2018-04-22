from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()

stayed_time=0

#-15,0,42


while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-13--15 y=0 z=41-43 for 10s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x<=-13 and  pos.x>=-15 and pos.y==-0 and pos.z>=41 and pos.z<=43:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.player.setTilePos(-20,10,40)
            stayed_time=0
    else:
        stayed_time=0
