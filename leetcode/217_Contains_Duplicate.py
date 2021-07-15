from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = [c[1] for c in list(Counter(nums).items()) if c[1] > 1]
        for i in cnt:
            if i >= 2:
                return True
            else:
                return False
