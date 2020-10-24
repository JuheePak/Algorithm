### `Divide and Conquer(분할정복법)`



### 재귀함수를 디자인 하기 위한 세가지 단계

1. 함수의 정의를 명확히 한다.
2. **기저 조건**에서 함수가 제대로 작동하게 작성한다.
3. 함수가 제대로 동작한다고 가정하고 함수를 완성한다.



### 가장 가까운 값 찾기

> 오름차순으로 정렬된 n개의 숫자가 주어지고, 정수 m*m*이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 출력하는 프로그램을 작성하시오. 만약 가장 가까운 숫자가 2개 이상이라면, 그 중 가장 작은 숫자를 출력한다.
>
> **만약 1 4 6 7 10 14 16 과 8을 입력하면 7을 출력한다.**

``` python
import sys

def getNearestInternal(data, m):
    """
    m과 가장 가까운 값 후보인 두 값을 리턴하는 함수
    """    
    if len(data) == 1:
        return (data[0], data[0])
    elif len(data) == 2:
        return (data[0], data[1])
        
    mid = len(data) // 2
    
    if data[mid] <= m:
        return getNearestInternal(data[mid:], m)
    else:
        return getNearestInternal(data[:mid+1], m)

def getNearest(data, m) :
    '''
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    '''
    
    value = getNearestInternal(data, m)
    
    """
    value[0]: m 이하이면서 가장 가까운 값
    value[1]: m 이상이면서 가장 가까운 값
    """
    
    if m - value[0] <= value[1] -m:
        return value[0]
    else:
        return value[1]
    

def main():
    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

if __name__ == "__main__":
    main()
```



### 거듭제곱 구하기

>본 연습문제에서는 m^n을 구하는 프로그램을 작성합니다.
>
>입력으로는 m, n이 차례대로 입력됩니다.
>
>**만약 getPower 함수의 반환 값이 1,000,000,007 보다 클 경우, 반환 값을 1,000,000,007로 나눈 나머지 값을 반환하세요.**

``` python
LIMIT_NUMBER = 1000000007

def getPower(m, n):
    '''
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''    
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = getPower(m, n//2)
        return (temp*temp) % LIMIT_NUMBER
    else:
        temp = getPower(m, (n-1)//2)
        return (temp*temp*m) % LIMIT_NUMBER       

def main():
    myList = [int(v) for v in input().split()]
    print(getPower(myList[0], myList[1]))

if __name__ == "__main__":
    main()

```



### `분할정복법`

- 문제를 소문제로 **분할**
- 각각의 **소문제**를 해결
- 소문제의 해결 결과를 이용해 **전체 문제를 해결**
- 단점: 작은 문제로 분할하는 것이 어렵다.



### 합병 정렬 구현

> *n*개의 숫자를 합병정렬을 이용하여 정렬하는 프로그램을 작성하세요.

``` python
import sys
import math

def mergeSort(data) :
    '''
    n개의 숫자를 합병정렬을 이용하여 정렬한 결과를 list로 반환하는 함수를 작성하세요.
    '''
    
    if len(data) == 1:
        return data
    mid = len(data) // 2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    result = []
    
    leftPtr = 0
    rightPtr = 0
    
    while leftPtr < len(left) or rightPtr < len(right):
        leftValue = left[leftPtr] if leftPtr < len(left) else math.inf
        rightValue = right[rightPtr] if rightPtr < len(right) else math.inf
        
        if leftValue < rightValue :
            result.append(leftValue)
            leftPtr += 1
        else:
            result.append(rightValue)
            rightPtr += 1
            
    return result

def main():
    data = [int(x) for x in input().split()]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()

```



### 연속 부분 최대합(Medium)

> *n*개의 숫자가 주어질 때, 연속 부분을 선택하여 그 합을 최대화 하는 프로그램을 작성하시오. 예를 들어, 다음과 같이 8개의 숫자가 있다고 하자.
>
> 1 2 -4 5 3 -2 9 -10
>
> 이 때, 연속 부분이란 연속하여 숫자를 선택하는 것을 말한다. 가능한 연속 부분으로써 [1, 2, -4], [5, 3, -2, 9], [9, -10] 등이 있을 수 있다. 이 연속 부분들 중에서 가장 합이 큰 연속 부분은 [5, 3, -2, 9] 이며, 이보다 더 합을 크게 할 수는 없다. 따라서 연속 부분 최대합은 5+3+(-2)+9 = 15 이다.

``` python
import sys

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    
    n = len(data)
    if n == 1:
        return data[0]
    """
    왼쪽, 오른쪽, 양쪽 연속부분의 최대합을 구하고 비교해서 가장 큰 값을 리턴한다.
    """
    mid = n//2
    left = getSubsum(data[:mid])
    right = getSubsum(data[mid:])
    
    Sum = 0
    
    leftSum = 0
    rightSum = 0
    
    for i in range(mid-1, -1, -1):
        Sum += data[i]
        leftSum = max(Sum, leftSum)
    
    Sum = 0
    
    for i in range(mid, n):
        Sum += data[i]
        rightSum = max(Sum, rightSum)
        
    return max([left, right, leftSum+rightSum])
        

def main():
    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
```

