import os

"""
https://stackoverflow.com/questions/8009882/how-to-a-read-large-file-line-by-line-in-python

"""

path = r"./data"
path = os.path.abspath(path)
file_name = 'list_of_fruits_1.csv'
full_file_name = os.path.join(path, file_name)

with open(full_file_name) as f:
    cnt = 0
    for line in f:
        print('line {}: {}'.format(cnt, line.strip()))
        cnt += 1
print(cnt)

# one-liner
with open(full_file_name) as f:
    cnt = 0
    cnt = sum(1 for line in f)
print(cnt)
