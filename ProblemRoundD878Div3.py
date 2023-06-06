def is_valid(x, array):
    count = 1
    maximum = array[0]
    minimum = array[0]
    
    for i in range(1, len(array)):
        maximum = array[i]
        if ((maximum - minimum + 1) // 2) > x:
            count += 1
            minimum = array[i]
    
    if count > 3:
        return False
    
    return True

num = int(input())

for i in range(num):
    n = int(input())
    l1 = list(map(int, input().split()))
    l1.sort()
    
    low = 0
    high = int(1e9)
    ans = int(1e9)
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_valid(mid, l1):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(ans)
