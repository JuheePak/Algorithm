def majorityElement(nums) -> int:
    # TimeError
    # for i in range(len(nums)):
    #     if nums.count(nums[i]) > len(nums)/2:
    #         return nums[i]

    myList = sorted(set(nums))
    for i in myList:
        if nums.count(i) > len(nums) / 2:
            return i