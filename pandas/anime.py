from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd;
import numpy as np;


df = pd.read_csv('/kaggle/input/datasets/hijiii/animedataset/anime.csv')

#make a new column for episode count
def episodeExtract(str):
    check = False
    data = ""
    for i in str:
        if i == ")":
            check = False
            return data
        if check == True :
            data  += i
        if i == "(" :
            check = True

df['Episodes'] = df['Title'].apply(episodeExtract)
df['Episodes'] = df['Episodes'].str.replace(' eps',"") 
df['Episodes'] = df['Episodes'].astype(int)

#make a new column for time stamp
def extraction_time(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1,i+20):
                data += txt[j]

            return data


df['Total Time'] = df['Title'].apply(extraction_time)

def calculate_total_months(period):
    try:
        start_str, end_str = period.split(' - ')
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        r = relativedelta(end_date, start_date)
        return r.years * 12 + r.months + 1  # +1 to include the starting month
    except:
        return None

df['Months'] = df['Total Time'].apply(calculate_total_months)

#which anime has the highest score
df[df['Score'] == df['Score'].max()]['Title']

#give me top 5 highest scoring anime
df['Title'].head(5)

#which anime has the highest episode count
df[df['Episodes'] == df['Episodes'].max()]

#animes with top 5 episode count
df['Title'].head()

# longest running anime (by duration in months)
longest_running = df.loc[df['Months'].idxmax()]