import sys
import datetime
from dateutil.parser import parse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

now = datetime.datetime.now()
year = [] # initialise list to store the years
with open(sys.argv[1], 'r') as f:
    friends = f.readlines()
    for friend in friends:
        year.append(friend.split('(')[1].strip('\n|)'))

today = "{} {} {}".format(now.day, now.strftime("%B"), now.year)

for i, j in enumerate(year):
    if j == 'Today':
        year[i] = today


dates = [parse(x) for x in year]

dateCount = {}
for item in set(dates):
    if item not in dateCount:
        dateCount[item] = 0
        for i, j in enumerate(dates):
            if j == item:
                dateCount[item] += 1

toViz = pd.Series(dateCount, name='DateValue')
toViz.index.name = 'Date'

cumulative = toViz.cumsum()

sns.set_style('white')
ax = cumulative.plot.area(color = '#43b2a7', alpha=0.5)
plt.gca().xaxis.grid(True)
plt.ylabel("Number of Friends")
sns.despine()
fig = plt.gcf()
plt.savefig('Friendios.png')
plt.show()

