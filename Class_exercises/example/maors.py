## libary imports
import sys
import os
import time

#Opening_Text_time
## variable definition:
info = "Created by: Maor Dahari,\n\
Purpose: take 2 dates and calculate amount of days between them.\n\
while using the time libary.\n\
Date: 10/11/19\n\
Version: 1.0.0"

## function definition:
def Time(info):
    for char in info:
        sys.stdout.write(char)
        sys.stdout.flush()
    
        if char !="\n":
           time.sleep(0.1)
        else:
           time.sleep(1)

os.system("cls")
Time(info)
os.system("cls")

## variable definition:
date_a = input("please enter date A: ")
date_b = input("please enter date B: ")

year_a = int(date_a.split('.')[2])
month_a = int(date_a.split('.')[1])
day_a = int(date_a.split('.')[0])

year_b = int(date_b.split('.')[2])
month_b = int(date_b.split('.')[1])
day_b = int(date_b.split('.')[0])

## function definition:
def year_calc(year_a,year_b):
    return((year_a - year_b)*365)

def month_calc(month_a,month_b):
    if month_a == 2 or month_b == 2:
        return ((month_a-month_b)*28)
    else:
        return ((month_a-month_b)*30)

def day_calc(day_a,day_b):
    return(day_a - day_b)

####
#Main
####

year = year_calc(year_a,year_b)
month = month_calc(month_a,month_b)
day = day_calc(day_a,day_b)

print(year,month,day)

