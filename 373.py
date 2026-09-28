class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        m = len(nums1)
        n = len(nums2)
        heap = []
        for i in range(m):
            heap.append((nums1[i] + nums2[0], (i,0)))
        
        heapq.heapify(heap)
        ans = []
        while heap and len(ans) != k:
            _, ij = heapq.heappop(heap)
            i,j = ij
            ans.append([nums1[i],nums2[j]])
            if j+1 < n:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], (i, j+1)))
            
        return ans

