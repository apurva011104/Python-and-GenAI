inp = input("Enter list of product IDs: ")

product_list = inp[1:-1].replace("\"","").replace(" ","").split(",")

formatted_product_list = []

for product in product_list:
    formatted_product_list.append(product.upper().replace("_","-"))
    
print(formatted_product_list)