status = ["Pending", "Processing", "Delivered", "Failed", "Pending"]

for s in status:
    if(s=="Failed"):
        print("Processing stopped due to Failed status.")
        break
    print(f"Processing order: {s}")