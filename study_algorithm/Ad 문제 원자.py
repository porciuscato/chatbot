import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    base = []
    N = int(input())
    K = 0
    for _ in range(N):
        atom = list(map(int, input().split()))
        atom = [atom[0] * 2, atom[1] * 2, atom[2], atom[3]]
        base.append(atom)

    mini = 1000
    maxi = -1000
    for i in range(N):
        if base[i][0] < mini:
            mini = base[i][0]
        if base[i][0] > maxi:
            maxi = base[i][0]
        if base[i][1] < mini:
            mini = base[i][1]
        if base[i][1] > maxi:
            maxi = base[i][1]

    def timer(arr):
        global K
        result = []
        length = len(arr)
        destroyed = [0] * length
        for i in range(length):
            if arr[i][2] == 0:
                arr[i][1] += 1
            elif arr[i][2] == 1:
                arr[i][1] -= 1
            elif arr[i][2] == 2:
                arr[i][0] -= 1
            elif arr[i][2] == 3:
                arr[i][0] += 1
        for i in range(length):
            if not destroyed[i]:
                count = 0
                for j in range(i + 1, length):
                    if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1] and not destroyed[j]:
                        count += 1
                        K += arr[j][3]
                        destroyed[j] = 1
                if count >= 1:
                    destroyed[i] = 1
                    K += arr[i][3]
        for i in range(length):
            if not destroyed[i]:
                result.append(arr[i])
        return result


    for i in range(maxi - mini):
        base = timer(base)

    print('#{} {}'.format(T, K))
