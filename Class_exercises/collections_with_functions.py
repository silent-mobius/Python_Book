data1=[1,2,3,[1,2,3,4,5,6],[[1,2],[3,4],[5,6]],((1,2),(3,4))]
data2={1:['a','b','c',5,6,7],2:[5,6,7,'c','b','a'],3:(1,2),4:(3,4)}
data3=(5,5,'a','b','c','a','c',5,'5','z','g','x')

#1.1 # 1.2

def shortest_list_in_collections(lst):
    short = len(lst)
    short_list =  []

    for i in lst:
        if type(i) == type(list()):
            for j in i:
                if type(j) == type(list()):
                    if len(j) < short:
                        short_list.append(j)
        
    return short_list


def insert_to_new_list(lst):
    new_list = []
    for k in lst:
        new_list = new_list + k

    return new_list

    
def print_collection(lst):
    for i in lst:
        print(i)


tmp_data = shortest_list_in_collections(data1)
new_tmp_data = insert_to_new_list(tmp_data)
print(new_tmp_data)



#2.1 #2.2
def get_duplicates_from_tuple(lst):
    new_tuple= []
    for i in data3:
        if i not in new_tuple:
            new_tuple.append(i)

    new_tuple = tuple(new_tuple)
    return new_tuple

tmp_tuple = get_duplicates_from_tuple(data3)

print(tmp_tuple)


# 3

def get_element_from_dict(lst,position):
    dict_element = lst[position]
    for k in dict_element:
        tmp = ord(str(k))
        tmp = tmp + 1
        lock = dict_element.index(k)
        tmp = chr(tmp)
        dict_element.insert(lock,tmp)
        dict_element.pop(lock+1 )
        
    return(dict_element)

tmp_data = get_element_from_dict(data2,2)
print(tmp_data)
