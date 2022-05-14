class Node:
    value: object = None

    def __repr__(self):
        return str(self.value)



class LinkedList:
    def __init__(self):
        self._length: int = 0
        self.head: "Node" = None

    def length(self) -> int:
        return self._length

    def __len__(self):
        return self.length()


class PriorNode(Node):
    nnext: "Node"

    def __init__(self, value, nnext=None, priority=None):
        self.value = value
        self.nnext = nnext
        self.priority = priority


class PriorQueue(LinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, value, priority):
        self._length += 1

        if not self.head:
            self.head = PriorNode(value, None, priority)
            return

        if self.head.priority > priority:
            old_head = self.head
            self.head = PriorNode(value, None, priority)
            self.head.nnext = old_head

        else:
            node_pointer = self.head
            while node_pointer.nnext and node_pointer.priority <= priority:
                node_pointer = node_pointer.nnext
            old_pointer = node_pointer.nnext
            node_pointer.nnext = PriorNode(value, None, priority)
            node_pointer.nnext.nnext = old_pointer

    def dequeue(self) -> object:
        node_pointer = self.head
        if len(self) == 0:
            raise IndexError('Список пуст!')
        elif len(self) == 1:
            self._length -= 1
            self.head = None
            return
        elif len(self) == 2:
            self._length -= 1
            self.head.nnext = None
            return
        else:
            for i in range(1, len(self)):
                self._length -= 1
                if i == len(self)-1:
                    node_pointer.nnext = None
                node_pointer = node_pointer.nnext

    def check(self) -> object:
        node_pointer = self.head
        while node_pointer.nnext:
            node_pointer = node_pointer.nnext
        return node_pointer.value