def twoSum(numbers, target):
    for i in numbers:
        chaVal = target - i
        tmp = []
        if chaVal >= 0 and chaVal in numbers:
            if numbers.index(i) == numbers.index(chaVal):
                mynum = numbers.index(chaVal) + 1
                tmp.append(numbers.index(chaVal) + 1)
                tmp.append(mynum + 1)
            if numbers.index(i) != numbers.index(chaVal):
                tmp.append(numbers.index(i) + 1)
                tmp.append(numbers.index(chaVal) + 1)
            return tmp
