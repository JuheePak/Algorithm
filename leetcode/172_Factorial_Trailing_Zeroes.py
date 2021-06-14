# Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.
# n이 5의 배수인 경우, trailing Zero의 수가 1씩 늘어남.
# eks 25!의 traling Zeros는 6임. 나눗셈을 적용함. 25/5 -> 5/5 -> 1로, 각 몫인 5+1을 더함.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n //= 5
            res += n
        return res