# SWEA 2105 디저트 카페
# 문제: 대각선으로만 움직여 사각형을 그리며 출발점으로 돌아온다. 같은 디저트 종류는 두 번 못 먹는다.
#       먹을 수 있는 디저트 수의 최댓값(불가능하면 -1).
# 풀이: 사각형은 "출발점(맨 위 꼭짓점) + 오른쪽 아래로 a칸 + 왼쪽 아래로 b칸"으로 정해진다.
#       모든 출발점과 a, b를 해 보며, 네 변을 따라 걸으면서 종류가 겹치는지 확인한다.

# 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위 (시계 방향으로 한 바퀴)
DR = [1, 1, -1, -1]
DC = [1, -1, -1, 1]


def tour(r, c, a, b):
    """(r, c)에서 a, b, a, b칸씩 네 방향으로 돌 때 먹는 디저트 수. 겹치거나 밖이면 -1."""
    eaten = set()
    steps = [a, b, a, b]
    for k in range(4):
        for s in range(steps[k]):
            r = r + DR[k]
            c = c + DC[k]
            if r < 0 or r >= N or c < 0 or c >= N:
                return -1
            if board[r][c] in eaten:          # 같은 디저트를 또 먹게 됨
                return -1
            eaten.add(board[r][c])
    return len(eaten)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    best = -1
    for r in range(N):
        for c in range(N):
            for a in range(1, N):
                for b in range(1, N):
                    # 사각형이 판 밖으로 나가면 확인할 필요도 없다
                    if c + a >= N or c - b < 0 or r + a + b >= N:
                        continue
                    if 2 * (a + b) <= best:   # 이보다 작은 사각형은 기록을 못 넘는다
                        continue
                    result = tour(r, c, a, b)
                    if result > best:
                        best = result

    print("#" + str(tc) + " " + str(best))
