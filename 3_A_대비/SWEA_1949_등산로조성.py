# SWEA 1949 등산로 조성
# 문제: 가장 높은 봉우리에서 출발해 상하좌우로 "더 낮은 칸"으로만 이어 가는 가장 긴 등산로.
#       딱 한 칸을 최대 K만큼 깎을 수 있다.
# 풀이: DFS + 백트래킹. 다음 칸이 높아서 못 갈 때, 아직 안 깎았고 K로 충분하면
#       그 칸을 "지금 높이 - 1"까지만 깎고 들어간다(더 많이 깎으면 손해).

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def dfs(r, c, length, used_cut):
    """(r, c)까지 length칸짜리 등산로를 만들었다. used_cut = 이미 깎았는지."""
    global best
    if length > best:
        best = length

    for k in range(4):
        nr = r + DR[k]
        nc = c + DC[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if visited[nr][nc]:                      # 이미 지나온 칸은 다시 못 간다
            continue

        if board[nr][nc] < board[r][c]:
            # 1) 원래 더 낮은 칸: 그냥 간다
            visited[nr][nc] = True
            dfs(nr, nc, length + 1, used_cut)
            visited[nr][nc] = False
        elif not used_cut and board[nr][nc] - K < board[r][c]:
            # 2) 깎으면 갈 수 있는 칸: 지금 높이보다 딱 1 낮게만 깎는다
            original = board[nr][nc]
            board[nr][nc] = board[r][c] - 1
            visited[nr][nc] = True
            dfs(nr, nc, length + 1, True)
            visited[nr][nc] = False
            board[nr][nc] = original             # 원래 높이로 되돌리기


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    # 봉우리는 "깎기 전" 지도에서 가장 높은 칸들
    top = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] > top:
                top = board[r][c]

    visited = []
    for i in range(N):
        visited.append([False] * N)

    best = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == top:
                visited[r][c] = True             # 출발 칸도 방문 표시(빠뜨리면 오답)
                dfs(r, c, 1, False)
                visited[r][c] = False

    print("#" + str(tc) + " " + str(best))
