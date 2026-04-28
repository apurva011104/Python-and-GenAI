branches = {
    "branch1":[],
    "branch2":[],
    "branch3":[],
    "branch4":[]
}

for key,value in branches.items():
    print(f"Enter {key} monthly revenues: ")
    for i in range(12):
        rev = float(input(f"Enter month {i+1}'s revenue: "))
        value.append(rev)

highestRevenueBranch = ""
highestRevenue = 0.0

for key,value in branches.items():
    totalRevenue = 0.0
    for i in value:
        totalRevenue += i
    if(totalRevenue>highestRevenue):
        highestRevenue = totalRevenue
        highestRevenueBranch

print(f"Branch with the highest revenue is {highestRevenueBranch} with total revenue of {highestRevenue}")