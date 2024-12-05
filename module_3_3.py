# Задача "Распаковка"
# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()  # Вывод значений параметров
print_params(5, 'мяч', False)  # Вызов функции с тремя аргументами
print_params(77,'снег') # Вызов функции с двумя аргументами + 1 по умолчанию
print_params(b='ваза')  # Вызов функции с одним аргументом + 2 по умолчанию
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров:
values_list = [200, 'вода', False]
values_dict = {'a': 300, 'b': 'роза', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


