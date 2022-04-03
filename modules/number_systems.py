import math

list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'       # для быстрого перевода

# Перевод ИЗ любой СИ в десятичную
def to_decimal(number: str, base: str) -> str:
    base = int(base)
    number = number[::-1]
    number_rez = 0

    for i in range(len(number)):
        if list.index(number[i]) >= base or base == 1:
            raise RuntimeError()

        number_rez += list.index(number[i]) * base ** i

    return number_rez


# Перевод в любую СИ путём деления и получения остатка из 10
def number_to_provided(number: str, base: str) -> str:
    """Перевод числа в основание со значением base. """

    base = int(base)
    number = int(number)    # для перевода
    number_rez = ''         # хранится число

    if base == 1:
        raise AttributeError()

    while number // base != 0:
        number_rez += str(list[number % base])
        number = number // base

    number_rez += str(list[number % base])  # последняя цифра
    number_rez = number_rez[::-1]           # разворачиваем число, оно записано слева направо, вместо 225 522

    # убираем ведущие нули в числе
    zero_counter = 0
    while number_rez[zero_counter] == '0':
        zero_counter += 1
        if zero_counter >= len(number_rez):
            zero_counter -= 1
            break

    return number_rez[zero_counter::]       # возвращаем число в виде строки, с удалением ведущих нулей


# Перевод в любую СИ путём деления и получения остатка из 10
# + перевод дробной части.
def float_to_provided(float_number: float, base: str) -> str:
    base = float(base)
    float_number_ = float_number
    integral_part = int(float_number_)
    fractional_part = float_number_ - integral_part

    integral_converted = number_to_provided(str(integral_part), base)
    fractional_converted = ""
    for i in range(0, 23):
        fractional_part *= base

        if int(fractional_part) >= 0:
            fractional_converted += list[int(fractional_part)]
            fractional_part -= int(fractional_part)

        else:
            fractional_converted += '0'

        if math.isclose(fractional_part, 0, rel_tol=1e-09, abs_tol=0.0):
            break

    print(integral_converted + '.' + fractional_converted)

    return str(integral_converted + '.' + fractional_converted)
