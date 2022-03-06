import sys
import math
import PyQt5.QtWidgets as qtw

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


class MainWindow(qtw.QWidget):
    """
    Класс для реализации графического интерфейса.
    Также выполняются арифметические операции, после перевода в 10-ую
    """

    def __init__(self):
        """
        Задаётся окно размером 300x600, создаются поля для ввода
        """

        super().__init__()
        self.setWindowTitle("Калькулятор Баслин Ярослав БПМ-20-3")
        self.setGeometry(300, 300, 600, 600)
        self.setLayout(qtw.QVBoxLayout())

        my_label_1 = qtw.QLabel("Введите первое число:")
        self.layout().addWidget(my_label_1)
        n = qtw.QLineEdit()
        self.layout().addWidget(n)

        my_label_6 = qtw.QLabel("Введите систему исчисления для 1:")
        self.layout().addWidget(my_label_6)
        base_1 = qtw.QLineEdit()
        self.layout().addWidget(base_1)

        my_label_2 = qtw.QLabel("Введите второе число:")
        self.layout().addWidget(my_label_2)
        m = qtw.QLineEdit()
        self.layout().addWidget(m)

        my_label_3 = qtw.QLabel("Введите систему исчисления для 2:")
        self.layout().addWidget(my_label_3)
        base_2 = qtw.QLineEdit()
        self.layout().addWidget(base_2)

        my_label_4 = qtw.QLabel("Операция:")
        self.layout().addWidget(my_label_4)
        oper = qtw.QLineEdit()
        self.layout().addWidget(oper)

        my_label_5 = qtw.QLabel("Введите систему исчисления результата:")
        self.layout().addWidget(my_label_5)
        base_3 = qtw.QLineEdit()
        self.layout().addWidget(base_3)

        my_button = qtw.QPushButton("Посчитать", clicked=lambda: button_event())
        self.layout().addWidget(my_button)

        my_label_ = qtw.QLabel("Ответ:")
        self.layout().addWidget(my_label_)

        self.show()

        def button_event():
            """Получаем значения полей, выполняем операцию, проверка на невалидность операций."""
            n_ = n.text()
            m_ = m.text()
            base_1_ = base_1.text()
            base_2_ = base_2.text()
            base_3_ = base_3.text()
            oper_ = oper.text()

            try:
                n_ = to_decimal(n_, base_1_)
                m_ = to_decimal(m_, base_2_)

            except RuntimeError:
                m_ = None
                n_ = None
                my_label_1.setText("Неверное основание для чисел")

            except AttributeError:
                my_label_1.setText("Неверное основание для ")

            if m_ is not None and n_ is not None:
                if m_ == '0' and oper_ == '/':
                    my_label_.setText('Деление на 0')

                elif int(n_) < int(m_) and oper_ == '-':
                    ans = eval(str(m_) + oper_ + str(n_))
                    strr = number_to_provided(ans, base_3_)
                    my_label_.setText(f'Ответ: {strr}')

                elif oper_ != '+' and oper_ != '-' and oper_ != '*' and oper_ != '/':
                    my_label_.setText("Неизвестная операция")

                elif int(m_) != 0 and int(n_) % int(m_) != 0 and oper_ == '/':
                    ans = eval(str(n_) + oper_ + str(m_))
                    strr = float_to_provided(ans, base_3_)
                    my_label_.setText(f'Ответ {strr}')

                else:
                    ans = eval(str(n_) + oper_ + str(m_))
                    strr = number_to_provided(ans, base_3_)
                    my_label_.setText(f'Ответ: {strr}')


def main():
    app = qtw.QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



