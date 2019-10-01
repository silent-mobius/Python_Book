#!/usr/bin/env python3


var = int(input("Please insert number: "))
i =0 

while i< 20 :
    print(var,i)
    i  += 1 # i = i+1



i = int(input("Please insert number :"))

if i>1000:
    print(i,"is bigger then 1000")
else:
    while i < 1000:
        print(i)
        i+=1



i = int(input("enter nnumber :"))

if i>1000:
    print(i ,"is bigger then 1000")
else:
    while i < 1000:
        if i%2==1:
            print(i)
        i+=1



import time
x=int(input('insert number: '))
i=0
while i< x:
    print('*'*i,)
    i = i+1
    time.sleep(0.5)