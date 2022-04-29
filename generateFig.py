import pandas as pd
import matplotlib.pyplot as plt
import csv

# d={}
# with open('pydriller_authorcount.csv', 'r') as csvfile:
#     line = csv.reader(csvfile, delimiter=',')
#
#     for row in range(1,):
#         d[line[row][0]]=int(line[row][1])


# temp = []
# res = dict()
# for key, val in d.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
data = pd.read_csv('pydriller_authorcount.csv')

a = data.to_dict('records')
xx = {}
for b in a:
    xx[b['Author Name']] = b['Count']

c = dict(sorted(xx.items(), key=lambda item: item[1], reverse=True))
Top5Authors = {k: c[k] for k in list(c)[1:6]}

plt.bar(Top5Authors.keys(), Top5Authors.values())
plt.savefig('AuthorsCount.png')
plt.show()


