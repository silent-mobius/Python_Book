detail_name = input("Please insert name")
detail_lname = input("Please insert last name")
detail_id = input("Please insert id")
detail_address = input("Please insert address")

if detail_name == '' or detail_name == None:
    detail_name = input("Please insert name")

if detail_lname == '' or detail_lname == None:
    detail_lname = input("Please insert last name")

if detail_id == '' or detail_id == None:
    detail_id = input("Please insert id")

if detail_address == '' or detail_address == None:
    detail_address = input("Please insert name")

character_list = []

for letter in detail_name:
    character_list.append(letter)

for letter in detail_lname:
    character_list.append(letter)

for letter in detail_id:
    character_list.append(letter)

for letter in detail_address:
    character_list.append(letter)

uniq_character_set = set(character_list)


print("The unique chatacters in your details: ", uniq_character_set,"amount of characters is :", len(uniq_character_set))