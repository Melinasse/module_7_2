def custom_write(file_name, strings,):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i , string in enumerate(strings, 1): # i - номер элемента списка, string - элемент спика, strings - итерируемый объект
        dots = file.tell()
        file.write(f'{string}\n')
        string_positions[(i, dots)] = string # Запись ключа в словарь в виде кортежа приравненному значению.
    file.close()
    return string_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.','Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
