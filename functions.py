FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, "r") as data:
        todos_list = data.readlines()
    return todos_list


def write_todos(todos_arg, filepath=FILE_PATH):
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, "w") as data:
        data.writelines(todos_arg)

