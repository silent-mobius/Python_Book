import sys

'''
data = sys.argv[0]
name = sys.argv[1]

print(" the data inserted is :", type(name), name)
'''
'''
def get_input(var):
    data = sys.argv[1]
    if data == '':
        data = input("Please provide input: ")
    var = data
    return var
'''


try:
    data = sys.argv[1]

except IndexError:
    data = input("Please insert data: ")

except:
    print("there was an error - exiting the program")
    sys.exit(1)

print("the data inserted is: ", data)