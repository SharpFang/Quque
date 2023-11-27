from collections import deque

def constrained_subset_sum(nums, k):
    dp = [0] * len(nums)
    result = float('-inf')
    dq = deque()

    for i, num in enumerate(nums):
        while dq and i - dq[0] > k:
            dq.popleft()
        dp[i] = max(num, num + (dp[dq[0]] if dq else 0))
        result = max(result, dp[i])

        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        dq.append(i)

    return result

# Приклади
print(constrained_subset_sum([10,2,-10,5,20], 2))  # Виведе 37
print(constrained_subset_sum([-1,-2,-3], 1))  # Виведе -1
print(constrained_subset_sum([10,-2,-10,-5,20], 2))  # Виведе 23
