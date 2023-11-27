from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

# Приклад
counter = RecentCounter()
print(counter.ping(1))  # Виведе 1
print(counter.ping(100))  # Виведе 2
print(counter.ping(3001))  # Виведе 3
print(counter.ping(3002))  # Виведе 3
