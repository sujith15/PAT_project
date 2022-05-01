from pydriller import Repository
import pandas as pd
import matplotlib.pyplot as plt
import csv

authorCommitCount = {}
yearCommitCount = {}

#Commits in test files
for commit in Repository('https://github.com/open-mpi/ompi',filepath='test').traverse_commits():
    if commit.author.name in authorCommitCount.keys():
        authorCommitCount[commit.author.name] += 1
    else:
        authorCommitCount[commit.author.name] = 1
    year = commit.author_date.isoformat()[0:4]
    if year in yearCommitCount.keys():
        yearCommitCount[year] += 1
    else:
        yearCommitCount[year] = 1

print(sum(yearCommitCount.values()))

#total number of authors
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



