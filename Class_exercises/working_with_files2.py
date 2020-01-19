
# working with files
var = open('file.txt')

for i in var.read():
    print(i,end='')

var.close()


with open('file.txt') as var:
    for i in var.readlines():
        print(i)