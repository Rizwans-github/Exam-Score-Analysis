
'''
In this project, I'm conducting an in-depth analysis of exam scores using Python. 
Using  libraries like NumPy, Matplotlib, Seaborn, and Pandas, I'm dissecting various dimensions of student performance. 
From scrutinizing gender distributions and exploring the correlation with parent's education to dissecting ethnic group disparities and
examining sports participation, 
'''

# Importing necessary libraries for data analysis and visualization
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Loading exam score data from a CSV file into a Pandas DataFrame named df
df = pd.read_csv('C:/Users/Mohd Rizwan/Downloads/Da Project/Exam Score Analysis using Python/Expanded_data_with_more_features.csv')

# Displaying the first few rows and summary statistics of the DataFrame
df.head()
df.describe()
df.info()


# Dropping an unnecessary column named 'Unnamed: 0'
df = df.drop('Unnamed: 0', axis = 1)
df.head(1)


# Standardizing gender labels (changing 'female' to 'Female' and 'male' to 'Male')
df['Gender'] = df['Gender'].replace(['female','male'], ['Female', 'Male'])
df.head()

# Checking for missing values in the DataFrame
df.isna().sum()

# Visualizing the gender distribution using a bar chart
plt.figure( figsize = (3,3))
ax = sns.countplot(data = df, x = 'Gender' )
plt.ylabel('Count', color = '#3274a1', fontsize = 11)
plt.xlabel('Gender', color = '#3274a1', fontsize = 11)
plt.xticks(fontsize = 10, color = '#3274a1')
plt.yticks(fontsize = 10, color = '#3274a1')
plt.title('Graph',fontsize = 12, weight = 'bold', color = '#3274a1')
ax.bar_label(ax.containers[0], label_type = 'center', color = 'white', fontsize= 10)
plt.show()


# Visualizing gender distribution with hue using a bar chart
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

# Printing the count of male students
print((df['Gender']=='Male').sum())

# Grouping data by parent's education and calculating mean scores
gb = df.groupby('ParentEduc').agg({'MathScore': 'mean', 'ReadingScore': 'mean', 'WritingScore': 'mean'})
print(gb)

# Visualizing the relationship between parent's education and student scores using a heatmap
plt.figure(figsize = (4,4))
sns.heatmap(gb, cmap = 'BuGn')
plt.xticks(rotation = 15, color = '#03441b', weight = 'semibold')
plt.yticks(color = '#03441b', weight = 'semibold')
plt.ylabel('Parent\'s Education', color = '#03441b', fontsize = 14, weight = 'bold')
plt.title('Relationship b/w Parent\'s Education & Student\'s Score', color = '#03441b', weight = 'bold')
plt.show()

# Visualizing distribution using box plots for Math, Reading, and Writing scores
plt.figure(figsize=(3, 3))
sns.boxplot(data=df, x="MathScore")
plt.show()

plt.figure(figsize=(3, 3))
sns.boxplot(data=df, x="ReadingScore")
plt.show()

plt.figure(figsize=(3, 3))
sns.boxplot(data=df, x="WritingScore")
plt.show()

# Printing unique values in the 'EthnicGroup' column
print(df['EthnicGroup'].unique())

# Counting and visualizing distribution of students across ethnic groups using a pie chart
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


# Visualizing mode of transport used by students with gender breakdown using a bar chart
plt.figure(figsize=(4, 3))
ax = sns.countplot(data=df, x='TransportMeans', hue='Gender')
plt.legend(title='Legend', bbox_to_anchor=(1, 1))
for container in ax.containers:
    ax.bar_label(container, weight='bold', color='white', label_type='center', fontsize=11)
plt.ylabel('No. of Students', color='#3274a1', weight='bold')
plt.title('Mode of Transport used', color='#3274a1', weight='bold')
plt.xlabel('Mode', color='#3274a1', weight='bold')
plt.show()

# Grouping data by sports practice and calculating mean scores
Sports = df.groupby('PracticeSport').agg({'MathScore': 'mean', 'WritingScore': 'mean', 'ReadingScore': 'mean'})
print(Sports)

# Visualizing the relationship between sports practice and student scores using a heatmap
sns.heatmap(Sports, cmap='viridis')
plt.show()

#CONCLUSION
'''
To sum up our analysis, we've dived into different aspects of student data. We looked at gender distributions, the influence of parent's education, and explored ethnic group disparities, along with modes of transport and sports participation. Visualizations, like count plots and heatmaps, helped paint a clear picture.

This project showcases the effectiveness of Python's data analytics tools in extracting meaningful insights from a comprehensive dataset. It emphasizes the importance of data analysis in understanding patterns and gaining valuable insights into the factors that impact student scores.

In a nutshell, our exploration underlines the rich stories hidden within the data, demonstrating the power of analytical tools in deciphering these narratives.
'''