##########
#Created by : Silent-Mobius
#purpose: lear to work with files
#date: 17/11/2019
#version: 1.0.0
##########

f = open('file.txt','r')
var = -1
#print(f.read(10))
#print(f.readlines())
for line in f.read():
    #print(line,end=' ')
    if line == '\n':
        var = var + 1
    
    if var == 1:
        print(line,end=' ')



f.close()