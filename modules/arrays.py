"""Implementation of an array: via bidirectional lists and via built-in array."""
from __future__ import annotations


class Node:

    _data = 0
    _next = None

    def __init__(self, data: int):
        self._data = data

    def __str__(self):
        return f"{self._data}"

    @classmethod
    def init_with_node(cls, node: Node, data: int) -> Node:
        cls._next = node
        cls._data = data
        return cls

    def get_next_node(self) -> Node:
        return self._next

    def set_next_node(self, node: any) -> None:
        self._next = node


class NodeArray:
    """
    Node-base array
    """
    _head = None
    _logic_size = 0

    def __init__(self):
        pass

    def __iter__(self) -> Node:
        start = self._head
        while start:
            yield start
            start = start.get_next_node()

    def __str__(self):
        dt = []
        start = self._head

        while start:
            dt.append(start.__str__())
            start = start.get_next_node()

        return f"{dt}"

    def __getitem__(self, item_id: int):

        if item_id >= self._logic_size or item_id < 0:
            raise IndexError("Incorrect index!")

        counter = 0
        result = self._head

        while counter != item_id:
            result = result.get_next_node()
            counter += 1

        return result

    def add(self, node: Node) -> None:
        if self._head:
            start = self._head

            while start.get_next_node():
                start = start.get_next_node()

            start.set_next_node(node)

        else:
            self._head = node

        self._logic_size += 1

    def insert_at(self, item_pos: int, node: Node) -> None:
        if item_pos >= self._logic_size or item_pos < 0:
            raise IndexError("Incorrect index!")

        start = self._head
        tmp = None

        if item_pos == 0:
            tmp = self._head
            self._head = node
            self._head.set_next_node(tmp)
            self._logic_size += 1

        else:
            for i in range(item_pos - 1):
                start = start.get_next_node()

            tmp = start
            start = start.get_next_node()
            tmp.set_next_node(node)
            node.set_next_node(start)

    def remove(self) -> None:
        start = self._head

        for i in range(self._logic_size - 1):
            start = start.get_next_node()

        start.set_next_node(None)

    def remove_at(self, pos: int) -> None:
        if pos == 0:
            self._head = self._head.get_next_node()

        else:
            start = self._head

            for i in range(self.pos - 1):


    def is_empty(self) -> bool:
        return True if self._logic_size == 0 else False


class CommonArray:
    """
    Array interface implementation.
    """

    _data = []
    _logic_size = 0

    def __init__(self):
        pass

    def __iter__(self):
        for i in self._data:
            yield i

    def __getattr__(self, item_id):
        if item_id >= self._logic_size or item_id < 0:
            raise IndexError("Incorrect index!")

        return self._data[item_id]

    def __str__(self):
        return f"{self._data}"

    def add(self, item: int) -> None:
        self._data.append(item)
        self._logic_size += 1

    def insert_at(self, item_pos: int, item: int) -> None:
        if item_pos >= self._logic_size or item_pos < 0:
            raise IndexError("Incorrect index!")

        self._data.insert(item_pos, item)

    def remove(self) -> None:
        if self.is_empty():
            raise RuntimeError("Container is empty!")

        self._logic_size -= 1
        self._data.pop()

    def remove_at(self, item_pos: int) -> None:
        if item_pos >= self._logic_size or item_pos < 0:
            raise IndexError("Incorrect index!")

        if self.is_empty():
            raise RuntimeError("Container is empty!")

        self._data.remove(self._data[item_pos])

    def is_empty(self) -> bool:
        return True if self._logic_size == 0 else False
