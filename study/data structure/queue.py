class Queue:
    def __init__(self):
        self._data = []
        self._front = 0

    def enqueue(self, item):
        """큐의 뒤에 요소 추가"""
        self._data.append(item)

    def dequeue(self):
        """큐의 앞 요소 제거 및 반환"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        item = self._data[self._front]
        self._front += 1

        # 메모리 정리 (front가 너무 커졌을 때)
        if self._front > len(self._data) // 2:
            self._data = self._data[self._front:]
            self._front = 0

        return item

    def peek(self):
        """큐의 앞 요소 조회 (제거하지 않음)"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[self._front]

    def is_empty(self):
        """큐가 비어 있는지 여부"""
        return self._front == len(self._data)

    def size(self):
        """큐의 현재 요소 개수"""
        return len(self._data) - self._front

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # 1
print(q.peek())     # 2
print(q.size())     # 2
