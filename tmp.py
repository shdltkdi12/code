import heapq

def f(intervals):
    if not intervals:
        return 0
    intervals.sort()
    heap = []
    ans=  [0 for _ in range(len(intervals))]
    max_day = 1
    for i, (start, end) in enumerate(intervals):
        while heap and heap[0][0] <= start:
            end, idx, day = heapq.heappop(heap)
            ans[idx] = day
            max_day = 1

        if heap:
            max_day +=1
            heapq.heappush(heap, (end, i, max_day))
        else:
            heapq.heappush(heap, (end, i, 1))
    while heap:
        _, idx, day = heapq.heappop(heap)
        ans[idx] = day
    return ans
