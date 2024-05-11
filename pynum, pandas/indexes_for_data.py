import pandas as pd

data = {
    'Age': [25, 30, 22, 18, 43],
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Jason'],
    'Salary': [50000, 43000, 75000, 86000, 77000],
}

df = pd.DataFrame(data)

# меняем с числового индекса на наименование столбца. В нашем случае это будет Name
df.set_index('Name', inplace=True)

# changed_df = df.loc[['Alice', 'Carol']]

# changed_df = df.iloc[[0, 2]]

# changed_df = df.loc[['Bob', 'Jason'] , 'Age']

# changed_df = df.iloc[1, 0]

changed_df = df.loc[df['Age'] > 30]

print(type(changed_df))



