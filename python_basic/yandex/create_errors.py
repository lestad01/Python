# генерация ошибки с помощью RAISE

def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b


try:
    divide_nums(10, 0)
except Exception as e:
    print(e)

print('Continue...')


# home work
# создайте функцию image_info с одним параметром типа dict
# функция ожидает словарь, в котором дб как минимум 2 ключа: image_id, image_title
# функция должна возвращать строку такого вида "image my cat has id 5136"
# если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку TypeError
# вызовите функцию и корректно обработайте ошибку в случае возникновения

def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image title must be present!")
    return f"Image '{img['image_title']}' has id {img['image_id']}"


print(image_info({'image_title': 'My account', 'image_id': 1211}))

try:
    print(image_info({'image_title': 'My account'}))
except Exception as e:
    print(e)
