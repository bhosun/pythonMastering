file_paths = [
    '/Users/mykeels/Documents/file.txt',
    '/Users/mykeels/Documents/file.csv',
    '/Users/mykeels/Music/a-whole-new-world.mp3',
    '/Users/mykeels/Movies/a-day-to-remember.mp4',
]

for path in file_paths:
    splits = path.split('.')
    file_length = len(splits)
    file_ext = splits[file_length - 1]
    print(file_ext)
