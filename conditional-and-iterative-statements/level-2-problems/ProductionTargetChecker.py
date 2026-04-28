weeklyProduction = []

print("Enter daily production for a week:")

for i in range(1,8,):
    units = int(input(f"Enter day {i}'s production units: "))
    weeklyProduction.append(units)
 
target = int(input("Enter target production units: "))
   
dayNum = 1

for i in weeklyProduction:
    if(i<target):
        print(f"Day {dayNum}: {i} units (below target)")
    dayNum+=1
