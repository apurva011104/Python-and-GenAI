import re

inp = input("Enter csv text: ").strip()
inp = re.sub("\\s+"," ",inp)

csv_values = re.sub(",+",",",inp).split(",")

cleaned_values_list = []

for value in csv_values:
    val = value.strip()
    formattedVal = ""
    for v in val:
        if(not v.isspace() and not v.isalnum()):
            continue
        formattedVal = formattedVal + "" + v
    cleaned_values_list.append(formattedVal)
    
cleaned_values = ", ".join(cleaned_values_list)

print(cleaned_values)