# 실전문제 2

"""
첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10,000), K(1 <= K <= 10000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 각각의 자연수는 1 이상 10000이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.

큰수의 법칙에 따라 더해진 답을 출력한다.
예)
5 8 3
2 4 5 4 6

답)46
"""
# n은 배열의 크기, m은 숫자가 더해지는 횟수, k는 숫자가 연속해서 나올 수 있는 횟수
n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data = sorted(data) # 오름차순 정렬

"""
sorted vs sort()
sorted(data) --> 원본은 유지되고 새 리스트를 만든다. 정렬값을 반환.
data.sort() --> 반환값은 None, 기존 리스트에 반영된다.
"""

first = data[n-1]  # 제일 큰 수
second = data[n-2]  # 두번째로 큰 수

""" 단순하게 푸는 예시
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1  # 숫자가 더해지는 횟수를 한번씩 감소

    if m == 0:
        break
    result += second  # 두번째로 작은 수는 한번만 더해주면 되니까 for 반복문을 쓸 필요가 없다
    m -= 1

print(result)
"""

cnt = int(m/(k+1)) * k
cnt += (m % (k+1))

result = 0
result += (cnt) * first
result += (m-cnt)*second

print(first, second)
print(result)

