def string_compression_3(word: str) -> str:
    comp = ""
    prev = word[0]
    count = 1

    for i in range(1, len(word)):
        if prev != word[i]:
            comp = comp + str(count) + prev
            prev = word[i]
            count = 1
        else:
            if count == 9:
                comp = comp + str(count) + prev
                count = 1
            else:
                count = count + 1
    comp = comp + str(count) + prev

    return comp

print(string_compression_3("abcde"))