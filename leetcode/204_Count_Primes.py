class Solution:
    def countPrimes(self, n: int) -> int:
        tmp = []
        for i in range(2, n+1):
            if n % i == 0:
                while n % i == 0:
                    tmp.append(n)
                    n = n / i
                return len(tmp)

## 수정해야 함