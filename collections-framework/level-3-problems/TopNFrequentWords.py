import ast
from collections import Counter as counter

input_string = input("Enter the string and value of 'n' in format ('s',n): ")

t = ast.literal_eval(input_string)

words_list = t[0].split(" ")

words_frequency = counter(words_list)

print(words_frequency.most_common(t[1]))