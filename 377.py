class Solution:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        ans = 0
        n = len(nums)
        def f(i, target):
            nonlocal ans
            if target - nums[i] < 0:
                return
            elif target - nums[i] == 0:
                ans +=1
                return
            
            for j in range(n):
                f(j, target - nums[i])
            
        for i in range(n):
            f(i, t)
        return ans
