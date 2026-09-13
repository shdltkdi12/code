class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        left = 0
        ans = []
        for right in range(len(nums)):
            if right - left < k:
                if not queue:
                    queue.append(right)
                else:
                    while queue and nums[queue[-1]] < nums[right]:
                        queue.pop()
                    queue.append(right)
            else:
                ans.append(nums[queue[0]])
                if queue[0] <= right-k:
                    queue.popleft()
                if not queue:
                    queue.append(right)
                else:
                    while queue and nums[queue[-1]] < nums[right]:
                        queue.pop()
                    queue.append(right)
                left +=1
        if queue[0] < left:
            queue.popleft()
        ans.append(nums[queue[0]])
        return ans

