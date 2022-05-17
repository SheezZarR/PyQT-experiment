
class ArrayBinTree:

    _data = []

    def __init__(self):
        pass

    def resize(self, desired_size):
        """ Resizes an array. """
        for i in range(len(self._data), desired_size):
            self._data.append(None)

    def add_element(self, element):
        """ Adds an element to the tree. """

        for i in range(len(self._data)):
            if self._data[i] is None:
                self._data[i] = element
                return

        self._data.append(element)

    def insert_element(self, pos, element):
        """ Inserts an element with a given position into the tree. """

        parent = pos // 2 - 1 + (pos // 2) % 2

        if parent < len(self._data):
            if self._data[parent] and pos < len(self._data):
                self._data[pos] = element
            else:
                self.resize(desired_size=pos)
                self._data[pos] = element

        raise RuntimeError(f"Невозможно вставить элемент {element} на позицию {pos}. Нет родителя!")

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

    def show_parent(self, elem) -> str:
        if self._data[0] == elem:
            return f"{elem} является корнем"

        elem_ind = self._data.index(elem)
        parent = elem_ind // 2 - 1 + (elem_ind // 2) % 2

        return f"Родитель {elem} элемент {self._data[parent]}"

    def show_children(self, elem) -> str:
        elem_ind = self._data.index(elem)
        arr_size = len(self._data)
        print(self._data)
        left = self._data[elem_ind * 2 + 1] if elem_ind * 2 + 1 < arr_size else 'Нету'
        right = self._data[elem_ind * 2 + 2] if elem_ind * 2 + 2 < arr_size else 'Нету'

        return f"Первый потомок {elem}: {left}, второй: {right}"


class TreeNode:
    _data = None
    left = None
    right = None


class LinkedListBinTree:



def main():
    tree = ArrayBinTree()


main()