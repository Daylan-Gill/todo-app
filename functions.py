FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Function reads a text file and then returns a list of all todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Function writes a text file and then returns a list of all todo items"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
