'''
#my_str = "Welcome to worderful world of JoJo's Bizarre Advanture"
my_str = input("Please provide data: ")
# breakdown the string into a list of words
words = my_str.split()
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)
'''
# Program to multiply two matrices using nested loops
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)


















