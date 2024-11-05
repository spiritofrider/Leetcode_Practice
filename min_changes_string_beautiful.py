def min_changes(s: str) -> int:
    count, chg = 0,0
    while count < len(s):
        if s[count] != s[count+1]:
            chg = chg + 1
        count = count+2
    return chg

print(min_changes("1001"))