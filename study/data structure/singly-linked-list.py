class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """리스트의 끝에 노드 추가"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """리스트의 앞에 노드 추가"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """특정 값을 가진 첫 번째 노드 삭제"""
        current = self.head

        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return  # 값이 없는 경우

        prev.next = current.next

    def find(self, data):
        """값이 존재하는지 탐색"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """리스트 출력"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)

ll.display()      # 0 -> 1 -> 2 -> 3
print(ll.find(2)) # True

ll.delete(2)
ll.display()      # 0 -> 1 -> 3
