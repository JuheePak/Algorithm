# 전제 조건: 정렬이 되어 있어야 한다.
# 개효율적임

def binarySearch(ary, data):
    start = 0
    end = len(ary)-1

    while start <= end:
        mid = (start+end) // 2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1 #못찾음


# 메인 코드부
dataAry = [1, 2, 3, 5, 9, 11, 55, 77, 88, 128, 444, 9999] # 9찾기
print(binarySearch(dataAry, 9))
print(binarySearch(dataAry, 1234))