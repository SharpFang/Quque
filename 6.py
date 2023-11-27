from collections import deque

def max_sliding_window(nums, k):
    result = []
    window = deque()

    for i, num in enumerate(nums):
        while window and window[0] < i - k + 1:
            window.popleft()
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Приклади
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Виведе [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))  # Виведе [1]
