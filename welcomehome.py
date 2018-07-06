from mcpi.minecraft import Minecraft
import time
import mcpi.block as block
#import RPi.GPIO as GPIO
import serial
import mcpi.vec3 as vec3
import csv

f=open("mcHouse.csv",'r')
csvreader=csv.reader(f)
mcHouse_data=list(csvreader)
pos=vec3.Vec3(0,15,160)


MC=Minecraft.create()

#pos=MC.player.getTilePos()
import jake.CLASS as singingHouse








allRoom=[]
allHouse=[]

for i in range(5):
    sing=singingHouse.mchouse(mcHouse_data,MC,pos)
            
    sing.house()
    Room=sing.getrange()
    house_name=sing.getname()
    print (Room)
    allRoom.append(Room)
    pos.x=pos.x+20
    allHouse.append(sing)
    



    status1=[False,-1]

while True:
    newpos=MC.player.getTilePos()
    #print(newpos.x)
    #print(newpos.z)
    
    time.sleep(2)
    for room in allRoom:
        if newpos.x>room[0] and newpos.x<room[1] and newpos.z>room[2] and newpos.z<room[3]:
                ID=allRoom.index(room)
                status1=[True,ID]
                print('singing and shining')
                print("you are in room:",ID+1)

                #microsinging(status1)
                #microsinging.led(status1,status1)
        
        else:
            status1=[False,-1]





