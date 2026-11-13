# SWEA 1953 탈주범 검거
# 문제: 터널 구조물(1~7)마다 뚫린 방향이 다르다. 맨홀에서 시작해 L시간 동안 갈 수 있는 칸 수.
# 풀이: BFS. 두 칸이 이어지려면 "내 칸에서 그 방향이 뚫려 있고, 상대 칸에서 반대 방향이 뚫려 있어야" 한다.
#       맨홀 칸이 1시간째이므로 거리(시간)가 L 이하인 칸만 센다.
from collections import deque

DR = [-1, 1, 0, 0]          # 0:위 1:아래 2:왼쪽 3:오른쪽
DC = [0, 0, -1, 1]
OPPOSITE = [1, 0, 3, 2]     # 위<->아래, 왼쪽<->오른쪽

# 구조물 번호별로 뚫린 방향 [위, 아래, 왼쪽, 오른쪽]
PIPE = [
    [False, False, False, False],  # 0: 터널 없음
    [True, True, True, True],      # 1: 상하좌우
    [True, True, False, False],    # 2: 상하
    [False, False, True, True],    # 3: 좌우
    [True, False, False, True],    # 4: 상, 우
    [False, True, False, True],    # 5: 하, 우
    [False, True, True, False],    # 6: 하, 좌
    [True, False, True, False],    # 7: 상, 좌
]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    time = []                        # time[r][c] = 도착한 시간 (0이면 아직 안 감)
    for i in range(N):
        time.append([0] * M)

    queue = deque()
    queue.append((R, C))
    time[R][C] = 1                   # 맨홀에 들어간 것이 1시간째
    count = 1

    while len(queue) > 0:
        r, c = queue.popleft()
        if time[r][c] == L:          # 이미 L시간이면 더 못 간다
            continue
        for k in range(4):
            if not PIPE[board[r][c]][k]:          # 내 칸에서 이 방향이 막힘
                continue
            nr = r + DR[k]
            nc = c + DC[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if time[nr][nc] != 0:                  # 이미 간 칸
                continue
            if not PIPE[board[nr][nc]][OPPOSITE[k]]:   # 상대 칸에서 반대쪽이 막힘
                continue
            time[nr][nc] = time[r][c] + 1
            count = count + 1
            queue.append((nr, nc))

    print("#" + str(tc) + " " + str(count))
