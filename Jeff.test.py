from mcpi.minecraft import Minecraft
import binvox_rw
import time
import csv
import mcpi.vec3 as vec3
import mcpi.block as block
import Jeff.build_house_hawaiistyle as MHouse

mc=Minecraft.create()

#pos=mc.player.getTilePos()
pos=vec3.Vec3(86,47,67)

mc.player.setTilePos(86,47,67)
stayed_time=0


with open('xjergao.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
#print(model.data)

for y in range(model.dims[1]):
    print("layer y=",y)
    layer_data=model.data[y]
    stringlayer=""
    for x in range(model.dims[0]):
        stringlayer=stringlayer+"\n"
        for z in range(model.dims[2]):
            if model.data[x][z][y] == True:
                stringlayer=stringlayer+'1'
                mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.STONE.id)
            else:
                stringlayer=stringlayer+'0'
                mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.AIR.id)
    print(stringlayer)


g=open("authorized.csv","r")
csvreader1=csv.reader(g)
houseid=list(csvreader1)

def set_csv(csvname):
        f=open(csvname,"r")        
        csvreader=csv.reader(f)
        housedata=list(csvreader)
        return housedata


housen=[]
for houseamount in range(10):
    housen.append([pos.x+15*houseamount,pos.y,pos.z])

#speciality=[]    
for a in houseid[1:]:
    housedata=set_csv(str(a[1]))   
    housen[int(a[0])-1]=[int(a[2]),int(a[3]),int(a[4])]
    

for s in housen:
    buildhouse=MHouse.House(s,mc)
    buildhouse.buildall()

'''
for d in speciality:
    specialhouse=House(d)
    specialhouse.buildall()


for house in housen:
    House()
for spe in speciality:
    House.buildwall()   
    House.buildfloor()
    House.buildroof()
    House.buildbase()
'''

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-22~-24 y=8~10 z=-40~-42 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x>=-24 and pos.x<=-22 and pos.z>=-42 and pos.z<=-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0



