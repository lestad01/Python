class User:
    name = None
    age  = None

user1 = User()
print("user1.age", user1.age)
print("user1.name", user1.name)
print(user1.__dict__)


user1.name = "John"
print("user1.name", user1.name)
print(user1.__dict__)

user2 = User()
user2.name = "Alex"
user2.age = 20
print(user2.__dict__)

User.age = 0
print(user1.age)
print(user1.__dict__)

user1.age = 15

print(user1.age)
print(user1.__dict__)