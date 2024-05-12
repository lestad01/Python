import pandas as pd
import numpy as np
csv = pd.read_csv('new_money.csv')
pd.set_option('display.min_rows', 100)

def populate_age(row):
    try: 
        money_str = row['money'][1:]
        money = float(money_str)

        if money > 15000:
            age = np.random.randint(18, 35)
        else:
            age = np.random.randint(35, 75)
        
        row['age'] = age
        return row
    except ValueError as _ex:
        print(f'Error processing row: {row}')
        return np.nan

count_df_new = csv.apply(populate_age, axis='columns')
print(count_df_new)

