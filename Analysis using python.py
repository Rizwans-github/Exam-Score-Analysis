import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/Mohd Rizwan/Downloads/Da Project/Exam Score Analysis using Python/Expanded_data_with_more_features.csv')
df.head()
df.describe()
df.info()

df = df.drop('Unnamed: 0', axis = 1)
df.head(1)


df['Gender'] = df['Gender'].replace(['female','male'], ['Female', 'Male'])
df.head()

df.isna().sum()


plt.figure( figsize = (3,3))
ax = sns.countplot(data = df, x = 'Gender' )
plt.ylabel('Count', color = '#3274a1', fontsize = 11)
plt.xlabel('Gender', color = '#3274a1', fontsize = 11)
plt.xticks(fontsize = 10, color = '#3274a1')
plt.yticks(fontsize = 10, color = '#3274a1')
plt.title('Graph',fontsize = 12, weight = 'bold', color = '#3274a1')
ax.bar_label(ax.containers[0], label_type = 'center', color = 'white', fontsize= 10)
plt.show()



plt.figure( figsize = (3,3))
ax = sns.countplot(data = df, x = 'Gender' , hue = 'Gender')
plt.ylabel('Count', color = '#3274a1', fontsize = 11)
plt.xlabel('Gender', color = '#3274a1', fontsize = 11)
plt.xticks(fontsize = 10, color = '#3274a1')
plt.yticks(fontsize = 10, color = '#3274a1')
plt.title('Graph',fontsize = 12, weight = 'bold', color = '#3274a1')
for container in ax.containers:
    ax.bar_label(container, label_type = 'center', color = 'white', fontsize = 11)
plt.show()

print((df['Gender']=='Male').sum())


gb = df.groupby('ParentEduc').agg({'MathScore': 'mean', 'ReadingScore': 'mean', 'WritingScore': 'mean'})
print(gb)


plt.figure(figsize = (4,4))
sns.heatmap(gb, cmap = 'BuGn')
plt.xticks(rotation = 15, color = '#03441b', weight = 'semibold')
plt.yticks(color = '#03441b', weight = 'semibold')
plt.ylabel('Parent\'s Education', color = '#03441b', fontsize = 14, weight = 'bold')
plt.title('Relationship b/w Parent\'s Education & Student\'s Score', color = '#03441b', weight = 'bold')
plt.show()

plt.figure(figsize = (3,3))
sns.boxplot(data = df, x = "MathScore")
plt.show()

plt.figure(figsize = (3,3))
sns.boxplot(data = df, x = "ReadingScore")
plt.show()

plt.figure(figsize = (3,3))
sns.boxplot(data = df, x = "WritingScore")
plt.show()

print(df['EthnicGroup'].unique())


groupA = df.loc[(df['EthnicGroup'] == 'group A')].count()
groupB = df.loc[(df['EthnicGroup'] == 'group B')].count()
groupC = df.loc[(df['EthnicGroup'] == 'group C')].count()
groupD = df.loc[(df['EthnicGroup'] == 'group D')].count()
groupE = df.loc[(df['EthnicGroup'] == 'group E')].count()
Label = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
mlist = [groupA['EthnicGroup'], groupB['EthnicGroup'], groupC['EthnicGroup'],  groupD['EthnicGroup'], groupE['EthnicGroup']]
plt.figure(figsize =(5,5))
plt.pie( mlist, labels = Label, autopct = '%1.2f%%', labeldistance = 1.05, textprops = {'weight': 'bold', 'color': 'black'})
plt.title('Distribution of Ethnic Groups', weight = 'bold', color = 'teal')
plt.legend(Label, bbox_to_anchor = (1.3, 1), title = 'Legend')
plt.show()
print(mlist)


plt.figure(figsize = (4,3))
ax = sns.countplot(data= df, x='TransportMeans', hue = 'Gender')
plt.legend(title = 'Legend', bbox_to_anchor = (1,1))
for container in ax.containers:
    ax.bar_label(container, weight = 'bold', color = 'white', label_type = 'center', fontsize = 11)
plt.ylabel('No. of Students', color = '#3274a1', weight = 'bold')
plt.title('Mode of Transport used', color = '#3274a1', weight = 'bold')
plt.xlabel('Mode', color = '#3274a1', weight = 'bold')
plt.show()

Sports = df.groupby('PracticeSport').agg({'MathScore': 'mean', 'WritingScore': 'mean', 'ReadingScore': 'mean'})
print(Sports)

sns.heatmap(Sports, cmap = 'viridis')
plt.show()
