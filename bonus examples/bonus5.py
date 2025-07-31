test_list = ['gabi', 'ioana', 'freya']
test_list.sort(reverse=True)

for index, item in enumerate(test_list):
    print(f"{index + 1}.{item.capitalize()}")