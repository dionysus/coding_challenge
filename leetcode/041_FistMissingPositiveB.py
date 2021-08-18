def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # replace neg or >index with 1s
    hasOne = False
    for i in range(len(nums)):
        if nums[i] == 1:
            hasOne = True
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = 1

    # ensure 1 exists
    if not hasOne:
        return 1

    # accommodate 1:1 mapping
    nums.append(1)

    # flag indices with negation
    for i in range(len(nums)):
        index = abs(nums[i])
        nums[index] = -abs(nums[index])

    # find index missing flag
    i = 2
    while i < len(nums):
        if nums[i] > 0:
            break
        else:
            i += 1

    return i

if __name__ == "__main__":
    nums = [0,2,2,1,1]
    print(firstMissingPositive(nums))