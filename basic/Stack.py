class Stack:
    def __init__(self):
        self.items = [] # 데이터 저장을 위한 리스트 준비

    # 시간 복잡도 O(1)
    def push(self, val):
        self.items.append(val)

    # 시간 복잡도 O(1)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stck is empty") # pop 할 아이템이 없으면 indexError발생

    # 시간 복잡도 O(1)
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    # 시간 복잡도 O(1)
    def __len__(self):
        # len() 호출하면 stack의 item 수 반환
        return len(self.items)