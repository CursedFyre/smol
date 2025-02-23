import math
import sys

from datetime import datetime
import time

# Method 1
t = time.localtime(time.time())
#t.tm_hour
#t.tm_min

c=int(input("Current resin: "))
n=int(input("Needed resin: "))
diff=n-c
h=math.floor(diff*8/60)
mn=(diff*8)%60
print(" ")
print("Time left=",h , mn)
#print(t.tm_hour, t.tm_min) printing current time
print(" ")
print("Full at:")
#ADDING
fh=t.tm_hour+h
fm=t.tm_min+mn
#print(fh , fm) printing time sum
#both large
if(fh>=24 and fm>=60): 
    print(fh-23 , fm-60)
#mins large 
elif(fm>=60):
    print(fh+1 , fm-60)
#hours large
elif(fh>=24):
    print(fh-24 , fm)
#normal
else:
    print(fh , fm)
print(" ")





piss=int(input("Go Away"))