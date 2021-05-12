#result = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#print(result[2][1])

def generate(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        tmp = generate(numRows - 1)
        # 더해서 아래로 내려 가야 하는 리스트
        mylist = tmp[-1]
        sum_list = [mylist[i]+mylist[i+1] for i in range(len(mylist)-1)]
        #for i in range(len(mylist)-1): #왜이건안됨?ㅠ
        #    sum_list = [mylist[i] + mylist[i+1]]
        sum_list.insert(0, 1) 
        sum_list.append(1) # 무조건 1로 끝남
        tmp.append(sum_list)
    return tmp

print(generate(4))