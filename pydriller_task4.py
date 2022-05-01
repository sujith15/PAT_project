from pydriller import Repository
import csv

with open('assert_count.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    test_files = []
    for row in reader:
        test_files.append(row['File Name'])
count = 0
files = []
d = {}
mod = 0
i = 0
authorCommitCount = {}
yearCommitCount = {}
for commit in Repository('https://github.com/open-mpi/ompi',filepath='test').traverse_commits():
    for file in commit.modified_files:
        if file.filename.endswith('.c') and file.filename not in files:
            files.append(file.filename)
            count = count + 1
            d[file.filename] = [[], [], [0], [0]]
            if commit.author.name not in d[file.filename][0]:
                d[file.filename][0].append(commit.author.name)
                d[file.filename][3][0] += 1
            d[file.filename][1].append(commit.author_date.isoformat())
        elif file.filename in files:
            d[file.filename][2][0] += 1
            if commit.author.name not in d[file.filename][0]:
                d[file.filename][3][0] += 1
                d[file.filename][0].append(commit.author.name)
        if commit.author.name in authorCommitCount.keys():
            authorCommitCount[commit.author.name] += 1
        else:
            authorCommitCount[commit.author.name] = 0
            year = commit.author_date.isoformat()[0:4]
        if year in yearCommitCount.keys():
            yearCommitCount[year] += 1
        else:
            yearCommitCount[year] = 0

filename = 'pydriller_task4.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["FileName", "List Of Authors", "Date Created", "Number of Commits", "Number of authors"])
    for key, value in d.items():
        csvwriter.writerow([key, ','.join(value[0]), value[1][0], value[2][0], value[3][0]])

with open('author_count.csv', 'w') as csvfile:
    csvwriterAuthors = csv.writer(csvfile)
    csvwriterAuthors.writerow(["Author Name", "Count"])
    for key, value in authorCommitCount.items():
        csvwriterAuthors.writerow(([key, value]))

with open('commit_count.csv', 'w') as csvfile:
    csvwriterYears = csv.writer(csvfile)
    csvwriterYears.writerow(["Date", "Count"])
    for key, value in yearCommitCount.items():
        csvwriterYears.writerow(([key, value]))
