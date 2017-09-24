u = 0
t = int(input("Time spent on the road: "))
a = int(input("Acceleration: "))
sdist = int(input("Distance: "))
import math
def v():
    v = u + (a * t)
    return v
def srun():
    s = (u * t) + (1/2 * a * t**2)
    return s
def s1():
    s = (1/2 * t)*(v() + u)
    return s
def v1():
    v = math.sqrt(u**2 + (2 * a * sdist))
    return v
def duration():
    for x in range(0,t):(repr(x))
def distance():
    for y in range(0,t):
        s = srun() /10
        y = "*"
        z = s * y
        return z
T=0
while(T<=t):
    groundslam = u + (a * T)
    print("Duration:",T,"  Distance:","*"*(groundslam * T),)
    T = T + 1
for i in range(1):
    if (v(),v1() >= 60) :
        print("The person went over the speed limit. (Max speed was",v(),"m/s)")
    else:
        print("The person did not go over the speed limit. (Max speed was",v(),"m/s)")
for i in range(1):
    if (srun(),s1() >= sdist):
        print("The person reached the destination. (Reached",srun(),"m)")
    else:
        print("The person did not reach the destination. (Reached",srun(),"m)")

print("* indicates 1 m")





