i=0
while i < 10:
    print(i)
    i = i + 1
    # i += 1 shortcut to i = i + 1

x = 0

while x<100:
    if x%2==0:
        print(x)
    x = x+1

#break
#continue

i=0

while i < 6:
    print(i)
    if i==3:
        break
    i += 1

i=0

while i < 6:
    i += 1
    print(i)
    if i==3:
        continue



i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Iisnolonger smaller then 6")

