import sys
import math
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from pages import calc
from modules import number_systems, combinatorics


class App(qtw.QMainWindow, calc.Ui_mainWindow):
    """PyQT app window."""

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.main_stack.setCurrentIndex(0)

        self.open_calc.clicked.connect(self.open_calculator)
        self.open_comb.clicked.connect(self.open_combinatorics)

        self.main_menu_button.clicked.connect(self.open_main_menu)
        self.comb_main_menu_button.clicked.connect(self.open_main_menu)
        self.calculate_button.clicked.connect(self.number_transform)
        self.comb_calculate_button.clicked.connect(self.calc_combinatorics)
        self.add_k_type.clicked.connect(self.add_new_k_type)
        self.remove_k_type.clicked.connect(self.remove_new_k_type)


    def open_main_menu(self):
        self.main_stack.setCurrentIndex(0)

    def open_calculator(self):
        self.main_stack.setCurrentIndex(1)

    def open_combinatorics(self):
        self.main_stack.setCurrentIndex(2)
        self.combinatoric_stack.setCurrentIndex(0)
        self.comboBox.currentIndexChanged.connect(self.change_combo_stack)

    def change_combo_stack(self, page_id):
        self.combinatoric_stack.setCurrentIndex(page_id)

    def add_new_k_type(self):
        self.form_with_types.addRow(
            qtw.QLabel(f"Тип {self.form_with_types.rowCount()}, кол-во: "),
            qtw.QLineEdit()
        )

    def remove_new_k_type(self):
        self.form_with_types.removeRow(self.form_with_types.rowCount() - 1)

    def calc_combinatorics(self):
        ans = 0

        if self.combinatoric_stack.currentIndex() == 0:
            ans = combinatorics.permutations(len(set(self.alphabet_input.text().split(" "))))

        elif self.combinatoric_stack.currentIndex() == 1:
            if self.form_with_types.rowCount() > 1:
                numbers_of_types = []
                sum = 0
                total_n = int(self.nInput_perm_n_k.text())

                for i in range(self.form_with_types.rowCount()):
                    amount = int(self.form_with_types.itemAt(i, 1).widget().text())
                    numbers_of_types.append(amount)
                    sum += amount

                if total_n == sum:

                    ans = combinatorics.permutations_duplicates(
                        total_n,
                        numbers_of_types
                    )
                else:
                    ans = "не совпадает количество предметов общее и под частям."
            else:
                ans = "необходимо добавить более двух типов предметов."

        elif self.combinatoric_stack.currentIndex() == 2:
            ans = combinatorics.partial_permutation(
                int(self.nInput_partial.text()),
                int(self.mInput_partial.text())
            )

        elif self.combinatoric_stack.currentIndex() == 3:
            ans = combinatorics.partial_permutation_dubplicates(
                int(self.nInput_rpartial.text()),
                int(self.mInput_rpartial.text())
            )

        elif self.combinatoric_stack.currentIndex() == 4:
            ans = combinatorics.combinations(
                int(self.nInput_comb.text()),
                int(self.mInput_comb.text())
            )

        elif self.combinatoric_stack.currentIndex() == 5:
            ans = combinatorics.combinations_duplicates(
                int(self.nInput_rcomb.text()),
                int(self.mInput_rcomb.text())
            )

        self.comb_ans_box.setText(f"Ответ: {ans}")

    def number_transform(self):
        n_ = self.num_1.text()
        m_ = self.num_2.text()
        base_1_ = self.base_1.text()
        base_2_ = self.base_2.text()
        base_3_ = self.base_3.text()
        oper_ = self.oper.text()

        try:
            n_ = number_systems.to_decimal(n_, base_1_)
            m_ = number_systems.to_decimal(m_, base_2_)

        except RuntimeError:
            m_ = None
            n_ = None
            self.label_ans.setText("Неверное основание для чисел")

        except AttributeError:
            self.label_ans.setText("Неверное основание для ")

        if m_ is not None and n_ is not None:
            if m_ == '0' and oper_ == '/':
                self.label_ans.setText('Деление на 0')

            elif int(n_) < int(m_) and oper_ == '-':
                ans = eval(str(m_) + oper_ + str(n_))
                strr = number_systems.number_to_provided(ans, base_3_)
                self.label_ans.setText(f'Ответ: {strr}')

            elif oper_ != '+' and oper_ != '-' and oper_ != '*' and oper_ != '/':
                self.label_ans.setText("Неизвестная операция")

            elif int(m_) != 0 and int(n_) % int(m_) != 0 and oper_ == '/':
                ans = eval(str(n_) + oper_ + str(m_))
                strr = number_systems.float_to_provided(ans, base_3_)
                self.label_ans.setText(f'Ответ {strr}')

            else:
                ans = eval(str(n_) + oper_ + str(m_))
                strr = number_systems.number_to_provided(ans, base_3_)
                self.label_ans.setText(f'Ответ: {strr}')


def main():
    app = qtw.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
