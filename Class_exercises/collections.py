data1=[1,2,3,[1,2,3,4,5,6],[[1,2],[3,4],[5,6]],((1,2),(3,4))]
data2={1:['a','b','c',5,6,7],2:[5,6,7,'c','b','a'],3:(1,2),4:(3,4)}
data3=(5,5,'a','b','c','a','c',5,'5','z','g','x')

#1.1 # 1.2
short=len(data1)
short_list=[]
new_list=[]
for i in data1:
    try:
        if type(i) == type(list()):
            if len(i) < short:
                short_list.append(i)
    
    except:
        print('error happened')

for i in short_list:
    new_list = new_list + i

print(new_list)


#2.1 #2.2
new_tuple= []
for i in data3:
    if i not in new_tuple:
        new_tuple.append(i)

new_tuple = tuple(new_tuple)

print(new_tuple)

