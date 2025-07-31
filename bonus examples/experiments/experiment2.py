import csv

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))


city = input("Enter a city name: ").lower()

for row in data[1:]:
    if row[0].lower() == city:
        print(row[1])