def replace_char(s, k):
    char_dict = {}
    res = []
    for i, char in enumerate(s):
        if char in char_dict and i - char_dict[char] <= k:
            res.append('-')
        else:
            res.append(char)
        char_dict[char] = i
    return ''.join(res)
s =  input()
k = int(input())
output_str = replace_char(s, k)
print(output_str)
