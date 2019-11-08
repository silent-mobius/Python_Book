def convert_to_list(data):
    tmp = str(data).split(',')
    return list(tmp)

def convert_to_tuple(data):
    tmp = str(data).split(',')
    return tuple(tmp)

data = input("Please enter comma seperated values: ")

print(convert_to_list(data), convert_to_tuple(data))