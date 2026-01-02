from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """큐의 뒤에 요소 추가"""
        self._data.append(item)

    def dequeue(self):
        """큐의 앞 요소 제거 및 반환"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        """큐의 앞 요소 조회 (제거하지 않음)"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]

    def is_empty(self):
        """큐가 비어 있는지 여부"""
        return len(self._data) == 0

    def size(self):
        """큐의 요소 개수"""
        return len(self._data)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10
print(q.peek())     # 20
print(q.size())     # 2
