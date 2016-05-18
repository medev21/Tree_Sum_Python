import sys

name = "triangle.txt"

# Open the file for reading.
with open(name) as f:
    array =[]
    for line in f:
        results = map(int, line.split())
        array.append(results)

print(array[99])
