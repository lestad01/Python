import random

# i = 10
# while i < 50:
#     print(i)
#     i += 10

# while True:
#     answer = input("Enter yes or no: ")
#     if answer == 'no':
#         break

# continue

random_num = random.randint(1, 8)
# while True:
#     num = int(input("Guess the number 1 to 8: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulations!", random_num)
#     break


# Task
# while True:
#     try:

#         num_one = float(input("Please enter number one: "))
#         num_two = float(input("Please enter number two: "))
#     except ValueError as e:
#         print(e)
#         print("You must enter numbers!")
#         continue

#     print(num_one / num_two)
#     answer = input("Do you want to continue? (yes/no): ")
#     if answer == 'no':
#         break

# сокращенный for in
# all_nums = [-3, 1, 0, -10, 21, 3]

# absolute_nums = [abs(num) for num in all_nums]
# print(absolute_nums)

# # ---------------------

# new_all_nums = [2, -1, 2, 0, 4, 9, -11, 23]

# positivie_nums = [num for num in new_all_nums if num > 0]

# print(positivie_nums)
# # ----------------------------

# my_set = {1, 10, 15}

# new_set = {val * val for val in my_set}

# print(new_set)
# # -----------------------------

# my_scores = {
#     'a': 10,
#     'b': 7,
#     'c': 14
# }

# scores = {k: v * 10 for k, v in my_scores.items()}

# scores = {}

# for k, v in my_scores.items():
#     scores[k] = v * 10
#     print(scores)


my_new_scores = [10, 7, 11]

scores = {index: element * 2 for index, element in enumerate(my_new_scores)}

print(scores)
# Task

my_motorbike = {
    'brand': 'bmv',
    'country': 'Germany',
    'owner': 'Aleksandr'
}

bike = {k: v.upper() for k, v in my_motorbike.items()}

print(bike)

# task 2

new_list_motorbike = ['BMW', 'Germany', 'Aleksandr']
new_bike = [elem for elem in new_list_motorbike if len(elem) > 3]
print(new_bike)
