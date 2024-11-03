def roatateString(s, goal):
    for i in range(len(s)):
        new = s[i+1:] + s[0:i+1]
        if new == goal:
            return True
    return False

print(roatateString("abcde", "cdeab"))

def rotateString2(s, goal):
    if len(s) != len(goal):
        return False
    return goal in s+s

print(rotateString2("abcde", "cdeab"))