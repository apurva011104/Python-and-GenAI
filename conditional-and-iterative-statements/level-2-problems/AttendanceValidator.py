attendance = float(input("Enter attendance of employee: "))

if attendance>=90:
    print("Excellent")
elif attendance>=75 and attendance<90:
    print("Satisfactory")
else:
    print("Poor")