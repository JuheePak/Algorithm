"""
만들 수 없는 금액
N개의 동전 중 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 구현하라
e.g. N이 5이고 각 3, 2, 1, 1, 9원 화폐단위 동전이라 할 때, 만들 수 없는 양의 정수 금액 중
최솟값은 8원이다.

"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)



"""
나왜이거안풀리냐 미치겟네ㅠㅠㅠㅠ
젠장할~~~~~~ 띄ㅇ어쓰기~~~~~ 꼭 잘합시다~~~~~~~~~
"""