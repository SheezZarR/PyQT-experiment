
class ArrayBinTree:

    _data = []

    def __init__(self):
        pass

    def resize(self, desired_size: int) -> None:
        """ Resizes a tree with empty. """

        for i in range(len(self._data), desired_size):
            self._data.append(None)

    def add_element(self, element: int) -> None:
        """ Adds an element to the tree. """

        for i in range(len(self._data)):
            if self._data[i] is None:
                self._data[i] = element
                return

        self._data.append(element)

    def insert_element(self, pos: int, element: int) -> None:
        """ Inserts an element at given position into the tree. """

        arr_size = len(self._data)

        parent = pos // 2 - 1 + pos % 2
        left_of_pos = pos // 2 - 1 + pos % 2
        right_of_pos = pos // 2 - 1 + pos % 2

        left = self._data[left_of_pos] if left_of_pos > arr_size else None
        right = self._data[right_of_pos] if right_of_pos > arr_size else None

        if parent < len(self._data):
            if not left and not right:
                if self._data[parent] and pos < len(self._data) - 1:
                    self._data[pos] = element
                else:
                    self.resize(desired_size=pos * 2 + 1)
                    self._data[pos] = element

                return

            raise IndexError(f"Невозможно вставить элемент {element} на позицию {pos}. Есть потомки!")

        raise IndexError(f"Невозможно вставить элемент {element} на позицию {pos}. Нет родителя!")

    def remove_element(self, elem: int) -> None:
        """ Removes an element at given position from the tree. """

        pos = self._data.index(elem)
        arr_size = len(self._data)

        if len(self._data) <= pos:
            raise IndexError(f"Невозможно удалить элемент на позиции {pos}!")

        left = (pos * 2 + 1) if pos * 2 + 1 < arr_size else 'Нету'
        right = (pos * 2 + 2) if pos * 2 + 2 < arr_size else 'Нету'

        if right != 'Нету' and left != 'Нету':
            raise RuntimeError(f"У удаляемого элемента есть потомок!")

        else:
            self._data[pos] = None
            if left != 'Нету':
                self._data[pos] = self._data[left]
                self._data[left] = None

            if right != 'Нету':
                self._data[pos] = self._data[right]
                self._data[right] = None

    def show_tree(self) -> str:
        """ Returns a string representing the tree. """

        if len(self._data) == 0:
            return "Пустое дерево"

        result = ""
        elem_per_level = 1
        countdown = elem_per_level
        for i in range(len(self._data)):
            if countdown > 0:
                result += str(self._data[i]) + " "
                countdown -= 1

            if countdown == 0:
                result += '\n'
                elem_per_level *= 2
                countdown = elem_per_level

        return result

    def show_parent(self, elem: int) -> str:
        """ Returns a string containing the parent element. """


        if self._data[0] == elem:
            return f"{elem} является корнем"

        elem_ind = self._data.index(elem)
        parent = elem_ind // 2 - 1 + elem_ind % 2

        return f"Родитель элемента: {elem}, будет: {self._data[parent]}."

    def show_children(self, elem: int) -> str:
        """ Returns a string containing the children elements. """

        elem_ind = self._data.index(elem)
        arr_size = len(self._data)

        left = self._data[elem_ind * 2 + 1] if elem_ind * 2 + 1 < arr_size and self._data[elem_ind * 2 + 1] else 'Нету'
        right = self._data[elem_ind * 2 + 2] if elem_ind * 2 + 2 < arr_size and self._data[elem_ind * 2 + 2] else 'Нету'

        return f"Первый потомок {elem}: {left}, второй: {right}."


class TreeNode:
    _data = None
    left = None
    right = None


class LinkedListBinTree:

    _top = None

    def __init__(self):
        pass

    def add_element(self, elem):
        pass

    def show_tree(self, elem):
        pass
