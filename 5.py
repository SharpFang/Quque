def moves_to_stamp(stamp, target):
    m, n = len(stamp), len(target)
    stamped = ['?'] * n
    result = []

    def can_stamp(start):
        changed = False
        for i in range(m):
            if stamped[start + i] == '?' or stamped[start + i] == stamp[i]:
                changed = True
                stamped[start + i] = '?'
            else:
                return False, changed
        return True, changed

    def backtrack(start):
        changed = False
        for i in range(n - m + 1):
            can, change = can_stamp(i)
            if can:
                changed = True
                result.append(i)
                if backtrack(i + m):
                    return True
                result.pop()
                for j in range(m):
                    if stamped[i + j] == '?':
                        stamped[i + j] = target[i + j]
        return changed

    if not backtrack(0):
        return []
    return result[::-1]

# Приклади
print(moves_to_stamp("abc", "ababc"))  # Виведе [0, 2]
print(moves_to_stamp("abca", "aabcaca"))  # Виведе [3, 0, 1]
