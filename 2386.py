class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        heap = []
        maxi = 0
        n=  len(nums)
        for num in nums:
            if num >0:
                maxi += num
        
        sorted_nums = sorted([abs(nums[i]) for i in range(n)])

        heap.append((-1*maxi, -1))
        heapq.heapify(heap)
        counter = 1
        while heap:
            val, idx = heapq.heappop(heap)
            val *= -1
            if counter == k:
                # print('dbg', val, counter)
                return val
            # print('dbg1',len(heap), 'counter', counter, 'val', val)       
            counter +=1
            if idx+1 < n:
                #take
                # print('dbg2',val, sorted_nums[idx+1])
                heapq.heappush(heap,  (-1*val+sorted_nums[idx+1], idx +1))
                # not take
            if idx+2 <n:
                
                # print('dbg3',val, sorted_nums[idx+1])
                heapq.heappush(heap, (-1*val+sorted_nums[idx+1]-sorted_nums[idx+2], idx+2))

