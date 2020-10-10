import random

# 함수 선언부
def quickSort(ary):
    n = len(ary)
    if n <= 1:
        return ary
    pivot = ary[len(ary)//2] # 기준 값을 중간으로
    leftAry=[]
    rightAry=[]
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

# 전역 변수부
ary = [random.randint(100, 999) for _ in range(20)]

# 메인 코드부
print('정렬 전 --> ', ary)
ary = quickSort(ary)
print('정렬 후 --> ', ary)