import sys

name = "triangle.txt"

# Open the file for reading.
with open(name) as f:
    array =[]
    for line in f:

        array.append(line.split())

print(array[99])
