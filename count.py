import os
from git import Repo
import sys
import re

giturl="https://github.com/open-mpi/ompi"
Repo.clone_from(giturl, "clone_files")

def is_file(filepath):
    print(filepath)
    file = open(filepath, 'r',encoding='utf-8')
    assert_count = 0
    if ".DS_Store" not in filepath and filepath.endswith(".c"):
        lines = file.readlines()

        for line in lines:
            if re.search(r'^\s*.(assert\(.*\))', line):
                assert_count = assert_count + 1
    return assert_count


def is_directory(f):
    list = []
    for filename in os.listdir(f):
        filepath = os.path.join(f, filename)
        print(filepath)
        if os.path.isfile(filepath):
            assert_count = is_file(filepath)
            if assert_count != 0:
                list.append(filepath + " " + str(assert_count))
        elif os.path.isdir(filepath):
            list = is_directory(filepath)

    return list


with open('test_files.txt', 'w', encoding='utf8') as textfile:
    for root, dirs, files in os.walk(r'clone_files'):
        print("root is..", root)
        print("dirs is...", dirs)
        print("files is..", files)
        for dir in dirs:
            print("dir is...", dir)
            test_path = root + "/" + dir
            for subdir in os.listdir(test_path):
                f = os.path.join(test_path, subdir)
                print(f)
                if os.path.isdir(f):

                    list = is_directory(f)
                    for ch in list:
                        textfile.write(ch)
                        textfile.write('\n')
                elif os.path.isfile(f):
                    assert_count = is_file(f)
                    if assert_count != 0:
                        textfile.write(f + " " + str(assert_count))
                        textfile.write('\n')

        break
