# лямбда функция
lambda a, b: a * b


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")
print(morning_greeting('Aleksander'))

# evening_greeting = greeting("Good Evening")
# print(evening_greeting('Aleksander'))
