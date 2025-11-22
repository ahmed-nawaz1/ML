import pandas as pd ;

data  = [12, 15, 7, 20, 9]

series = pd.Series(data)

# print(series)
# print(series.size)
# print(series.head(3))

# Data as dictionary
data_2 = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
    "Math": [85, 90, 75, 82],
    "English": [78, 88, 80, 79],
    "Science": [92, 95, 85, 88]
}

# df = pd.DataFrame(data_2)

# print(df)

# print(df.columns)
# print(df.shape)


df = pd.read_json('em.json')

# print(df)
# print(df.head(3))
# print(df.tail(2))
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df[df["Salary"] > 50000])
# print(df[(df["Salary"] > 50000) & (df["Salary"] < 60000)])


print(df.head(3) , "\n" , df.tail(2))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df[df["Salary"]>50000])
print("it department employees:")
print(df[df["Department"] == "IT"])

