import sys


def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print('Cannot devide by zero')


try:
    num = float(sys.argv[1])
    num2 = float(sys.argv[2])
except IndexError:
    num = float(input("insert number1: "))
    num2 = float(input("insert number2: "))

for i in [0,5]:
    print(add(num,num2))
    print(mul(num,num2))
    print(sub(num,num2))
    print(div(num,num2))



    