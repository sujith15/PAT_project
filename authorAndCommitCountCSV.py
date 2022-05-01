from pydriller import Repository
import pandas as pd
import matplotlib.pyplot as plt
import csv

authorCommitCount = {}
yearCommitCount = {}
for commit in Repository('https://github.com/open-mpi/ompi', filepath='test',
                         only_modifications_with_file_types=['.c']).traverse_commits():
    if commit.author.name in authorCommitCount.keys():
        authorCommitCount[commit.author.name] += 1
    else:
        authorCommitCount[commit.author.name] = 1
    year = commit.author_date.isoformat()[0:4]
    if year in yearCommitCount.keys():
        yearCommitCount[year] += 1
    else:
        yearCommitCount[year] = 1

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

print(sum(yearCommitCount.values()))

series = pd.read_csv('commit_count.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
plt.xlabel('Date')
plt.ylabel('No. of Commits')
plt.title('Number of commits in each year in Test')
plt.show()
plt.savefig('commit_count.png')
plt.close()

data = pd.read_csv('author_count.csv')

a = data.to_dict('records')
xx = {}
for b in a:
    xx[b['Author Name']] = b['Count']

c = dict(sorted(xx.items(), key=lambda item: item[1], reverse=True))
Top5Authors = {k: c[k] for k in list(c)[0:5]}

plt.bar(Top5Authors.keys(), Top5Authors.values())
plt.xlabel('Author Name')
plt.ylabel('No. of Commits')
plt.title('TOP CONTRIBUTORS')
plt.savefig('author_count.png')
plt.close()