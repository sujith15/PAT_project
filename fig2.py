import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

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
plt.title('COMMITS COUNT')
plt.savefig('commit_count.png')
plt.show()

