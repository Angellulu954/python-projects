import datetime
date=datetime.date(2025,1,2)
today=datetime.date.today()
time=datetime.time(12,30,0)
now=datetime.datetime.now()
now=now.strftime("%H:%M:%S %d-%m-%Y")
targetdate=datetime.datetime(2020,1,2,12,30,1)
currentdate=datetime.datetime.now()
if targetdate<currentdate:
    print("Target date has already passed.")
else:
    print("Target date has NOT passed.")    