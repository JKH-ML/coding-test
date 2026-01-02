class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        """스택의 맨 위에 요소 추가"""
        self._data.append(item)

    def pop(self):
        """스택의 맨 위 요소 제거 및 반환"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """스택의 맨 위 요소 조회 (제거하지 않음)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        """스택이 비어 있는지 여부"""
        return len(self._data) == 0

    def size(self):
        """스택의 요소 개수"""
        return len(self._data)


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())   # 3
print(s.peek())  # 2
print(s.size())  # 2
