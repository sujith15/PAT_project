import matplotlib.pyplot as plt
import csv

d={}
with open('pydriller_authorcount.csv', 'r') as csvfile:
    line = csv.reader(csvfile, delimiter=',')

    for row in line:
        d[row[0]]=int(row[1])
d.pop('Author Name')

print(int(d['Rich Graham']))
# temp = []
# res = dict()
# for key, val in d.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
print(d)

# plt.bar(d.keys(),d.values())
# plt.show()
# print(d)



