
import pandas as pd;

df = pd.read_csv('/kaggle/input/datasets/hijiii/countries/Countries.csv')

df

df.shape

df.describe()

#which country has the highest population
df[df['population']==df['population'].max()]['country']

df.columns

#what is the capital of the country with highest population
df[df['population'] == df['population'].max()]['capital_city']

#which country has the least population
df[df['population'] == df['population'].min()]['country']

#what is the capital of the country with least population
df[df['population'] == df['population'].min()]['capital_city']

df.head()

#give me top 5 countries with highest democratic score
df.sort_values(by='democracy_score' , ascending=False,inplace = True )
df['country'].head()

#how many total regions are there
df['region'].value_counts().count()

#how many countries lie in Eastern Europe region
df[df['region'] == 'Eastern Europe']['country']

#who is the political leader of the 2nd highest populated country
df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader']

#how many country have Republic in their full name
df['country_long'].str.contains('Republic' , case=False).sum()

#which country in african region has highest population
africa_df = df[df['continent'] == 'Africa']

africa_df [africa_df['population'] == africa_df['population'].max()]