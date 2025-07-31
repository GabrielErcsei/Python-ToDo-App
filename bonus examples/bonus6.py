contents = ['This is just some dummy content for the first file', 'This is just some dummy content for the first file', 'This is just some dummy content for the first file']

file_names = ['file1.txt', 'file2.txt', 'file3.txt']

for content, filename in zip(contents, file_names):
    file = open(f"../files/{filename}", 'w')
    file.write(content)