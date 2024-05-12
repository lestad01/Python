import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)


def add_new_column(elem):
    return elem + 12

df['C'] = df['A'].map(add_new_column)



group_df = df.groupby('B').count()

new_data = {'A': -5, 'B': 50, 'C': 63}

df_new = pd.DataFrame([new_data])


new_pd = pd.concat([df, df_new])

#print(df_new)

#print(group_df)

# newpd_group = new_pd.groupby('B').count()
# newpd_group = new_pd.groupby('B').min()
newpd_group = new_pd.groupby('B').max()
print(newpd_group)


# drop_col = df.drop(columns=['A', 'B']) # inplace = True
#drop_col = df.drop(index=1, columns=['A'])
drop_col = df[df.A == 3] # row
q = df.drop(drop_col.index)
print(q)

