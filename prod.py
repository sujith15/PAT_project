import os
from git import Repo
import csv
import re
import pandas as pd
import matplotlib.pyplot as plt


# giturl="https://github.com/open-mpi/ompi"
# Repo.clone_from(giturl, "clone_files")

def is_file(filepath):
    assert_count = 0
    debug_count = 0
    list1 = []
    list2 = []
    if ".DS_Store" not in filepath and (filepath.endswith(".c") or filepath.endswith(".h") or filepath.endswith(".sh")):
        file = open(filepath, 'r', encoding='utf-8')
        lines = file.readlines()

        for line in lines:
            if re.search(r'^\s*.(assert\(.*\))', line):
                list1.append(lines.index(line) + 1)
                assert_count = assert_count + 1

        for line in lines:
            if line.startswith("#if") and line.find("DEBUG") > 0:
                list2.append(lines.index(line) + 1)
                lines[lines.index(line)] = ""

                debug_count = debug_count + 1


    else:
        return [], [], -1, -1
    return list1, list2, assert_count, debug_count


def is_directory(dir, subdir, f):
    list = []
    for filename in os.listdir(f):
        filepath = os.path.join(f, filename)

        if os.path.isfile(filepath):

            list3, list4, assert_count, debug_count = is_file(filepath)
            if assert_count != -1 or debug_count != -1:
                list1 = [filepath, dir, subdir, filename, assert_count, list3, debug_count, list4]
                list.append(list1)
        elif os.path.isdir(filepath):

            list = is_directory(dir, subdir, filepath)

    return list


with open('prod_count.csv', 'w', encoding='utf8', newline='') as csvfile:
    for root, dirs, files in os.walk(r'clone_files'):

        header = ['Path', 'Directory', 'Sub Directory', 'File Name', 'Assert count', 'Assert Location', 'Debug count',
                  'Debug Location']
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for dir in dirs:

            if dir != 'test':
                test_path = root + "/" + dir
                for subdir in os.listdir(test_path):
                    f = os.path.join(test_path, subdir)

                    if os.path.isdir(f):

                        list = is_directory(dir, subdir, f)

                        writer.writerows(list)

                    elif os.path.isfile(f):
                        if f.endswith(".c") or f.endswith(".h") or f.endswith(".sh"):
                            list5, list6, assert_count, debug_count = is_file(f)
                            if assert_count != -1 or debug_count != -1:
                                writer.writerow([f, dir, subdir, subdir, assert_count, list5, debug_count, list6])

        break

