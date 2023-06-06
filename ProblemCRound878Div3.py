num = int(input())

for i in range(num):
    n, k, q = map(int, input().split())
    temperatures = list(map(int, input().split()))

    valid_subarrays = 0
    current_length = 0

    for temp in temperatures:
        if temp <= q:
            current_length += 1
        else:
            current_length = 0

        if current_length >= k:
            valid_subarrays += current_length - k + 1

    print(valid_subarrays)
