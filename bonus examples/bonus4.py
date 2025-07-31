filenames = ["1.raw data.txt", "2.reports.txt", "3.test.txt"]
first_occurrence = 1
for filename in filenames:
    filename = filename.replace('.', '-', first_occurrence)
    print(filename)

filenames_tuple = ("1.raw data.txt", "2.reports.txt", "3.test.txt")