from pdb import set_trace as st


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    memory = dict()
    # st()
    for array in arrays:
        for i in array:
            try:
                memory[i] += 1
            except KeyError:
                memory[i] = 1

    result = [i[0] for i in memory.items() if i[1] > 1]

    # st()
    return result


# if __name__ == "__main__":
#     arrays = []

#     # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
#     arrays = [
#         [1],
#         [1],
#     ]

    print(intersection(arrays))
