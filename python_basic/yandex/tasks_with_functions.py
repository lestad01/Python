
# задача по функцим № 1
def merge_lists_to_dict(first_list, second_list):
    new_list = dict(zip(first_list, second_list))
    return new_list


merge_func = merge_lists_to_dict(first_list=[1, 2, 0, 11], second_list=[
                                 True, 'Charlie', '86', 'Alex'])
merge_func_onearg = merge_lists_to_dict([1, 2, 3, 4], second_list=[
    True, 'Charlie', '86', 'Alex'])
print(merge_func)
print(merge_func_onearg)

# Создайте функцию update_car_info
# в которой все именованные аргументы будут
# объединяться в словарь car


# def update_car_info(**args):
#    print(args)
#    car = {
#        f"Mark of car: {args['mark']} "
#        f"year of manufacture of the car: {args['year']}"
#    }
#    return car

def update_car_info(**car):
    car['is_available'] = True
    return car


message = update_car_info(brand='Audi', price=1650000)
# TypeError: update_car_info() takes 0 positional arguments but 1 was given
second_message = update_car_info('Audi', price=1650000)
print(message)
print(second_message)
