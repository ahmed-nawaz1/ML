import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('/kaggle/input/datasets/hijiii/ipl-capstone-project-matplotlib/IPL.csv')
# df.head()


# df.info()

# Check the size of rows and columns of the dataset
row = df.shape[0]

column = df.shape[1]

# Now let's see how many columns have null values in total.
nullColumn = df.isnull().sum()

# Which team won the most matches?
matchWinner = df['match_winner'].value_counts()
barPlot = sns.barplot(y = matchWinner.index , x = matchWinner.values)

# Toss Decision Trends
decisionTrends = sns.countplot(x= df['toss_decision'])

# Toss Winner vs Match Winner
count = df[df['toss_winner'] == df['match_winner']]['match_id'].count()
percentage = (count *100)/df.shape[0]
percentage.round(2)

# How do teams win? (Runs vs Wickets)
sns.countplot(x= df['won_by'])

# 1 Most "Player of the Match" Awards

playerOfMatch = df['player_of_the_match'].value_counts().head(10)

sns.barplot(y = playerOfMatch.index , x = playerOfMatch.values )



