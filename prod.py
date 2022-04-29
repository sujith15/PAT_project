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
    debug_count = 0
    list1 = []
    list2 = []
    if ".DS_Store" not in filepath and (filepath.endswith(".c") or filepath.endswith(".h") or filepath.endswith(".sh")):
        file = open(filepath, 'r', encoding='utf-8')
        # assert_count = 0 if ".DS_Store" not in filepath and (filepath.endswith(".c") or filepath.endswith(".h") or
        # filepath.endswith(".sh")) :
        lines = file.readlines()

        for line in lines:
            if re.search(r'^\s*.(assert\(.*\))', line):
                list1.append(lines.index(line)+1)
                assert_count = assert_count + 1

        for line in lines:
            # if re.search(r'^.*.DEBUG\(.*', line):
            if line.startswith("#if") and line.find("DEBUG") > 0:

                print(line)
                print("Holla")
                list2.append(lines.index(line)+1)
                lines[lines.index(line)]=""
                print(line)
                debug_count = debug_count + 1
            # if debug_count > 0:
            #     break

    else:
        return [],[],-1, -1
    return list1, list2, assert_count, debug_count


def is_directory(dir, subdir, f):
    list = []
    for filename in os.listdir(f):
        filepath = os.path.join(f, filename)
        print(filepath)
        if os.path.isfile(filepath):
            print("hello")
            list3, list4, assert_count, debug_count = is_file(filepath)
            if assert_count != -1 or debug_count != -1:
                # if assert_count != 0:
                list1 = [filepath, dir, subdir, filename, assert_count, list3, debug_count, list4]
                list.append(list1)
        elif os.path.isdir(filepath):

            list = is_directory(dir, subdir, filepath)

    return list


with open('prod_count.csv', 'w', encoding='utf8', newline='') as csvfile:
    for root, dirs, files in os.walk(r'clone_files'):
        print("root is..", root)
        print("dirs is...", dirs)
        print("files is..", files)
        header = ['Path', 'Directory', 'Sub Directory', 'File Name', 'Assert count', 'Assert Location', 'Debug count',
                  'Debug Location']
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for dir in dirs:
            print("dir is...", dir)
            if dir != 'test':
                test_path = root + "/" + dir
                for subdir in os.listdir(test_path):
                    f = os.path.join(test_path, subdir)
                    print(f)
                    if os.path.isdir(f):

                        list = is_directory(dir, subdir, f)

                        writer.writerows(list)

                    elif os.path.isfile(f):
                        if f.endswith(".c") or f.endswith(".h") or f.endswith(".sh"):
                            list5, list6, assert_count, debug_count = is_file(f)
                            if assert_count != -1 or debug_count != -1:
                                writer.writerow([f, dir, subdir, subdir, assert_count, list5, debug_count, list6])

        break

data = pd.read_csv("prod_count.csv")
dirs = data["Directory"].unique()
dirs.sort()
print(dirs)
# count = data["Assert count"]
count = data.groupby('Directory')['Assert count'].sum()
print(count)
print(type(count))

x = []
y = []
x = dirs
y = count
plt.bar(x, y)
plt.xlabel('Folders')
plt.ylabel('Count')
plt.title('ASSERT STATEMENTS COUNT(Production Files)')
plt.ylim(0, 200)

plt.savefig("prod_assert_plot.png")
plt.show()

data = pd.read_csv("prod_count.csv")
dirs = data["Directory"].unique()
dirs.sort()
print(dirs)
# count = data["Assert count"]
count = data.groupby('Directory')['Debug count'].sum()
print(count)
print(type(count))

x = []
y = []
x = dirs
y = count
plt.bar(x, y)
plt.xlabel('Folders')
plt.ylabel('Count')
plt.title('DEBUG STATEMENTS COUNT(Production Files)')
plt.ylim(0, 200)

plt.savefig("prod_debug_plot.png")
plt.show()
