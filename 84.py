class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(heights)):
            if heights[i] == 0:
                stack = []
                continue

            if not stack:
                ans = max(ans, heights[i])
                stack.append([heights[i],i])
            elif stack[-1][0] < heights[i]:
                ans = max(ans, (i+1 - stack[-1][1]) * stack[-1][0])
                stack.append([heights[i], i])
            else:
                prev =i
                while stack and stack[-1][0] >= heights[i]:
                    _, prev = stack.pop()
                    ans = max(ans, (i+1 - prev)*heights[i])
                stack.append([heights[i],prev])
            
            print(stack, ans)
        if stack:
            prev = stack[-1][1]
            stack.pop()
            while stack:
                ans = max(ans, (prev +1 - stack[-1][1]) * stack[-1][0])
                stack.pop()
        return ans

        # [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
        #  0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,
