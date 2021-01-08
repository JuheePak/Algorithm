# greedy, 탐욕법 1

# 거스름돈을 1260원 준다고 할 때, 화폐단위는 500, 100, 50, 10원이다.

n = 1260
cnt = 0

coin = [500, 100, 50, 10]

for c in coin:
    cnt += n // c #거슬러 줄 동전의 개수
    n %= c

print(cnt)



