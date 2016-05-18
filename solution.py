import sys

name = "triangle.txt"

# Open the file for reading.
with open(name) as f:
    array =[]
    for line in f:

        array.append(line.split())

def tree():

    name = "triangle.txt"

    # Open the file for reading.
    with open(name) as f:
        tree_array =[]
        for line in f:
            results = map(int, line.split())
            tree_array.append(results)

    # print(tree_array[99])
    sum = 0

    for index, val in reversed(list(enumerate(tree_array))):

        if(len(tree_array[index]) == 1):
            sum = tree_array[index][0]
            break

        i = 0
        sum_array = []
        for num in tree_array[index - 1]:

            a = num + tree_array[index][i]

            b = num + tree_array[index][i + 1]

            if a > b:
                sum_array.append(a)
            else:
                sum_array.append(b)

            i += 1


        tree_array[index - 1] = sum_array

    print(sum)

tree()
