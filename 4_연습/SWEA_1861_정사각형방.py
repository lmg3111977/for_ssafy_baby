# SWEA 1861 정사각형 방
# 문제: N x N 방에 1 ~ N^2가 하나씩 적혀 있다. 상하좌우로 "정확히 1 큰 수"인 방으로만 이동한다.
#       가장 많은 방을 지나갈 수 있는 출발 방 번호(같으면 작은 번호)와 그 방 수.
# 풀이: 숫자 v에서 v+1로 갈 수 있는지만 알면 된다(이웃 중 v+1이 있는가).
#       그러면 v부터 시작한 경로 길이 = (v+1로 갈 수 있으면 v+1의 길이 + 1, 아니면 1).
#       큰 수부터 거꾸로 계산하면 한 번에 끝난다.

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    total = N * N
    can_go_next = [False] * (total + 2)      # can_go_next[v] = v에서 v+1로 갈 수 있는가
    for r in range(N):
        for c in range(N):
            v = board[r][c]
            for k in range(4):
                nr = r + DR[k]
                nc = c + DC[k]
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == v + 1:
                    can_go_next[v] = True

    length = [0] * (total + 2)               # length[v] = v에서 출발했을 때 지나는 방 수
    for v in range(total, 0, -1):            # 큰 수부터
        if can_go_next[v]:
            length[v] = length[v + 1] + 1
        else:
            length[v] = 1

    best_room = 1
    for v in range(1, total + 1):            # 작은 번호부터 보므로 같으면 작은 번호가 남는다
        if length[v] > length[best_room]:
            best_room = v

    print("#" + str(tc) + " " + str(best_room) + " " + str(length[best_room]))
