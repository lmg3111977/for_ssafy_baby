# AD_12 농사 로봇
# 풀이: 시작 위치(모든 농지) x 시작 방향(4개)을 전부 그대로 시뮬레이션해서 최댓값을 고른다.
#
# 날짜 계산 정리:
#   p일에 심음 -> p+1일에 싹 -> 싹 난 뒤 (3 + K)일 후 곡식 (K = 그 농지에서 몇 번째 싹인지)
#   => 오늘(day) - 심은 날(p) >= 4 + K 이면 곡식이 열린 상태
import sys
input = sys.stdin.readline

DR = [-1, 0, 1, 0]   # 방향 0:위 1:오른쪽 2:아래 3:왼쪽 (시계 방향)
DC = [0, 1, 0, -1]
TURN_ORDER = [1, 0, 3, 2]   # 이동 우선순위: 오른쪽(+1) > 앞(+0) > 왼쪽(+3) > 뒤(+2)


def is_ripe(r, c, day):
    """(r, c)에 곡식이 열려 있으면 True."""
    if plant_day[r][c] == -1:            # 심은 게 없음
        return False
    return day - plant_day[r][c] >= 4 + sprout_count[r][c]


def can_move_to(r, c, day):
    """로봇이 (r, c)로 들어갈 수 있으면 True. 빈 농지 또는 곡식이 열린 농지만 가능."""
    if board[r][c] == 1:                 # 산
        return False
    if plant_day[r][c] == -1:            # 빈 농지
        return True
    return is_ripe(r, c, day)            # 싹이 자라는 중이면 False, 곡식이면 True


def find_next(r, c, d, day):
    """오른쪽 > 앞 > 왼쪽 > 뒤 순서로 처음 갈 수 있는 곳을 찾는다. 없으면 None."""
    for turn in TURN_ORDER:
        nd = (d + turn) % 4
        nr = r + DR[nd]
        nc = c + DC[nd]
        if can_move_to(nr, nc, day):
            return (nr, nc, nd)
    return None


def simulate(r, c, d):
    """(r, c)에서 방향 d로 시작해 M일 동안 일했을 때 수확 횟수."""
    global plant_day, sprout_count
    plant_day = []                       # 씨를 심은 날 (-1 = 빈 농지)
    sprout_count = []                    # 이 농지에서 싹이 난 횟수 K
    for i in range(N):
        plant_day.append([-1] * N)
        sprout_count.append([0] * N)

    harvest = 0
    for day in range(1, M + 1):
        # ---- 오전 ----
        if is_ripe(r, c, day):
            harvest = harvest + 1        # 곡식이 열렸으면 수확
            plant_day[r][c] = -1         # 수확하면 빈 농지가 된다
        elif plant_day[r][c] == -1:
            # 빈 농지: 다음 칸으로 갈 수 있을 때만 씨를 심는다
            if find_next(r, c, d, day) is not None:
                plant_day[r][c] = day
                sprout_count[r][c] = sprout_count[r][c] + 1

        # ---- 오후 ----
        next_move = find_next(r, c, d, day)
        if next_move is not None:
            r, c, d = next_move          # 이동하면서 그 방향을 바라본다
        # 갈 곳이 없으면 제자리에 머문다

    return harvest


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    best = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:         # 농지에서만 시작할 수 있다
                for d in range(4):
                    result = simulate(r, c, d)
                    if result > best:
                        best = result

    print("#" + str(tc) + " " + str(best))
