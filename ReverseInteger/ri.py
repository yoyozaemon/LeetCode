class Solution:
    def reverse(self, x: int) -> int:
        if x != 0:
            sign = int(x / abs(x))
            m = int(str(abs(x))[::-1])
        else:
            sign = 0
            m = 0
        if m <= 2**31:
            return sign * m
        else: 
            return 0
