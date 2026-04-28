salesAmounts = [2525.0, 2547.0, 2415.0, 2759.0,2681.0, 2357.0]

sum = 0.0

for amt in salesAmounts:
    sum += amt

avg = sum / len(salesAmounts)

print(f"Sales Amounts: {salesAmounts}")
print(f"Average: {avg:.2f}")