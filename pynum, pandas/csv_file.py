import pandas as pd

csv = pd.read_csv('telegram_accounts.csv')
print(csv.head(10))
print(csv.shape)

pd.set_option('display.min_rows', 100)

print(csv)