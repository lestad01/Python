import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25,35,30,27,21],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Seattle']
# }

# d_f = pd.DataFrame(
#     data,
#     index=['A', 'B', 'C', 'D', 'E']
# )
# print(d_f)
# new_df = d_f.iloc[1]
# new_df = d_f.loc['D']
#print(new_df)

# new_df = d_f.iloc[1, 2]
# new_df = d_f.iloc[1:3]
# new_df = d_f.loc['B', 'Age']
# print(new_df)

csv = pd.read_csv('telegram_accounts.csv')

#pd.reset_option('display.min_rows')


# last_elem = csv.iloc[-5:]
# bio_csv = csv.loc[:, 'phone_number']

# nw_csv = csv.loc[csv.status =='online']
# print(last_elem)
# print(bio_csv)

check_name_verification = (csv.status =='online') & (len(csv.username) > 10)
not_verfied = csv.loc[check_name_verification]
len(not_verfied.head())
df_copy = not_verfied.copy() 
df_copy['status'] = 'offline'

print(not_verfied['status'])
print(df_copy['status'])