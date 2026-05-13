import ast

dictionary_A_string = input("Enter dictionary A: ")

dictionary_B_string = input("Enter dictionary B: ")

dictionary_A = ast.literal_eval(dictionary_A_string)

dictionary_B = ast.literal_eval(dictionary_B_string)

merged = {}

for key in set(dictionary_A) | set(dictionary_B):
    merged[key] = dictionary_A.get(key, 0) + dictionary_B.get(key, 0)

print(merged)