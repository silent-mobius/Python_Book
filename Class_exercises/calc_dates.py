##############################################
#Created by : Silent-Mobius
#Purpose: take 2 dates and calculate amount of days between them
#Date: 10/11/2019
#Version: 1.1.4
##############################################

## library imports

## variable definition:

date_a=input("Please enter date A: ")
date_b=input("Please enter date B: ")

year_a = int(date_a.split('.')[2])
month_a = int(date_a.split('.')[1])
day_a = int(date_a.split('.')[0])

year_b = int(date_b.split('.')[2])
month_b = int(date_b.split('.')[1]) 
day_b = int(date_b.split('.')[0])

## function deifinition:


def year_calc(year_a, year_b):
    return ((year_a - year_b)*365)


def month_calc(month_a, month_b):
    if month_a == 2 or month_b == 2:
        return ((month_a-month_b)*28)
    else:
        return ((month_a-month_b)*30)


def day_calc(day_a, day_b):
    return(day_a - day_b)


def deco(var):
    print("###################################")
    print("#", var)
    print("###################################")

#####
#Main -_-
#####
year = year_calc(year_a,year_b)
month = month_calc(month_a,month_b)
day = day_calc(day_a,day_b)

var =year+month+day

deco(var)

deco(year_calc(year_a,year_b)+month_calc(month_a,month_b)+day_calc(day_a,day_b))