class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 리스트 끝에 노드 추가
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    # 리스트 출력
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes) + " -> None")
        
        # 특정 값을 가진 노드 삭제
    def delete(self, key):
        current = self.head

        # 1. 머리 노드(head)가 삭제할 대상인 경우
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # 2. 삭제할 노드 찾기
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # 찾는 값이 없는 경우
        if not current:
            return

        # 연결 끊기
        prev.next = current.next
        current = None

    # 특정 값 검색
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
sll = LinkedList()
sll.append(10)
sll.append(20)
sll.append(30)

sll.display()  # 출력: 10 -> 20 -> 30 -> None

print(sll.search(20))  # 출력: True

sll.delete(20)
sll.display()  # 출력: 10 -> 30 -> None