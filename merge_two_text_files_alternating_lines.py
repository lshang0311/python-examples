import os
from itertools import zip_longest

"""
https://stackoverflow.com/questions/42480006/merge-two-text-files-alternating-lines-using-python-3-x-code

"""

path = r"../data"
path = os.path.abspath(path)
file_name_1 = 'file_1.csv'
file_name_2 = 'file_2.csv'
full_file_name_1 = os.path.join(path, file_name_1)
full_file_name_2 = os.path.join(path, file_name_2)

with open(full_file_name_1) as f1, \
        open(full_file_name_2) as f2:
    for lines in zip_longest(f1, f2):
        for line in lines:
            if line is not None:
                print(line.strip())
