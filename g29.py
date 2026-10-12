def f(arr):
    n = len(arr)
    prefix = [1] *n
    suffix = [1]*n
    for i in range(1,n):
        prefix[i] = 1 if arr[i-1] > arr[i] else prefix[i-1]+1
    for i in range(n-2,-1,-1):
        suffix[i] = 1 if arr[i] > arr[i+1] else suffix[i+1] + 1
    ans = 0
    for i in range(n):
        prev = float('-inf') if i-1 <0 else arr[i-1]
        next = float('inf') if i +1 == n else arr[i+1]
        
        prev_sum = 0 if i-1 <0 else prefix[i-1]
        next_sum = 0 if i+1 == n else suffix[i+1]
        ans = max(ans, prev_sum+1, next_sum+1)
        if prev <= next:
            ans = max(ans, prev_sum+next_sum+1)
    return ans


