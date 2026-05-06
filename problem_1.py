def max_cyclic_substring_sum(s):
    n = len(s)
    s2 = s + s  
    char_set = set()

    left = 0
    current_sum = 0
    max_sum = 0

    for right in range(len(s2)):
       
        val = ord(s2[right]) - ord('a') + 1

       
        while s2[right] in char_set:
            remove_val = ord(s2[left]) - ord('a') + 1
            current_sum -= remove_val
            char_set.remove(s2[left])
            left += 1

        char_set.add(s2[right])
        current_sum += val

       
        if right - left + 1 > n:
            remove_val = ord(s2[left]) - ord('a') + 1
            current_sum -= remove_val
            char_set.remove(s2[left])
            left += 1

        max_sum = max(max_sum, current_sum)

    return max_sum
s = input().strip()
print(max_cyclic_substring_sum(s))
