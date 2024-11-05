def lexicographical_order(s):
    freq = [0] * 52
    for ch in s:
        if 'a' <= ch <= 'z': 
            freq[ord(ch) - ord('a')] += 1
        elif 'A' <= ch <= 'Z': 
            freq[ord(ch) - ord('A') + 26] += 1
    for i in range(26):
        if freq[i] != 0:
            ch = chr(ord('a') + i)
            print(f"{ch} : {freq[i]}")
    for i in range(26, 52):
        if freq[i] != 0:
            ch = chr(ord('A') + (i - 26))
            print(f"{ch} : {freq[i]}")

s = input("Enter a string: ")
lexicographical_order(s)
