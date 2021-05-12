def getRow(rowIndex):
    if rowIndex == 0:
        return []
    elif rowIndex == 1:
        return [1]
    elif rowIndex == 2:
        return [1, 1]
    else:
        tmp = getRow(rowIndex - 1)
        sum_list = [tmp[i]+tmp[i+1] for i in range(len(tmp)-1)]
        sum_list.insert(0, 1)
        sum_list.append(1) # 무조건 1로 끝남
    return sum_list

print(getRow(5))