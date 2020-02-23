x = 'f'


def add_one(x):
    try:
        if type(x) is str and  str(x).isalpha():
            tmp = ' '
            tmp = x
            x = ord(tmp)
            x = x+1
            x = chr(x)
            return x
        
        if type(x) is str and  str(x).isalnum():
            tmp = ' '
            tmp = x[-1]
            if tmp == 'z' or tmp == 'Z':
                tmp= tmp - 26
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