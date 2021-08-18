def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # return 1 if not have 1

    hasOne = False
    for i in range(len(nums)):
        if nums[i] == 1:
            hasOne = True
            break
    if not hasOne:
        return 1
    
    # we now know that 1 already exists

    # set all negatives to 1 as a placeholder
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i] = 1

    # accommodate 1:1 mapping
    nums.append(1)
    
    i = 0
    while i < len(nums) - 1:
        currNum = nums[i]

        # originally negative number
        if currNum == 1 or currNum == -1:
            pass
        else: 
            # positive number (neg if flagged) to check
            index = abs(currNum)
            if index < len(nums):
                # flag index by making negative
                if nums[index] > 0:
                    nums[index] = -nums[index]
        i += 1

    # we know 1 exists, start at 2
    # return first unflagged index
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