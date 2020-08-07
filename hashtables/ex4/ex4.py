def has_negatives(array):
    """
    YOUR CODE HERE
    """
    # Your code here
    memory = dict()
    # st()

    for i in array:
        i = abs(i)
        try:
            memory[i] += 1
        except KeyError:
            memory[i] = 1

    result = [i[0] for i in memory.items() if i[1] > 1]

    # st()
    return result


# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
