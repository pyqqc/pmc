#import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12,GPIO.OUT)


#mc=Minecraft.create("192.168.0.155",4711)
mc=Minecraft.create()


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


#pos=vec3.Vec3(60,15,160)
pos=mc.player.getTilePos()

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
