'''print("Please enter 2 numbers: ")
num1=input()
num2=input()
sentance=input("Please insert long string: ")
#print(type(num1),type(num2))

num1=int(num1)
num2=int(num2)

print(type(num1),type(num2))

if num1 > num2:
print("Yes")

if num1 > num2:
    print("Yes")
elif num1 < num2:
    print("No")

if num1 > num2:
    print("Yes")
elif num1 < num2:
    print("No")
elif num1 >= num2:
    print("Yes")
elif num1 <= num2:
    print("No")
else:
    print("Error")

if (num1>=num2) and (num1<=num2):
    print("Both")
else:
    print("what ever")

if (num1>=num2) or (num1<=num2):
    print("Both")
else:
    print("what ever")

if (num1>=num2) and not  (num1<=num2):
    print("Both")
else:
    print("what ever")


if 'l' in 'Alex':
    print("includes")



while num1 < num2:
    print(sentance)
    num1 = num1 + 1
    num2 = num2 - 1

for index in "Alex Schapelle":
    print(index,end=' ')
    if (index == "a") or (index == "A"):
        print("Found", index)

'''
var="Alex Schapelle"
for i in range(len(var)):
    print(i)