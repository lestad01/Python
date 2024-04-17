import datetime
my_name = 'Alex'

if my_name:
    print(True)


print(datetime.MINYEAR)


def name_func(name):
    string = ''
    if name == 'Alex':
        string = 'Hello,' + '{name}' + '.how are you?'
    else:
        string = 'Who you are?'
    return string


print(name_func('Maks'))
