def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            cnt = i
    return cnt

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))