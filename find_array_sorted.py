def canSortArray(nums: list[int]) -> bool:
    currMax, currMin, prevMax = 0, 0, 0
    prevBit = -1

    for x in nums:
        b = x.bit_count()
        if prevBit != b:
            if currMin < prevMax:
                return False
            prevMax = currMax
            currMin, currMax = x, x
            prevBit = b
        else:
            currMin = min(currMin, x)
            currMax = max(currMax, x)
    return currMin >= prevMax

print(canSortArray([3,16,8,4,2]))
print(canSortArray([8,4,2,30,15]))