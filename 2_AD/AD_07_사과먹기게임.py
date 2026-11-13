# AD_07 사과 먹기 게임
# 풀이: 상태 = (행, 열, 바라보는 방향). 전진은 비용 0, 우회전은 비용 1.
#       비용이 0과 1뿐이라 "0-1 BFS"(덱 사용)로 최소 비용을 구한다.
#       사과마다 구간을 나눠서, 도착할 때 바라보는 방향별 비용을 다음 구간으로 넘긴다.
import sys
from collections import deque
input = sys.stdin.readline

DR = [0, 1, 0, -1]   # 방향 0:오른쪽 1:아래 2:왼쪽 3:위 (시계 방향 순서)
DC = [1, 0, -1, 0]   # 그래서 우회전 = 방향 번호 + 1
INF = 999999999


def go_to_apple(start_r, start_c, start_cost, target_r, target_c):
    """(start_r, start_c)에서 출발해 (target_r, target_c)에 도착한다.
    start_cost[d] = 방향 d를 보고 출발할 때 이미 쓴 우회전 수
    돌려주는 값: arrive[d] = 방향 d로 사과에 도착할 때 최소 우회전 수"""
    # cost[r][c][d] 3차원 표 만들기
    cost = []
    for r in range(N):
        line = []
        for c in range(N):
            line.append([INF, INF, INF, INF])
        cost.append(line)

    dq = deque()
    for d in range(4):
        if start_cost[d] < INF:
            cost[start_r][start_c][d] = start_cost[d]
            dq.append((start_cost[d], start_r, start_c, d))

    arrive = [INF, INF, INF, INF]
    while len(dq) > 0:
        now, r, c, d = dq.popleft()
        if now > cost[r][c][d]:
            continue
        if r == target_r and c == target_c:
            # 사과 칸에 들어서는 순간 먹으므로 여기서 더 움직이지 않는다
            if now < arrive[d]:
                arrive[d] = now
            continue

        # 1) 앞으로 한 칸 (비용 0) -> 덱의 앞에 넣는다
        nr = r + DR[d]
        nc = c + DC[d]
        if 0 <= nr < N and 0 <= nc < N:
            if now < cost[nr][nc][d]:
                cost[nr][nc][d] = now
                dq.appendleft((now, nr, nc, d))

        # 2) 제자리에서 우회전 (비용 1) -> 덱의 뒤에 넣는다
        nd = (d + 1) % 4
        if now + 1 < cost[r][c][nd]:
            cost[r][c][nd] = now + 1
            dq.append((now + 1, r, c, nd))

    return arrive


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    # 사과 번호 -> 위치
    apple_pos = {}
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                apple_pos[board[r][c]] = (r, c)

    now_cost = [0, INF, INF, INF]      # 처음: 오른쪽(0번 방향)을 보고 우회전 0번
    now_r = 0
    now_c = 0
    for number in range(1, len(apple_pos) + 1):      # 1번 사과부터 순서대로
        target_r, target_c = apple_pos[number]
        now_cost = go_to_apple(now_r, now_c, now_cost, target_r, target_c)
        now_r = target_r
        now_c = target_c

    print("#" + str(tc) + " " + str(min(now_cost)))
