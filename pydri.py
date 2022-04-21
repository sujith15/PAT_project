from pydriller import Repository


for commit in Repository('https://github.com/open-mpi/ompi').traverse_commits():
    print(commit.hash)
    print(commit.msg)
    print(commit.author.name)

    for file in commit.modified_files:
        print(file.filename, ' has changed')