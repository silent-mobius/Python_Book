#!/usr/bin/env python3

def avg_number(x, y):
    print("Average of ",x," and ",y, " is ",(x+y)/2)

avg_number(3, 4)


def printt():
    print("This is Python 3.2 Tutorial")
    print("This is Python 3.2 Tutorial")
    print("This is Python 3.2 Tutorial")

printt()


def nsquare(x, y):
    return (x*x + 2*x*y + y*y)

print("The square of the sum of 2 and 3 is : ", nsquare(2, 3))
 


def marks(english, math = 85, science = 80):
    print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)

marks(71, 77)
marks(65, science = 74)
marks(science = 70, math = 90, english = 75)


def average(x, y):
    return (x + y)/2

print(average(4, 3))

