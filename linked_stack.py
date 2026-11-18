
# linked_stack.py

from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0

    # Menambahkan data ke stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    # Mengambil data paling atas
    def pop(self):
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    # Melihat data paling atas
    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

    # Memeriksa apakah stack kosong
    def is_empty(self):
        return self.top is None

    # Menghitung jumlah data
    def size(self):
        return self._size

    # Menghapus seluruh isi stack
    def clear(self):
        self.top = None
        self._size = 0

    # Mengambil seluruh isi stack
    def get_all(self):
        result = []
        current = self.top

        while current is not None:
            result.append(current.data)
            current = current.next

        return result

    # Menampilkan isi stack
    def display(self):
        if self.is_empty():
            print("Stack kosong")
            return

        print("Isi Stack (Top ke Bottom):")
        current = self.top

        while current is not None:
            print(current.data)
            current = current.next
