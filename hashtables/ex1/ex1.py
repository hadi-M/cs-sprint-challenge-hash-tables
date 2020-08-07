from pdb import set_trace as st


def get_indices_of_item_weights(weights, length, limit):
    # """
    # YOUR CODE HERE
    # """
    # # Your code here
    memory = dict()
    difference = [limit-i for i in weights]
    duplicates = weights + difference
    # st()
    for i in duplicates:
        try:
            memory[i] += 1
            num_1 = i
            num_2 = limit - i
            return sorted(
                (
                    weights.index(max(num_1, num_2)),
                    length - 1 - weights[::-1].index(min(num_1, num_2))
                ),
                reverse=True
            )
        except KeyError:
            memory[i] = 1

    return None
    # pass


if __name__ == "__main__":
    weights_1 = [9]
    print(get_indices_of_item_weights(weights_1, 1, 9))
    weights_2 = [4, 4]
    print(get_indices_of_item_weights(weights_2, 2, 8))
    weights_3 = [4, 6, 10, 15, 16]
    print(get_indices_of_item_weights(weights_3, 5, 21))
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights_4, 9, 7))