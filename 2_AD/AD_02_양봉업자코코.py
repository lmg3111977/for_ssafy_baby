# AD_02 양봉업자 코코
# 풀이: 모든 칸에서 시작해 DFS로 4칸을 골라 본다(완전탐색)
#       + DFS 한 줄 경로로는 못 만드는 "가운데 1칸 + 이웃 3칸" 모양은 따로 계산
import sys
input = sys.stdin.readline

# 벌집은 열마다 높이가 엇갈린다. 짝수 열(0,2,4..)은 위로, 홀수 열(1,3..)은 반 칸 아래로.
# 그래서 짝수 열과 홀수 열은 대각선 이웃의 행 번호가 다르다.
EVEN_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1)]  # 짝수 열: 대각선 이웃은 윗줄(r-1)
ODD_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1)]     # 홀수 열: 대각선 이웃은 아랫줄(r+1)


def get_neighbors(r, c):
    """(r, c) 칸과 붙어 있는 칸들의 좌표 목록을 돌려준다(판 밖은 뺀다)."""
    if c % 2 == 0:
        dirs = EVEN_DIRS
    else:
        dirs = ODD_DIRS

    result = []
    for d in dirs:
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < N and 0 <= nc < M:
            result.append((nr, nc))
    return result


def dfs(r, c, count, total):
    """지금 (r, c)까지 count칸을 골랐고 합이 total이다. 4칸이 될 때까지 이웃으로 뻗어 간다."""
    global best
    if count == 4:                      # 4칸을 다 골랐으면
        if total > best:                # 최댓값 갱신
            best = total
        return

    for (nr, nc) in get_neighbors(r, c):
        if not visited[nr][nc]:         # 아직 고르지 않은 칸만 (not = 아니면)
            visited[nr][nc] = True      # 고른다고 표시
            dfs(nr, nc, count + 1, total + board[nr][nc])
            visited[nr][nc] = False     # 돌아와서 표시를 지운다(백트래킹)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    visited = []
    for i in range(N):
        visited.append([False] * M)

    best = 0
    for r in range(N):
        for c in range(M):
            # 1) (r, c)에서 출발하는 모든 4칸 경로
            visited[r][c] = True
            dfs(r, c, 1, board[r][c])
            visited[r][c] = False

            # 2) 가운데 (r, c) + 이웃 중 큰 값 3개 (Y자, 삼각형 모양)
            #    이웃은 모두 가운데와 붙어 있으니 어떤 3개를 골라도 연결된다.
            values = []
            for (nr, nc) in get_neighbors(r, c):
                values.append(board[nr][nc])
            if len(values) >= 3:
                values.sort(reverse=True)           # 큰 값부터 정렬
                total = board[r][c] + values[0] + values[1] + values[2]
                if total > best:
                    best = total

    print("#" + str(tc) + " " + str(best))
