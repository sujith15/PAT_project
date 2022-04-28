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
for commit in Repository('https://github.com/open-mpi/ompi', filepath="test").traverse_commits():
    for file in commit.modified_files:
        if file.filename in test_files and file.filename not in files:
            files.append(file.filename)
            count = count + 1
            d[file.filename] = [[], [], [0],[0]]
            if commit.author.name not in d[file.filename][0]:
                d[file.filename][0].append(commit.author.name)
                d[file.filename][3][0] += 1
            d[file.filename][1].append(commit.author_date.isoformat())
        elif file.filename in files:
            d[file.filename][2][0] += 1
            if commit.author.name not in d[file.filename][0]:
                d[file.filename][3][0] += 1
                d[file.filename][0].append(commit.author.name)

        # print('The file {} is created on {} by {}.'.format(file.filename,commit.author_date,commit.author.name))

print(d)
print(len(d))
print(count)

filename = 'pydriller_task4.csv'
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["FileName", "List Of Authors", "Date Created", "Number of Commits", "Number of authors"])
    for key, value in d.items():
        csvwriter.writerow([key, ','.join(value[0]), value[1][0], value[2][0], value[3][0]])

# print(
#     'The file {} was added by {} on {}, '
#     'committed by {} on date {}'.format(
#         filename,
#         commit.author.name,
#         commit.author_date,
#         commit.committer.name,
#         commit.committer_date
#     )
# )
