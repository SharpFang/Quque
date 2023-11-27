def first_unique_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

# Приклади
print(first_unique_char("leopard"))  # Виведе 0
print(first_unique_char("loveleopard"))  # Виведе 2
print(first_unique_char("aabb"))  # Виведе -1
