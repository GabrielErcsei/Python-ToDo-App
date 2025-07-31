INDEX = 1
FILEPATH = "todos.txt"

def display_to_do_list(todos: list):
    """ Returns a list of todo items """
    for index, item in enumerate(todos):
        print(f"{index + INDEX}-{item}")


def get_todos_from_file(filepath: str = FILEPATH) -> list[str]:
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos_to_file(todos: list, filepath: str = FILEPATH) -> None:
    with open(filepath, 'w') as file:
        file.writelines(todos)


# test -> this is only executed when the file is run directly, and not by using import

if __name__ == "__main__":
    print("Test")