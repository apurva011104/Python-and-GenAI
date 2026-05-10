def is_name_valid(name):
    name = name.lower().strip()
    if name=="none":
        print(name)
        return False
    name = name.replace("\"","").strip()
    if len(name)==0:
        return False
    for ch in name:
        if not ch.isalpha():
            return False
    return True
    

names_list_input = input("Enter names list: ")

names_list_input = names_list_input.replace("[","").replace("]","")

names_list = names_list_input.split(",")

print(names_list)
filtered_list = []

for name in names_list:
    if is_name_valid(name):
        new_name = name.strip()[1:-1].strip()
        new_name = new_name[0].upper()+""+new_name[1:].lower()
        filtered_list.append(new_name)

print(filtered_list)

    