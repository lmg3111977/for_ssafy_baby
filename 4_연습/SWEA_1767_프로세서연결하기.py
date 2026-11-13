# SWEA 1767 프로세서 연결하기
# 문제: N x N 칩의 코어(1)를 가장자리까지 직선 전선으로 연결한다. 전선은 교차 불가.
#       연결한 코어 수를 최대로, 그중 전선 길이 합을 최소로.
# 풀이: 가장자리가 아닌 코어마다 (상, 하, 좌, 우, 연결 안 함) 5가지를 DFS로 모두 해 본다.
#       "남은 코어를 다 연결해도 최고 기록보다 적으면" 더 볼 필요가 없다(가지치기).

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def wire_length(r, c, k):
    """(r, c)에서 k 방향으로 끝까지 빈칸이면 전선 길이를, 막히면 -1을 돌려준다."""
    length = 0
    nr = r + DR[k]
    nc = c + DC[k]
    while 0 <= nr < N and 0 <= nc < N:
        if board[nr][nc] != 0:            # 코어나 다른 전선에 막힘
            return -1
        length = length + 1
        nr = nr + DR[k]
        nc = nc + DC[k]
    return length


def set_wire(r, c, k, value):
    """(r, c)에서 k 방향으로 가장자리까지 value(2=전선, 0=지우기)를 채운다."""
    nr = r + DR[k]
    nc = c + DC[k]
    while 0 <= nr < N and 0 <= nc < N:
        board[nr][nc] = value
        nr = nr + DR[k]
        nc = nc + DC[k]


def dfs(idx, connected, total):
    """cores[idx]를 고를 차례. 지금까지 connected개 연결, 전선 total."""
    global best_count, best_length
    # 가지치기: 남은 코어를 전부 연결해도 최고 기록에 못 미치면 중단
    if connected + (len(cores) - idx) < best_count:
        return
    if idx == len(cores):
        if connected > best_count:
            best_count = connected
            best_length = total
        elif connected == best_count and total < best_length:
            best_length = total
        return

    r, c = cores[idx]
    for k in range(4):
        length = wire_length(r, c, k)
        if length > 0:
            set_wire(r, c, k, 2)              # 전선 깔기
            dfs(idx + 1, connected + 1, total + length)
            set_wire(r, c, k, 0)              # 전선 걷기(되돌리기)
    dfs(idx + 1, connected, total)            # 이 코어는 연결하지 않는 경우


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    # 가장자리 코어는 이미 연결된 것으로 보므로 고를 필요가 없다
    cores = []
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if board[r][c] == 1:
                cores.append((r, c))

    best_count = -1
    best_length = 0
    dfs(0, 0, 0)
    print("#" + str(tc) + " " + str(best_length))
