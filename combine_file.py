first_file = './data/file1.txt'
second_file = './data/file2.txt'

with open(first_file, encoding='utf-8') as file1, open(second_file, encoding='utf-8') as file2:
    for line1, line2 in zip(file1, file2):
        print(line1.strip('\n') + ' ' + line2.strip('\n'))
