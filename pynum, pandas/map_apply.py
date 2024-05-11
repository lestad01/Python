import pandas as pd

csv = pd.read_csv('new_money.csv')

# description_num = csv.first_name.describe()

# print(description_num)

# arr = csv.first_name.unique()

# print(len(arr))


data = {
    'Name': ['Alice', 'Boby', 'Charlie', 'David', 'Eva'],
    'Age': [25, 31, 23, 28, 34]
}

df = pd.DataFrame(data)

def add_five(el):
    return el + 5

# метод map
df['NewAge'] = df['Age'].map(add_five)

# print(df)


# apply 
# метод mean выводит среднее значение столбца
average_value = csv.id.mean()


def substract (row):
    row.id = row.id - average_value
    return row


cnt = csv.id.map(lambda id: id - average_value)

# print(cnt)

result = csv.apply(substract, axis='columns')

print(csv)
print(result)

