from mcpi.minecraft import Minecraft
import serial
import csv
import time
import mcpi.vec3 as vec3
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)


mc=Minecraft.create("192.168.0.155",4711)


f=open("python.mc.csv",'r')
pattern = list(csv.reader(f))

f=open("mcHouse.csv",'r')
csvreader=csv.reader(f)
mcHouse_data=list(csvreader)


f=open('music.csv','r')
csvreader=csv.reader(f)
Music=list(csvreader)

song_number=len(Music)





musicbox={}
for x in range(song_number):
    musicbox[Music[x][0]]=x



#ser=serial.Serial(port='COM3')


pos=vec3.Vec3(60,15,160)



class mchouse:
    def __init__(self, data):
        self.data = data
        self.length=int(data[0][0])
        self.wide=int(data[0][1])
        self.height=int(data[0][2])
        a=self.length
        b=self.wide
        c=self.height
        self.RangeHouse=[pos.x+4,pos.x+3+a,pos.z+1,pos.z+b-1]
        self.name="star"

    def house(self):
        x=self.length
        y=self.height
        z=self.wide
        #pos=mc.player.getTilePos()
        #pos.x=poslist[0]
        #pos.y=poslist[1]
        #pos.z=poslist[2]
        mc.setBlocks(pos.x+3,pos.y+1,pos.z,pos.x+3+x,pos.y+y,pos.z+z,1)
        mc.setBlocks(pos.x+3,pos.y+3,pos.z,pos.x+3+x,pos.y+y-2,pos.z+z,89)
        mc.setBlocks(pos.x+4,pos.y+1,pos.z+1,pos.x+2+x,pos.y+y-1,pos.z+z-1,0)
        mc.setBlock(pos.x+3,pos.y+2,pos.z+round(z/2),0)
        mc.setBlock(pos.x+3,pos.y+1,pos.z+round(z/2),0)
        mc.setBlock(pos.x+3,pos.y+1,pos.z+round(z/2)-1,0)
        mc.setBlock(pos.x+3,pos.y+2,pos.z+round(z/2)-1,0)
        mc.setBlocks(pos.x+3,pos.y,pos.z,pos.x+3+x,pos.y,pos.z+z,17)
        for a in range(5):
            for c in range(5):
                mc.setBlock(pos.x+a+round(x/2+1),pos.y,pos.z+c+round(z/2-1.5),int(pattern[4-a][c])+17)
        

    def getrange(self):
        return self.RangeHouse

    def getname(self):
        return self.name

    def getID(self):
        return self.houseID

    def setID(self,houseID):
        self.houseID=houseID
       # (pos.x+3,pos.y+2,pos.z,12)

    def tnt(self):
        mc.setBlocks(pos.x+3,pos.y+3,pos.z,pos.x+3+x,pos.y+20,pos.z+20,46)



class microsinging:
    def __init__(self,status):
        if status[0]:
            place=status[1]
            for i in range(16):
                ser.write(Music[place][i].encode())
                ser.write('A'.encode())
                time.sleep(0.25)

    def led (self,status):
        if status[0]:
                GPIO.output(12,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(12,GPIO.LOW)
                time.sleep(1)
            



allRoom=[]
allHouse=[]


for i in range(10):
    myhouse=mchouse(mcHouse_data)
    myhouse.house()
    Room=myhouse.getrange()
    house_name=myhouse.getname()
    print (Room)
    allRoom.append(Room)
    pos.x=pos.x+20
    allHouse.append(myhouse)
    



status1=[False,-1]

while True:
    newpos=mc.player.getTilePos()
    #print(newpos.x)
    #print(newpos.z)
    
    time.sleep(2)
    for room in allRoom:
        if newpos.x>room[0] and newpos.x<room[1] and newpos.z>room[2] and newpos.z<room[3]:
            ID=allRoom.index(room)
            status1=[True,ID]
            print('singing and shining')
            print("you are in room:",ID+1)

            microsinging(status1)
            microsinging.led(status1)
        
    else:
        status1=[False,-1]
        
