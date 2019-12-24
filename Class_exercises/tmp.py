data2={1:['a','b','c',5,6,7],2:[5,6,7,'c','b','a'],3:(1,2),4:(3,4)}


def get_element_from_dict(par1,par2):
    tmp_data = par1[par2]
    for d in tmp_data:
        tmp = ord(str(d))
        tmp = tmp+1
        tmp = chr(tmp)
        lock = tmp_data.index(d)
        tmp_data.insert(lock,tmp)
        tmp_data.pop(lock+1)
    
    return tmp_data 


print(get_element_from_dict(data2,2))