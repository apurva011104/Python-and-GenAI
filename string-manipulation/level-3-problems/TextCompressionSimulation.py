string = input("Enter string: ")

compressed_string = ""

l = 0

while l<len(string):
    r = l
    count = 0
    while(r<len(string) and string[l]==string[r]):
        r+=1
        count+=1
    compressed_string =  compressed_string + "" + string[l] + "" +  str(count)
    l = r
    
print(compressed_string)