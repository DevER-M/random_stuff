from typing import Sequence, Any
import time


def measure(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}, {((end-start)*1000):.2f}ms")
        return result

    return wrap


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(
            f"<{self.value}, {type(self.value)} @{hex(id(self))} -> {hex(id(self.next))}>"
        )


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return " -> ".join(str(e) for e in self)

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr.value
            ptr = ptr.next
        return

    def __iter_node__(self):
        ptr = self.head
        while ptr:
            yield ptr
            ptr = ptr.next

    def __len__(self):
        return sum(1 for _ in self)

    def __contains__(self, value):
        return any(node == value for node in self)

    def __getitem__(self, depth: slice | int):
        if depth < 0:
            raise IndexError("Index Out Of Range")
        ptr = self.head
        while depth > 0:
            ptr = ptr.next
            depth -= 1
            if ptr is None:
                raise IndexError("Index Out Of Range")
        return ptr.value

    def __add__(self, operand):
        if not isinstance(operand, LinkedList):
            raise TypeError("Operand Not LinkedList")
        if self.head is None:
            return operand
        elif operand.head is None:
            return self

        head = self.head
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = operand.head
        return LinkedList(head)

    @staticmethod
    def from_seq(_seq: Sequence):
        if not _seq:
            return LinkedList(Node(_seq))
        _head = Node(_seq[0])
        ptr = _head
        for value in _seq[1:]:
            ptr.next = Node(value)
            ptr = ptr.next
        return LinkedList(_head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        elif self.head.value:
            self.head.value = value
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(value)

    def append_seq(self, _seq: Sequence):
        if self.head is None:
            self.head = Node(_seq[0])
            ptr = self.head
            for e in _seq[1:]:
                ptr.next = Node(e)
                ptr = ptr.next
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        for e in _seq:
            ptr.next = Node(e)
            ptr = ptr.next

    def stack(self, value):
        self.head = Node(value, self.head)

    def stack_seq(self, _seq: Sequence):
        if self.head is None:
            self.head = Node(_seq[0])
            for e in _seq[1:]:
                self.stack(e)
            return
        for e in _seq:
            self.stack(e)

    def pop_head(self):
        if self.head:
            self.head = self.head.next

    def pop_tail(self):
        if not self.head:
            return
        if self.head.next is None:
            self.head = None
            return
        ptr = self.head
        while ptr.next and ptr.next.next:
            ptr = ptr.next
        ptr.next = None

    def index(self, value) -> Any | None:
        for e in enumerate(self):
            if e[1] == value:
                return e[0]
        return

    def insert(self, value, depth: int):
        ptr = self.head
        while depth != 1:  # depth used as counter, stops one before the needed depth
            ptr = ptr.next
            depth -= 1
            if ptr is None:
                raise IndexError("Index Out Of Range")
        ptr.next = Node(value, ptr.next)

    def insert_seq(self, _seq: Sequence, depth: int):
        ptr = self.head
        sequence_head = Node(_seq[0])
        seq_ptr = sequence_head

        for e in _seq[1:]:
            seq_ptr.next = Node(e)
            seq_ptr = seq_ptr.next
        # now seq_ptr points to the end of sequence and sequence_head is head

        while depth != 1:
            ptr = ptr.next
            depth -= 1
            if ptr is None:
                raise IndexError("Index Out Of Range")

        seq_ptr.next = ptr.next  # link next value of sequence to ptr
        ptr.next = sequence_head  # link next value of ptr to head of sequence

    def reverse(self):
        prev = None
        ptr = self.head
        while ptr is not None:
            """v<<<< prev  <<<<<<<<<^
            v>>>> ptr >> ptr.next^
            """
            ptr.next, prev, ptr = prev, ptr, ptr.next
        self.head = prev

    def clear(self):
        self.head = None

    def pop(self, depth):
        ptr = self.head
        while depth != 1:
            ptr = ptr.next
            depth -= 1
            if ptr is None:
                raise IndexError("Index Out Of Range")
        retval = ptr.next
        ptr.next = ptr.next.next
        return retval

    def remove(self, value):
        ptr = self.head
        while value != ptr.next.value:
            ptr = ptr.next
            if ptr is None:
                raise ValueError("Value Not Found")
        retval = ptr.next
        ptr.next = ptr.next.next
        return retval


def test():
    x = LinkedList.from_seq("abc")
    print(
        f"""len {len(x)}
({x})"""
    )
    x.insert("d", 1)
    print(x)
    x.insert_seq("efg", len(x))
    print(x)
    x.pop_head()
    print(x, len(x))
    x.reverse()
    print(x)
    print()

    y = LinkedList.from_seq("xyz")
    print(x + y)


def test2():
    x = LinkedList.from_seq(range(10))
    print(x.remove(5))
    print(x)


if __name__ == "__main__":
    test2()
