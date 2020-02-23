x = 'f'


def add_one(x):
    try:
        if type(x) is str:
            tmp = ' '
            tmp = x
            x = ord(tmp)
            x = x+1
            x = chr(x)
            return x
        else:
            return x+1
    except:
        return False


print(add_one('a'))
print(add_one(6))