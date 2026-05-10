import ast

list_string = input("Enter the list of category wise sales: ")

list = ast.literal_eval(list_string)

dictionary = {}

for i in list:
    if i[0] not in dictionary:
        dictionary[i[0]] = 0
    dictionary[i[0]] = i[1] + dictionary[i[0]]
        
print(dictionary)