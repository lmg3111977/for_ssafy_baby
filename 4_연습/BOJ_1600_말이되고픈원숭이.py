# 백준 1600 말이 되고픈 원숭이
# 문제: W x H 격자에서 왼쪽 위 -> 오른쪽 아래. 보통은 상하좌우 한 칸,
#       최대 K번은 체스 말(나이트)처럼 이동할 수 있다. 장애물(1)은 못 지나간다. 최소 동작 수(못 가면 -1).
# 풀이: BFS인데 상태에 "말처럼 뛴 횟수"를 넣는다: (행, 열, 사용한 점프 수).
#       같은 칸이라도 점프를 몇 번 썼는지에 따라 앞으로 할 수 있는 일이 다르기 때문.
import sys
from collections import deque
input = sys.stdin.readline

MONKEY = [(-1, 0), (1, 0), (0, -1), (0, 1)]
HORSE = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

K = int(input())
W, H = map(int, input().split())
board = []
for i in range(H):
    board.append(list(map(int, input().split())))

# visited[r][c][j] = 점프를 j번 쓰고 (r, c)에 온 적이 있는가
visited = []
for r in range(H):
    line = []
    for c in range(W):
        line.append([False] * (K + 1))
    visited.append(line)

queue = deque()
queue.append((0, 0, 0, 0))                  # (행, 열, 쓴 점프 수, 동작 수)
visited[0][0][0] = True
answer = -1
while len(queue) > 0:
    r, c, used, moves = queue.popleft()
    if r == H - 1 and c == W - 1:
        answer = moves
        break
    # 1) 원숭이처럼 한 칸
    for (dr, dc) in MONKEY:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == 0 and not visited[nr][nc][used]:
            visited[nr][nc][used] = True
            queue.append((nr, nc, used, moves + 1))
    # 2) 점프가 남았으면 말처럼
    if used < K:
        for (dr, dc) in HORSE:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == 0 and not visited[nr][nc][used + 1]:
                visited[nr][nc][used + 1] = True
                queue.append((nr, nc, used + 1, moves + 1))

print(answer)
