class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        while low < high:
            print(low,high)
            median = (low+high) // 2
            if nums[0] < nums[median]: # <- that means we arent still in the rotated part, so move right
                low = median+1
            elif nums[0] > nums[median]: # <- we are in rotated, move left until loop breaks
                if nums[low] > nums[median]:
                    low +=1
                else:
                    high = median
            else:
                break
        if low==high==len(nums):
            return nums[0]
        return nums[low]

