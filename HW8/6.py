def count_chars(s):
    char_count = {}
    for c in s:
        char_count[char] = char_count.get(c, 0) + 1
    return char_count
