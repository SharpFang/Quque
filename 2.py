from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]

    def empty(self):
        return not bool(self.queue1)

# Приклад
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  # Виведе 2
print(stack.pop())  # Виведе 2
print(stack.empty())  # Виведе False
