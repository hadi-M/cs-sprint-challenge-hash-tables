# Your code here
from pdb import set_trace as st


def finder(paths, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    memory = dict()
    file_names = [single_file.rsplit("/", maxsplit=1)[-1] for single_file in paths]
    file_names_paths = list(zip(file_names, paths))
    for file_name_path in file_names_paths:
        # st()
        try:
            memory[file_name_path[0]].append(file_name_path[1])
        except KeyError:
            memory[file_name_path[0]] = [file_name_path[1]]

    result = []
    for query in queries:
        try:
            result.extend(memory[query])
        except KeyError:
            pass


    # st()
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
