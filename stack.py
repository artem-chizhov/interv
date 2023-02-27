from copy import deepcopy

class Stack:
    def __init__(self, inputs: list):
        if isinstance(inputs, list):
            self.value = deepcopy(inputs)
        elif isinstance(inputs, str):
            self.value = [char for char in inputs]
        else:
            self.value = [inputs]
        self.sz = len(self.value)

    def size(self) -> int:
        return self.sz

    def is_empty(self):
        return self.sz == 0

    def push(self, element):
        self.value.append(element)
        self.sz += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('стек пустой')
        else:
            ret = self.value.pop()
            self.sz -= 1
        return ret

    def peek(self):
        if self.is_empty():
            raise ValueError('стек пустой')
        else:
            return self.value[-1]

    def __str__(self):
        return f'Stack: {self.value}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.size():
            return self.pop()
        else:
            raise StopIteration

    def __eq__(self, other):
        return set(self.value) == set(other.value)

    def __len__(self):
        return self.size()