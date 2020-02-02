from sys import argv


def hello(name='you'):
    return ("Hello ",name)

try:
    data=argv[1]
    print(hello(data))
except:
    print('there was an error')