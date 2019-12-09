long_list=[]

num = 0
target = 'a'

while len(long_list) < 10:
    data = input("Please inset some data: ")
    if data == target :
        num = num + 1
    long_list.append(data)
    

print(long_list, num)