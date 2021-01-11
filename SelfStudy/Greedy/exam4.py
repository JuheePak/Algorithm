"""
곱하기 혹은 더하기
0부터 9로만 이루어진 문자열 S가 있을 떄, x 혹은 + 연산자만 넣어 만들 수 있는 가장 큰 수를 구할거임
e.g. 02984가 입력되면 만들 수 있는 가장 큰 수는 ((((0+2)*9)*8)*4)=576입니다.
"""

data = input()

result = int(data[0])
for i in range(1, len(data)):
    if int(data[i]) <= 1 or result <= 1: # data[i]가 0이거나 1인 경우는 더해주는 것이 곱셈보다 값이 크다.
        result += int(data[i])
    else:
        result *= int(data[i])

print(result)

