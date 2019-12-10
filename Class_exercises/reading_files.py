
with open('story.txt', 'r') as file_data:
    data = file_data.readlines()

#print(type(data))
#words = data.split(' ')

word_to_print=[]

for word in range(len(data)):
    if word % 4 == 0:
        word_to_print.append(data[word])
    

word_to_print=set(word_to_print)

print(word_to_print,end='')

