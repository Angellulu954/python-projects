import time 
import datetime 
import pygame 

def setalarm(alarmtime):
    print(f"Alarm set for {alarmtime}")
    soundfile="mymusic.mp3"
    isrunning=True
    while isrunning:
        currenttime=datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime)
        if currenttime==alarmtime:
            print("WAKEUP!🌞☝🏾")
            pygame.mixer.init()
            pygame.mixer.music.load(soundfile)
            pygame.mixer.music.play()
            isrunning=False
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        time.sleep(1)    
     
if __name__ =="__main__":
    alarmtime=input("Enter the alarm time(HH:MM:SS):")
    setalarm(alarmtime)