import re

coordinates_input = input("Enter (x, y, z) tuple: ")

coordinates_input = coordinates_input.replace("(","").replace(")","").replace("\"","")

coordinates_input = re.sub("\\s+","",coordinates_input)

(x,y,z) = tuple(coordinates_input.split(","))       #Unpacking tuple

print(f"Coordinates: X={x}, Y={y}, Z={z}")