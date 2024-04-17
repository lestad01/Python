grey_button = {
    'width': 200,
    'text': 'Buy',
    'color': 'grey'
}

red_button = {
    'color': 'red',
    **grey_button,

}

# print(red_button)
# print(grey_button)

# объединение словарей
button_default = {
    'text': 'Ok',
    'color': 'black',
    'width': 0,
    'height': 0
}

# button_info = {
#    'text': 'Buy'
# }

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 100
}

# button = {
#    **button_info,
#    **button_style
# }

button = {
    **button_default,
    **button_style
}
# button = button_default | button_style

print(button)
