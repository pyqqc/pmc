from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()
for x in range(10):
    for y in range(10):
        for z in range(10):
            mc.setBlock(pos.x+x,pos.y+y,pos.z+z,5)
for a in range(8):
    for b in range(8):
        for c in range(8):
            mc.setBlock(pos.x+a+1,pos.y+b+1,pos.z+c+1,0)
for t in range(2):
    mc.setBlock(pos.x+1,pos.y+t+1,pos.z,0)
for q in range(4):
    mc.setBlock(pos.x+q*2+1,pos.y+6,pos.z,20)
 
