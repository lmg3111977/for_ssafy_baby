# SWEA 4014 활주로 건설
# 문제: N x N 지형의 각 행과 각 열에 활주로를 놓을 수 있는지 센다.
#       높이가 1 차이 나는 곳에는 길이 X, 높이 1인 경사로를 놓을 수 있다(겹쳐 놓기 불가).
# 풀이: 한 줄(리스트)씩 앞에서부터 보며
#       오르막이면 "지금 칸 포함 왼쪽 X칸", 내리막이면 "다음 칸부터 오른쪽 X칸"이
#       같은 높이이고 아직 경사로가 없는지 확인한다.


def can_build(line):
    """한 줄에 활주로를 놓을 수 있으면 True."""
    used = [False] * N                      # 경사로를 이미 놓은 칸
    for i in range(N - 1):
        now = line[i]
        nxt = line[i + 1]
        if now == nxt:
            continue
        if abs(now - nxt) > 1:              # 2 이상 차이 나면 불가
            return False

        if nxt == now + 1:
            # 오르막: i, i-1, ..., i-X+1 칸에 경사로
            for j in range(i - X + 1, i + 1):
                if j < 0 or line[j] != now or used[j]:
                    return False
                used[j] = True
        else:
            # 내리막: i+1, ..., i+X 칸에 경사로
            for j in range(i + 1, i + X + 1):
                if j >= N or line[j] != nxt or used[j]:
                    return False
                used[j] = True
    return True


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    count = 0
    for r in range(N):                      # 가로줄
        if can_build(board[r]):
            count = count + 1
    for c in range(N):                      # 세로줄
        column = []
        for r in range(N):
            column.append(board[r][c])
        if can_build(column):
            count = count + 1

    print("#" + str(tc) + " " + str(count))
