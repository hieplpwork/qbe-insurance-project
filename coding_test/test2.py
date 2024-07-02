def compress_string(s):
    if not s:
        return ""
    
    res = []
    current_c = s[0]
    count = 1
    for c in s[1:]:
        if c == current_c:
            count += 1
        else:
            res.append(current_c + str(count))
            count = 1
            current_c = c

    res.append(current_c + str(count))
    return "".join(res)

input = "aaaaaabbbcccccdd"
print(compress_string(input))