import glob

# selects the file types that you want to filter using a file pattern
filepaths = glob.glob("files/*.txt")


for filepath in filepaths:
    with open(filepath, 'r') as file:
        print(file.read())
print(filepaths)