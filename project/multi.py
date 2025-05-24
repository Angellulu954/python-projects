import threading
import time
def walkdog(first,last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")
def takeouttrash():
    time.sleep(2)
    print("You take out the trash")
def getmail():
    time.sleep(4)
    print("You get the mail")        
chore1=threading.Thread(target=walkdog,args=("Scooby","DubiDoo"))
chore1.start()
chore2=threading.Thread(target=takeouttrash)
chore2.start()
chore3=threading.Thread(target=getmail)
chore3.start()
chore1.join()
chore2.join()
chore3.join()
print("All chores are complete!")