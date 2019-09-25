i = int(input("enter nnumber :"))

if i>1000:
    print(i ,"is bigger then 1000")
else:
    while i < 1000:
        if i%2==1:
            print(i)
        i+=1
