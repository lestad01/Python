import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'C', 'B', 'A', 'C', 'A', 'B', 'C', 'A'],
    'Val1': np.random.randint(1, 100, size=10),
    'Val2': np.random.randint(1, 100, size=10),
}

df = pd.DataFrame(data)

# task 1 
group_df = df.groupby('Category').Val1.mean()

# print(group_df)

# task 2
max_val2 = df.groupby('Category').Val2.max()
# print(max_val2)

# task 3 
sum_val = df.groupby('Category')[['Val1','Val2']].sum()
# print(sum_val)

# task 4 

#max_min_val1 = df.groupby('Category')['Val1'].agg([min, max])
# print(max_min_val1)

# task 5 

#size_val = df.groupby('Category').size()
# print(size_val)

# task 6 
middle_val = df.groupby('Category')[['Val1', 'Val2']].median()

# print(middle_val)

# task 7  найти стандартное отклонение значений Val1
# std_val = df.groupby('Category')['Val1'].std()

# print(std_val)

# task 8 среднее знач VAl1 и сумму знач VAl2 для каждой категории
# sum_avg_val = df.groupby('Category').agg({'Val1': 'mean', 'Val2': 'sum'})
# print(sum_avg_val)

# 9 среднее знач и стандартное отклонение Val1 для каждой категории

# mean_std_val = df.groupby('Category')['Val1'].agg(['std', 'mean'])
# print(mean_std_val)


# 10 функцию к значен Val1 для каждой категории

def custom_function(x):
    return (x**2).sum()

val_func = df.groupby('Category')['Val1'].agg(custom_function)

print(val_func)