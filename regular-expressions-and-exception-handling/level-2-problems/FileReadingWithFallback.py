try:
    with open("config.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found. Creating a new file...")

    with open("config.txt", "w") as file:
        file.write("New configuration file created.")