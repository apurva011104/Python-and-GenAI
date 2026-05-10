import re

regions_list_input = input("Enter customer regions list: ")

regions_list_input = regions_list_input.replace("[","").replace("]","").replace("\"","")

regions_list_input = re.sub("\\s+","",regions_list_input)

regions_list = regions_list_input.split(",")

regions_list = set(regions_list)

regions_list = list(regions_list)

regions_list.sort()

print(regions_list)