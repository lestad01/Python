# методы класса это функции
# любая функция объявленная в теле класса это метод
# в метод всегда приходит (параметр) self
# self - это обращение к себе. Тому кто вызвал этот метод
class User:
    def __init__(self):
        self.name = None
        self.age = None


user1 = User()
print(user1.__dict__)
print(user1.name)

# поменяли атрибут name
user1.name = "John"
print(user1.name)
