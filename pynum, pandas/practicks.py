import pandas as pd

#df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # apply, applymap

# apply
# def custom_logic(x):
    #return x.sum()
# new_df = df.apply(custom_logic, axis=1) # rows 1
# new_df = df.apply(custom_logic, axis=0) # columns - 0


# applymap
# def custom_logic(x):
#     return x + 1
# new_df = df.applymap(custom_logic)


# print(df)
# print(new_df)

# tasks 
# 1 получите сводную инфу о DataFrame с использованием .describe()
#print(df.A.describe())

# 2 Увеличьте зарплату на 10% с использованием .map() 
data = {
    'Age': [25, 30, 22, 18, 43],
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Jason'],
    'Salary': [50000, 43000, 75000, 86000, 77000],
}

df = pd.DataFrame(data)

# меняем с числового индекса на наименование столбца. В нашем случае это будет Name
df.set_index('Name', inplace=True)

# def sum_logic(x):
#     return x + 15/100

df['Salary'] = df['Salary'].map(lambda x: x*1.3)
# print(df)

# 3 Создать новый столбец 'Seniority' используя возраст и apply()
def set_seniority(age):
    if age < 35:
        return 'Junior'
    elif age < 45:
        return 'Adult'
    else:
        return 'Senior'
df['Senior'] = df['Age'].apply(set_seniority)

# print(df)

# 4 Примените функцию map() для изменения знач возраста с помощью словаря

age_mapping = {25: '25-29', 30: '30-34', 35: '35-39', 40: '40-44', 45: '45-49'}

df['Age'] = df['Age'].map(age_mapping)
#print(df)

# 5 используйте функцию applymap() для отобрадения всех числовых значений в DataFrame как строки
def custom_format(element):
    if isinstance(element, (int, float)):
        return str(element)
    return element

df = df.applymap(custom_format)
print(type(df))

