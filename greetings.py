import time
timestamp= time.strftime("%H:%M:%S")
print(timestamp)
currentTimestamp= int(time.strftime("%H")+time.strftime("%M")+time.strftime("%S"))
print(currentTimestamp)
if 120000>currentTimestamp>=0:
    print("Good Morning")
elif 160000>=currentTimestamp>120000 :
    print("good afternoon")
elif 200000>=currentTimestamp>160000 :
    print("Good Evening")
else:
    print("good night")
