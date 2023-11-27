from collections import deque

class MyCircularDeque:
    def __init__(self, k):
        self.capacity = k
        self.deque = deque()

    def insertFront(self, value):
        if len(self.deque) < self.capacity:
            self.deque.appendleft(value)
            return True
        return False

    def insertLast(self, value):
        if len(self.deque) < self.capacity:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self):
        if self.deque:
            self.deque.popleft()
            return True
        return False

    def deleteLast(self):
        if self.deque:
            self.deque.pop()
            return True
        return False

    def getFront(self):
        return self.deque[0] if self.deque else -1

    def getRear(self):
        return self.deque[-1] if self.deque else -1

    def isEmpty(self):
        return len(self.deque) == 0

    def isFull(self):
        return len(self.deque) == self.capacity

# Приклад
circularDeque = MyCircularDeque(3)
print(circularDeque.insertLast(1))  # Виведе True
print(circularDeque.insertLast(2))  # Виведе True
print(circularDeque.insertFront(3))  # Виведе True
print(circularDeque.insertFront(4))  # Виведе False
print(circularDeque.getRear())  # Виведе 2
print(circularDeque.isFull())  # Виведе True
print(circularDeque.deleteLast())  # Виведе True
print(circularDeque.insertFront(4))  # Виведе True
print(circularDeque.getFront())  # Виведе 4
