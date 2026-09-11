class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        inflection_index = n-k
        left_half = inflection_index
        right_half = n - inflection_index
        for i in range(min(left_half,right_half)):
            print(i, i+inflection_index)
            nums[i],nums[i+inflection_index] = nums[i+inflection_index], nums[i]
        if left_half > right_half:
            num =nums.pop(inflection_index-1)
            nums.append(num)
        elif left_half < right_half:
            num = nums.pop()
            nums.insert(inflection_index, num)
        
        return 
