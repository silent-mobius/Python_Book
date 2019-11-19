#######################################
#created by : Alex M. Schapelle
#purpose: to demonstrate the python  language -> write a python program to get details and validate them, and after that save them to specific file on the system
#date: 19/11/2019
#version: 1.0.0
######################################

def input_data_and_validate(data):
    print("Please provide",data,": ")
    data = input()
    if len(data) != 0:
        return data
    else:
        data = input(f"Please provide{data}  :")

def get_details(name, lname, _id, address):

    _name= input_data_and_validate(name)
    
    _lname = input_data_and_validate(lname)
    
    __id = input_data_and_validate(_id)
    
    _address = input_data_and_validate(address)

    return  [_name, _lname, __id, _address]


def save_file_to_specific_place(data,file_name="data_file.txt"):
    try:
        with open(file_name,'a') as d:
            for i in data:
                d.write(i)
    except IOError:
        print("can not find specific file or file name")
    except:
        print("Some other error happend")


##########################################################################
NAME=""
LNAME=""
ID=""
ADDRESS=""

details = get_details(NAME,LNAME,ID,ADDRESS)

print(type(details))

save_file_to_specific_place(details)

print("the program has finished")

