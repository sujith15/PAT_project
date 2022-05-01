import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("assert_count.csv")
dirs = data["Sub Directory"]
count = data["Assert count"]

x = []
y = []
x = dirs
y = count
plt.barh(x, y)
plt.xlabel('Count')
plt.ylabel('Folders')
plt.title('ASSERT STATEMENTS COUNT')

plt.savefig("assert_count_plot.png")
plt.show()

fig, ax = plt.subplots()
data['Sub Directory'].value_counts().plot(ax=ax, kind='barh', xlabel='Folders', ylabel='Count')
plt.xlabel('Count')
plt.ylabel('Folders')
plt.title('TEST FILES COUNT')
plt.savefig("testFiles_count_plot.png")
plt.show()





data = pd.read_csv("prod_count.csv")
dirs = data["Directory"].unique()
dirs.sort()
count = data.groupby('Directory')['Assert count'].sum()

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
count = data.groupby('Directory')['Debug count'].sum()


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


data = pd.read_csv('commit_count.csv')

a = data.to_dict('records')
xx = {}
for b in a:
    xx[b['Date']] = b['Count']
print(xx)
c = dict(sorted(xx.items(), key=lambda item: item[1], reverse=True))
print(c)
Top5Authors = {k: c[k] for k in list(c)[1:6]}

plt.bar(Top5Authors.keys(), Top5Authors.values())
plt.xlabel('Year')
plt.ylabel('No. of Commits')
plt.title('Number of Commits in each year')
plt.savefig('commit_count.png')
plt.show()

data = pd.read_csv('author_count.csv')

a = data.to_dict('records')
xx = {}
for b in a:
    xx[b['Author Name']] = b['Count']

c = dict(sorted(xx.items(), key=lambda item: item[1], reverse=True))
Top5Authors = {k: c[k] for k in list(c)[1:6]}

plt.bar(Top5Authors.keys(), Top5Authors.values())
plt.xlabel('Author Name')
plt.ylabel('No. of Commits')
plt.title('TOP CONTRIBUTORS')
plt.savefig('author_count.png')
plt.show()



