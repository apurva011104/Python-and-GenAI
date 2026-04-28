csvString = "23,45,67,12"
li = csvString.split(",")
print(li)
sum = 0
max = 0
for i in li:
    sum+=int(i)
    val = int(i)
    if(val>max):
        max = val

mean = sum/len(li)

print(f"Mean: {mean}")
print(f"Max Value: {max}")