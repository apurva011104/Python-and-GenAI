import ast

set_A_string = input("Enter set A: ")

set_B_string = input("Enter set B: ")

set_A = ast.literal_eval(set_A_string)

set_B = ast.literal_eval(set_B_string)

print(f"Intersection: {set_A.intersection(set_B)}")