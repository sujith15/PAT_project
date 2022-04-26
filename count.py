import os
from git import Repo
import csv
import re
import pandas as pd
import matplotlib.pyplot as plt


# giturl="https://github.com/open-mpi/ompi"
# Repo.clone_from(giturl, "clone_files")

def is_file(filepath):
    print(filepath)
    assert_count = 0
    if ".DS_Store" not in filepath and (filepath.endswith(".c") or filepath.endswith(".h") or filepath.endswith(".sh")):
        file = open(filepath, 'r', encoding='utf-8')
        # assert_count = 0 if ".DS_Store" not in filepath and (filepath.endswith(".c") or filepath.endswith(".h") or
        # filepath.endswith(".sh")) :
        lines = file.readlines()

        for line in lines:
            if re.search(r'^\s*.(assert\(.*\))', line):
                assert_count = assert_count + 1
    else:
        return -1
    return assert_count


def is_directory(dir, subdir, f):
    list = []
    for filename in os.listdir(f):
        filepath = os.path.join(f, filename)
        print(filepath)
        if os.path.isfile(filepath):
            print("hello")
            assert_count = is_file(filepath)
            if assert_count != -1:
                # if assert_count != 0:
                list1 = [filepath, dir, subdir, filename, assert_count]
                list.append(list1)
        elif os.path.isdir(filepath):

            list = is_directory(dir, subdir, filepath)

    return list


with open('assert_count.csv', 'w', encoding='utf8', newline='') as csvfile:
    for root, dirs, files in os.walk(r'clone_files'):
        print("root is..", root)
        print("dirs is...", dirs)
        print("files is..", files)
        header = ['Path', 'Directory', 'Sub Directory', 'File Name', 'Assert count']
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for dir in dirs:
            print("dir is...", dir)
            if dir == 'test':
                test_path = root + "/" + dir
                for subdir in os.listdir(test_path):
                    f = os.path.join(test_path, subdir)
                    print(f)
                    if os.path.isdir(f):

                        list = is_directory(dir, subdir, f)

                        writer.writerows(list)

                    elif os.path.isfile(f):
                        if f.endswith(".c") or f.endswith(".h") or f.endswith(".sh"):
                            assert_count = is_file(f)
                            if assert_count != -1:
                                writer.writerow([f, dir, subdir, subdir, assert_count])

        break

data = pd.read_csv("assert_count.csv")
dirs = data["Sub Directory"]
count = data["Assert count"]

x = []
y = []
x = dirs
y = count
plt.barh(x, y)
plt.xlabel('Assert count')
plt.ylabel('Folders')
plt.title('Data')

plt.savefig("assert_plot.png")
plt.show()
