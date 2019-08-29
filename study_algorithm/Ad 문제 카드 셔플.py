# 카드 셔플 문제

import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    que = []
    count = 0


    def isordered(arr):
        direction = 0
        length = len(arr)
        if arr[0] > arr[-1]:
            direction = 1
        if direction:
            for i in range(length - 1):
                if arr[i] - arr[i + 1] != 1:
                    return False
            return True
        else:
            for i in range(length - 1):
                if arr[i + 1] - arr[i] != 1:
                    return False
            return True


    que.append([cards, 0])
    while que:
        result = que.pop(0)
        if isordered(result[0]):
            break

        for i in range(N):
            arr1 = result[0][:N // 2]
            arr2 = result[0][N // 2:]
            # 카드셔플하고 que에 넣는다.

        if count >= 5:
            count = -1
            break

    print('#{} {}'.format(T, count))

