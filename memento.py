# memento_linked_stack.py — Implementasi Inti Memento & Linked Stack (LIFO)
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class EmptyStackError(Exception):
    """Pengecualian ketika operasi pop/peek dilakukan pada stack kosong."""

@dataclass(frozen=True, slots=True)
class EditorMemento:
    """
    Objek Memento (Immutable) yang menyimpan snapshot status internal TextEditor.
    Atribut bersifat read-only sehingga integritas riwayat tidak dapat diubah pihak luar.
    """
    content: str
    cursor_position: int
    action_label: str
    timestamp: str

class _StackNode(Generic[T]):
    """Simpul tunggal pada Linked Stack dengan optimasi memori __slots__."""
    __slots__ = ("data", "next")

    def __init__(self, data: T, next_node: Optional["_StackNode[T]"] = None) -> None:
        self.data: T = data
        self.next: Optional[_StackNode[T]] = next_node

class LinkedStack(Generic[T]):
    """
    Implementasi struktur data Stack (LIFO) berbasis Singly Linked List.
    Menjamin kompleksitas O(1) untuk operasi push, pop, peek, dan clear.
    """
    def __init__(self, max_capacity: Optional[int] = None) -> None:
        if max_capacity is not None and max_capacity <= 0:
            raise ValueError("max_capacity harus bernilai > 0")
        self._top: Optional[_StackNode[T]] = None
        self._size: int = 0
        self._max_capacity: Optional[int] = max_capacity

    @property
    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._top is None

    def push(self, item: T) -> None:
        """Menyisipkan elemen ke puncak stack dalam waktu konstan O(1)."""
        new_node = _StackNode(data=item, next_node=self._top)
        self._top = new_node
        self._size += 1

        # Pemangkasan simpul terbawah jika melebihi batas kapasitas riwayat
        if self._max_capacity is not None and self._size > self._max_capacity:
            self._evict_oldest()

    def pop(self) -> T:
        """Mengambil dan menghapus elemen puncak stack dalam waktu konstan O(1)."""
        if self._top is None:
            raise EmptyStackError("Tidak dapat pop: LinkedStack dalam keadaan kosong.")
        removed_node = self._top
        self._top = removed_node.next
        # Putuskan referensi pointer agar Garbage Collector segera membebaskan memori
        removed_node.next = None
        self._size -= 1
        return removed_node.data

    def peek(self) -> T:
        """Melihat elemen puncak tanpa menghapusnya dari stack (O(1))."""
        if self._top is None:
            raise EmptyStackError("LinkedStack kosong.")
        return self._top.data

    def clear(self) -> None:
        """Mengosongkan seluruh simpul pada stack secara aman."""
        current = self._top
        while current is not None:
            nxt = current.next
            current.next = None
            current = nxt
        self._top = None
        self._size = 0

    def _evict_oldest(self) -> None:
        """Memutus simpul paling dasar saat kapasitas maksimum terlampaui."""
        if self._top is None or self._top.next is None:
            return
        curr = self._top
        while curr.next is not None and curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self._size -= 1