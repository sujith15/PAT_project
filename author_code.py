import pandas as pd
import matplotlib.pyplot as plt

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


