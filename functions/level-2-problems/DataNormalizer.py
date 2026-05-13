import ast

def normalize_names(name_list: list):
    normalize_name_list = []
    for name in name_list:
        normalized_name = name.strip().lower()
        normalize_name_list.append(normalized_name)
    return normalize_name_list

name_list_input = input("Enter names list: ")

name_list = ast.literal_eval(name_list_input)

normalize_name_list = normalize_names(name_list)

print(normalize_name_list)