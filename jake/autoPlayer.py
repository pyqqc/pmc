import serial
import time
import csv



f=open('music.csv','r')
csvreader=csv.reader(f)
Music=list(csvreader)

song_number=len(Music)


musicbox={}
for x in range(song_number):
    musicbox[Music[x][0]]=x



ser=serial.Serial(port='COM3')



action = input("> ")
status1=action in musicbox

if status1:
    place=musicbox[action]
    for i in range(16):
        ser.write(Music[place][i].encode())
        ser.write('A'.encode())
        time.sleep(0.25)


