# AD_03 스노우맨
# 풀이: LIMIT을 0, 1, 2, ... 로 늘려 가며 BFS로 "보석에 닿는가?"를 확인한다.
#       처음으로 닿는 LIMIT이 정답.
import sys
from collections import deque
input = sys.stdin.readline


def can_reach(limit):
    """수직이동을 한 번에 limit칸까지 할 수 있을 때 보석에 도착할 수 있으면 True."""
    visited = []
    for i in range(N):
        visited.append([False] * M)

    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True

    while len(queue) > 0:
        r, c = queue.popleft()
        if r == gem_r and c == gem_c:          # 보석 도착
            return True

        # 1) 좌우 이동: 바로 옆 칸이 땅이면 갈 수 있다
        for nc in [c - 1, c + 1]:
            if 0 <= nc < M:
                if board[r][nc] != 0 and not visited[r][nc]:
                    visited[r][nc] = True
                    queue.append((r, nc))

        # 2) 상하 이동: 1칸 ~ limit칸 떨어진 곳에 땅이 있으면 그 땅에 착지할 수 있다
        #    (땅을 밟으면 게이지가 0이 되므로, 한 번의 수직이동은 limit칸 이하)
        for direction in [-1, 1]:              # -1 = 위로, 1 = 아래로
            for k in range(1, limit + 1):
                nr = r + direction * k
                if nr < 0 or nr >= N:          # 판 밖이면 그만
                    break
                if board[nr][c] != 0 and not visited[nr][c]:
                    visited[nr][c] = True
                    queue.append((nr, c))

    return False                               # 끝까지 못 찾음


N, M = map(int, input().split())
board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# 출발 지점(2)과 보석(3) 위치 찾기
for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            start_r = r
            start_c = c
        if board[r][c] == 3:
            gem_r = r
            gem_c = c

# LIMIT을 0부터 하나씩 늘려 본다
limit = 0
while True:
    if can_reach(limit):
        print(limit)
        break
    limit = limit + 1
