# SWEA 5656 벽돌 깨기
# 문제: W x H 판에 구슬을 N번 위에서 떨어뜨린다. 맞은 벽돌은 (숫자 - 1)칸 범위까지 연쇄로 깨지고,
#       깨진 뒤 남은 벽돌은 아래로 떨어진다. 남는 벽돌 수의 최솟값.
# 풀이: 구슬을 어느 열에 떨어뜨릴지 W^N가지(최대 12^4 = 20736)를 DFS로 모두 해 본다.
#       한 번 떨어뜨릴 때마다 판을 복사해서 ① 연쇄 폭발(BFS) ② 중력 순서로 처리한다.
from collections import deque

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def copy_board(board):
    new_board = []
    for row in board:
        new_board.append(row[:])
    return new_board


def shoot(board, col):
    """col 열에 구슬을 떨어뜨린 결과 판을 새로 만들어 돌려준다."""
    board = copy_board(board)
    # 1) 맨 위 벽돌 찾기
    top = -1
    for r in range(H):
        if board[r][col] != 0:
            top = r
            break
    if top == -1:                            # 빈 열이면 아무 일도 없다
        return board

    # 2) 연쇄 폭발: 큐에 (행, 열, 숫자)를 넣고 범위만큼 지운다
    queue = deque()
    queue.append((top, col, board[top][col]))
    board[top][col] = 0
    while len(queue) > 0:
        r, c, power = queue.popleft()
        for k in range(4):
            nr = r
            nc = c
            for step in range(power - 1):    # 숫자 - 1 칸까지
                nr = nr + DR[k]
                nc = nc + DC[k]
                if nr < 0 or nr >= H or nc < 0 or nc >= W:
                    break
                if board[nr][nc] != 0:
                    queue.append((nr, nc, board[nr][nc]))
                    board[nr][nc] = 0

    # 3) 중력: 열마다 남은 벽돌을 아래부터 다시 쌓는다
    for c in range(W):
        stack = []
        for r in range(H - 1, -1, -1):
            if board[r][c] != 0:
                stack.append(board[r][c])
        for r in range(H - 1, -1, -1):
            idx = H - 1 - r
            if idx < len(stack):
                board[r][c] = stack[idx]
            else:
                board[r][c] = 0
    return board


def count_bricks(board):
    count = 0
    for r in range(H):
        for c in range(W):
            if board[r][c] != 0:
                count = count + 1
    return count


def dfs(depth, board):
    global best
    remain = count_bricks(board)
    if remain == 0:                          # 다 깼으면 더 볼 필요 없음
        best = 0
        return
    if depth == N:
        if remain < best:
            best = remain
        return
    for col in range(W):
        dfs(depth + 1, shoot(board, col))
        if best == 0:
            return


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    start = []
    for i in range(H):
        start.append(list(map(int, input().split())))

    best = 999999
    dfs(0, start)
    print("#" + str(tc) + " " + str(best))
