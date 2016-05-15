import pdb

def tree():
    tree_array = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3],
    ]

    sum = 0

    for index, val in reversed(list(enumerate(tree_array))):

        # print(tree_array[index])
        if(len(tree_array[index]) == 1):
            sum = tree_array[index][0]
            break

        i = 0
        sum_array = []
        for num in tree_array[index - 1]:
            # print(tree_array[index - 1 ][i])
            # print(num)

            # a = tree_array[index - 1][i] + tree_array[index][i]
            # b = tree_array[index - 1][i] + tree_array[index][i + 1]

            a = num + tree_array[index][i]
            # pdb.set_trace()
            b = num + tree_array[index][i + 1]

            if a > b:
                sum_array.append(a)
            else:
                sum_array.append(b)

            i += 1


        tree_array[index - 1] = sum_array
        # print(tree_array[index - 1])

    print(sum)

# print(tree())
tree()
