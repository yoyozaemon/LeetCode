class Solution:
    def __init__(self):
        self.ans = 0
        self.mx = float('inf')

    def Solve(self, nums, x, i, T):
        n = len(nums)
        L = i
        R = n - 1
        while L < R:
            val = nums[x] + nums[L] + nums[R]
            if abs(T - val) < self.mx:
                self.ans = val
                self.mx = abs(T - val)
            elif val > T:
                R -= 1
            else:
                L += 1

    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i == 0 or nums[i - 1] != nums[i]:
                self.Solve(nums, i, i + 1, target)
        return self.ans
