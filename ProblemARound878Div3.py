num = int(input())

for i in range(num):
    n = int(input())
    str1 = input()
    str2 = ""

    z = 0
    while z < n:
        str2 += str1[z]
        j = z + 1
        while j < n:
            if str1[j] == str1[z]:
                z = j
                break
            j += 1
        z += 1

    print(str2)
