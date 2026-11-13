# AD_08 장기 포(包) 게임
# 풀이: DFS로 3번까지 모든 이동을 해 본다. 판을 바꿨다가 돌아오면 되돌린다(백트래킹).
#       먹은 쫄의 위치를 집합(set)에 모아서 마지막에 개수를 센다.
import sys
input = sys.stdin.readline

DR = [-1, 1, 0, 0]   # 상, 하, 좌, 우
DC = [0, 0, -1, 1]


def inside(r, c):
    return 0 <= r < N and 0 <= c < N


def dfs(r, c, moves):
    """포가 (r, c)에 있고 지금까지 moves번 움직였다."""
    if moves == 3:                       # 3번 다 움직였으면 끝
        return

    for k in range(4):
        # 1) 이 방향으로 가면서 처음 만나는 말 = 뛰어넘을 "다리"를 찾는다
        nr = r + DR[k]
        nc = c + DC[k]
        while inside(nr, nc) and board[nr][nc] == 0:
            nr = nr + DR[k]
            nc = nc + DC[k]
        if not inside(nr, nc):
            continue                     # 다리가 없으면 이 방향으로는 못 간다

        # 2) 다리 너머로 한 칸씩 가 본다
        nr = nr + DR[k]
        nc = nc + DC[k]
        while inside(nr, nc):
            if board[nr][nc] == 0:
                # 빈칸: 여기로 이동해 본다
                board[r][c] = 0
                board[nr][nc] = 2
                dfs(nr, nc, moves + 1)
                board[nr][nc] = 0        # 되돌리기
                board[r][c] = 2
            else:
                # 쫄: 먹고 그 자리로 이동. 쫄 너머로는 더 못 간다
                eaten.add((nr, nc))
                board[r][c] = 0
                board[nr][nc] = 2
                dfs(nr, nc, moves + 1)
                board[nr][nc] = 1        # 쫄 되살리기
                board[r][c] = 2
                break
            nr = nr + DR[k]
            nc = nc + DC[k]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    # 포(2)의 위치 찾기
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                po_r = r
                po_c = c

    eaten = set()        # 먹은 쫄의 원래 위치 (같은 쫄을 여러 번 먹어도 한 번만 센다)
    dfs(po_r, po_c, 0)
    print("#" + str(tc) + " " + str(len(eaten)))
