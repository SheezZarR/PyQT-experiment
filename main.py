import random
import sys
import math
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from pages import calc
from modules import number_systems, combinatorics, arrays, qsort, trees


class App(qtw.QMainWindow, calc.Ui_mainWindow):
    """PyQT app window."""

    node_array = arrays.NodeArray()
    common_array = arrays.CommonArray()
    arr_to_sort = []
    tree_array = trees.ArrayBinTree()

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.main_stack.setCurrentIndex(0)

        self.open_calc.clicked.connect(self.open_calculator)
        self.open_comb.clicked.connect(self.open_combinatorics)
        self.open_arrs.clicked.connect(self.open_arrays)
        self.open_tree.clicked.connect(self.open_tree_menu)
        self.open_sort.clicked.connect(self.open_algo)

        self.main_menu_button.clicked.connect(self.open_main_menu)
        self.comb_main_menu_button.clicked.connect(self.open_main_menu)
        self.arrays_main_menu_button.clicked.connect(self.open_main_menu)
        self.tree_main_menu_button.clicked.connect(self.open_main_menu)
        self.sorting_algo_main_menu_button.clicked.connect(self.open_main_menu)

        self.calculate_button.clicked.connect(self.number_transform)
        self.comb_calculate_button.clicked.connect(self.calc_combinatorics)
        self.execute_nd.clicked.connect(self.nd_act)
        self.execute_arr.clicked.connect(self.arr_act)
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

    def open_arrays(self):
        self.main_stack.setCurrentIndex(3)
        self.nd_stack.setCurrentIndex(0)
        self.arr_stack.setCurrentIndex(0)
        self.ndActionComboBox.currentIndexChanged.connect(self.change_nd_stack)
        self.arrActionComboBox.currentIndexChanged.connect(self.change_arr_stack)

    def open_tree_menu(self):
        self.main_stack.setCurrentIndex(4)
        self.tree_action_stack.setCurrentIndex(0)
        self.tree_combo_box.currentIndexChanged.connect(self.change_tree_stack)
        self.tree_run_action.clicked.connect(self.manage_tree_action)

    def open_algo(self):
        self.main_stack.setCurrentIndex(5)
        self.generate_array.clicked.connect(self.array_generator)
        self.sort_array_button.clicked.connect(self.sort_array)

    def change_combo_stack(self, page_id):
        self.combinatoric_stack.setCurrentIndex(page_id)

    def change_nd_stack(self, page_id):
        self.nd_stack.setCurrentIndex(page_id)

    def change_arr_stack(self, page_id):
        self.arr_stack.setCurrentIndex(page_id)

    def change_tree_stack(self, page_id):
        self.tree_action_stack.setCurrentIndex(page_id)

    def manage_tree_action(self):
        action_result = ""

        if self.tree_combo_box.currentIndex() == 0:
            # Add
            elements = list(map(int, self.add_tree_elemLineEdit.text().split(' ')))

            for elem in elements:
                self.tree_array.add_element(elem)

        elif self.tree_combo_box.currentIndex() == 1:
            # Insert
            element = int(self.insert_tree_elemLineEdit.text())
            position = int(self.insert_tree_posLineEdit.text())
            self.tree_array.insert_element(position, element)

        elif self.tree_combo_box.currentIndex() == 2:
            # Remove
            element = int(self.remove_tree_elemLineEdit.text())
            self.tree_array.remove_element(element)

        elif self.tree_combo_box.currentIndex() == 3:
            # Show parent
            element = int(self.tree_childLineEdit.text())
            action_result += self.tree_array.show_parent(element) + '\n'

        elif self.tree_combo_box.currentIndex() == 4:
            # Show children
            element = int(self.tree_parentLineEdit.text())
            action_result += self.tree_array.show_children(element) + '\n'

        action_result += self.tree_array.show_tree()

        self.tree_output_textBox.setText(action_result)

    # TODO: merge arr_act & nd_act into separate file
    def nd_act(self):
        """
        Функция управления односвязным списком.
        """
        action = self.ndActionComboBox.currentText()

        if action == "Добавить":
            items = self.addActionLineEdit_nd.text().split(' ')

            for item in items:
                self.node_array.add(arrays.Node(int(item)))

        elif action == "Вставить":
            position = int(self.insertPositionLineEdit_nd.text())
            item = int(self.insertValueLineEdit_nd.text())

            try:
                self.node_array.insert_at(position, arrays.Node(item))
            except Exception as e:
                self.nd_result_text.setText(e.__str__())

        elif action == "Удалить":
            try:
                self.node_array.remove()
            except Exception as e:
                self.nd_result_text.setText(e.__str__())
                return

        elif action == "Убрать элем.":
            position = int(self.RemovePosLineEdit_nd.text())

            try:
                self.node_array.remove_at(position)
            except Exception as e:
                self.nd_result_text.setText(e.__str__())
                return

        else:
            self.nd_result_text.setText("Неизвестная операция...")
            return

        self.nd_result_text.setText(self.node_array.__str__())

    def arr_act(self):
        """
        Функция управления взаимодействия с массивом.
        """
        action = self.arrActionComboBox.currentText()

        if action == "Добавить":
            items = self.addActionLineEdit_arr.text().split(' ')

            for item in items:
                self.common_array.add(int(item))

        elif action == "Вставить":
            position = int(self.insertPositionLineEdit_arr.text())
            item = int(self.insertValueLineEdit_arr.text())

            try:
                self.common_array.insert_at(position, item)
            except Exception as e:
                self.arr_result_text.setText(e.__str__())

        elif action == "Удалить":
            try:
                self.common_array.remove()
            except Exception as e:
                self.arr_result_text.setText(e.__str__())
                return

        elif action == "Убрать элем.":
            position = int(self.RemovePosLineEdit_arr.text())

            try:
                self.common_array.remove_at(position)
            except Exception as e:
                self.arr_result_text.setText(e.__str__())
                return

        else:
            self.arr_result_text.setText("Неизвестная операция...")
            return

        self.arr_result_text.setText(self.common_array.__str__())

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

    def array_generator(self):
        self.arr_to_sort = []
        random.seed(random.random())

        for i in range(random.randrange(1, 20, 1)):
            self.arr_to_sort.append(random.randint(1, 1999321) % 100 * 7 % 100)

        self.raw_array_text.setText(f"Массив: { self.arr_to_sort }")

    def sort_array(self):
        qsort.qsort(0, len(self.arr_to_sort) - 1, self.arr_to_sort)
        self.sorted_array_text.setText(f"Результат: { self.arr_to_sort }")


def main():
    app = qtw.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
