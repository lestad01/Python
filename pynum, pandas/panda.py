import pandas as pd

numbers = [1,2,3,4.2,5, '213']

# series тип данных надстройка над numpy массивом и содержит данные одного типа
series = pd.Series(numbers)

#print(series)


#print(series[1])

names = ['John', 'Jade', 'Alice']
ages = [23,12,43]

series_with_name = pd.Series(ages, index=names)

print(f'Age by name : {series_with_name["John"]}')

series_with_name['John'] = 18
print(series_with_name)


data = {
    'Bob': ['I liked that', 'That was awful'],
    'Suzi' : ['Pretty Good', 'Tasty']
}

pd.DataFrame(
    data,
    index= ['Product A', 'Product B']
)

data_2 = [30, 12, 44]
series_2 = pd.Series(
    data_2,
    index= ['A', 'B', 'C'],
    name= 'Products'
)

print(series_2)