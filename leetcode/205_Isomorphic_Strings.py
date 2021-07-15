class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(set(zip(s, t)))
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    