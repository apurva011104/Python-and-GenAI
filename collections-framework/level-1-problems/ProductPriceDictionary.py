import re

products_name_input = input("Enter product names list: ")

products_name_input = products_name_input.replace("[","").replace("]","").replace("\"","")

products_name_input = re.sub("\\s+","",products_name_input)

products_price_input = input("Enter product prices list: ")

products_price_input = products_price_input.replace("[","").replace("]","").replace("\"","")

products_price_input = re.sub("\\s+","",products_price_input)

products_name_list = products_name_input.split(",")

products_price_list = products_price_input.split(",")

zipped = dict(zip(products_name_list, products_price_list))

print(zipped)