#!/usr/bin/env python3

from time import sleep

x = 5
y = 2
my_list=[1,2,3,4]
sleep(5)

print("Aritmetic operators")

print(f" example : {x} + {y}=",x+y)
print(f" example : {x} - {y}=",x-y)
print(f" example : {x} * {y}=",x*y)
print(f" example : {x} / {y}=",x/y)
print(f" example : {x} ** {y}=",x**y)
print(f" example : {x} // {y}=",x//y)
print(f" example : {x} % {y}=",x%y)

print("Comparisant operators: ")

print(f" example : {x} == {y}=",x==y)
print(f" example : {x} != {y}=",x!=y)
print(f" example : {x} > {y}=",x>y)
print(f" example : {x} < {y}=",x<y)
print(f" example : {x} >= {y}=",x>=y)
print(f" example : {x} <= {y}=",x<=y)

sleep(5)

print("Logical Operators: ")

print(f" example : {x}==5 and {y}==2",(x==5 and y==2))
print(f" example : {x}>5 or {y}>2",(x==5 or y==2))
print(f" example : not({x}<5 and {y}<2)",not(x==5 and y==2))

sleep(5)

print("Membership/Inclusion Operator: ")

print(f"{y} is in {my_list}: ",y in my_list)
print(f"{x} is NOT in {my_list}: ",x not in my_list)


sleep(5)

print("identity Operator: ")

print(f"{x} is {y}: ", x is y)
print(f"{x} is not {y}: ", x is not y)

sleep(5)