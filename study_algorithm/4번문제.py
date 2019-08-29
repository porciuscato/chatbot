import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    mini = 0
    for i in range(N):
        mini += board[i][0]

    def select(depth, tot):
        global mini
        if depth == N:
            if tot < mini:
                mini = tot
        else:
            for i in board[depth]:
                adder = tot + i
                if adder > mini:
                    continue
                else:
                    select(depth + 1, adder)

    select(0, 0)

    print('#{} {}'.format(T, mini))
