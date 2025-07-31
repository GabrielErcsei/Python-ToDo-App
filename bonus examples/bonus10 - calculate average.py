def get_average() -> float:
    with open('files/data.txt', 'r') as file:
        data = file.readlines()

    temperatures = [float(i) for i in data[1:]]
    result = sum(temperatures) / len(temperatures)

    return result


average = get_average()
print(average)