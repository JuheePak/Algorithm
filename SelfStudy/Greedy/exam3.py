# 실전문제 3 - 숫자 카드 게임

"""
N행, M열의 숫자카드가 놓여있다. M이 공백을 기준으로 하여 각 자연수로 주어진다
N은 0보다 큰 자연수, M은 100 이하의 자연수이다.
둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000dlgkdml wkdustndlek.
첫째 줄에 게임에 맞게 선택한 카드에 적힌 숫자를 출력한다.
* 단 카드게임의 룰을 지켜라.
"""

n, m = map(int, input().split()) # 공백으로 쪼갠 정수 입력 받기

result = 0
"""
for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    result = max(result, min_data)

print(result)
"""

for i in range(n):
    data = list(map(int, input().split()))
    min_data = 10001 # 겁나 큰 값으로 설정

    for k in data:
        min_data = min(min_data, k)
    result = max(result, min_data)

print(result)
