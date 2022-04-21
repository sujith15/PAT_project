import os
from git import Repo
import sys

# giturl="https://github.com/open-mpi/ompi"
# Repo.clone_from(giturl, "clone_files")

with open('readme.txt', 'w') as textfile:
    for root, dirs, files in os.walk(r'clone_files'):
        print("root is..",root)
        print("dirs is...",dirs)
        print("files is..",files)
        for dir in dirs:
            print("dir is...",dir)
            if dir == "test":
                test_path=root+"/"+dir
                for subdir in os.listdir(test_path):
                    f=os.path.join(test_path,subdir)
                    print(f)
                    if os.path.isdir(f): 
                        for filename in os.listdir(f):
                            filepath=os.path.join(f,filename)
                            print(filepath)
                            if os.path.isfile(filepath):
                                file=open(filepath,'r')
                                lines=file.readlines()
                                # print(lines)
                                assert_count=0
                                for line in lines:
                                    if "assert(" in line:
                                        assert_count =assert_count + 1
                                print(filepath+" ",assert_count)
                                textfile.write(filepath+" "+str(assert_count))
                                textfile.write('\n')
                            elif os.path.isdir(filepath):
                                for filename1 in os.listdir(filepath):
                                    filepath1=os.path.join(filepath,filename1)
                                    print(filepath1)
                                    if os.path.isfile(filepath1):
                                        file=open(filepath1,'r')
                                        lines=file.readlines()
                                        # print(lines)
                                        assert_count=0
                                        for line in lines:
                                            if "assert(" in line:
                                                assert_count =assert_count + 1
                                        textfile.write(filepath+" "+str(assert_count))
                                        textfile.write('\n')


                    elif os.path.isfile(f):
                        file=open(f,'r')
                        lines=file.readlines()
                        assert_count=0
                        for line in lines:
                            if "assert(" in line:
                                assert_count =assert_count + 1
                                print(filepath+" ",assert_count)
                                textfile.write(filepath+" "+str(assert_count))
                                textfile.write('\n')

                    # if filename.is_file():
                    #     print(filename.path)
                # for file in os.listdir(files):
                #     print(file)
        break
    # # select file name
    # for file in files:
    #     # check the extension of files
    #     print(file)


