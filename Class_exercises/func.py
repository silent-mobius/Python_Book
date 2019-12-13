lst = [1,2,3,'a','b','c',[3,2,1],[4,3,2],(2,4,6),{9,8,7}, {1:0,2:1,3:2,4:3}]

for i in lst:
    print(i,end=' ')

print()
x = 0

while x < len(lst):
    print(lst[x],end=' ')
    x = x + 1 # x += 1
###########################################
print()

lst.append('Alex')
print(lst, end=' ')
lst.pop(1)
print(lst, end=' ')
lst.insert(4,'ninja')
print(lst, end=' ')
lst.remove('a')
print(lst, end=' ')
lst.reverse()
print(lst, end=' ')
#lst.sort()
#print(lst, end=' ')
lst.index('ninja')
print(lst, end=' ')
lst.clear()
print(lst, end=' ')

print()
lst = [1,2,3,'a','b','c',[3,2,1],[4,3,2],(2,4,6),{9,8,7}, {1:0,2:1,3:2,4:3}]

def type_print(lst):

    for i in lst:
        print(i,type(i))

new_list=(type_print(lst))

print(new_list)