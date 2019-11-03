def reverse_nameing(name,lname):
    return lname+" "+name

def reverse_lettering(var):
    return var[::-1]


name = input("Please enter name ")
lname = input("Please enter last name ")

print(reverse_nameing(name,lname))
print(reverse_lettering(name),reverse_lettering(lname))