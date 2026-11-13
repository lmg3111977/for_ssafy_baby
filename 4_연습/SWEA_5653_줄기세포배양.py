# SWEA 5653 줄기세포배양
# 문제: 생명력 X인 세포는 X시간 비활성 -> X시간 활성 -> 죽음. 활성이 된 첫 1시간에 상하좌우로 번식.
#       빈 칸에 여러 세포가 동시에 번식하면 생명력이 큰 세포가 차지한다. 죽은 세포도 칸을 차지한다.
#       K시간 뒤 살아 있는(비활성 + 활성) 세포 수.
# 풀이: 판이 무한히 넓으므로 2차원 배열 대신 딕셔너리 {(행, 열): (생명력, 태어난 시간)}를 쓴다.
#       태어난 시간 b, 생명력 X인 세포는
#         - b + X 시간에 활성이 되고, 그다음 1시간 동안 번식 -> 새 세포는 b + X + 1 시간에 태어남
#         - b + 2X 시간에 죽음
#       그래서 "언제 번식하는가"를 시간별 목록에 미리 넣어 두고 시간을 1씩 진행한다.

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cells = {}                       # (행, 열) -> (생명력, 태어난 시간)
    spread_at = {}                   # 시간 -> 그 시간에 새 세포를 낳을 세포 위치 목록
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            if row[c] > 0:
                cells[(r, c)] = (row[c], 0)
                t = row[c] + 1       # 태어난 시간 0 + X + 1
                if t not in spread_at:
                    spread_at[t] = []
                spread_at[t].append((r, c))

    for time in range(1, K + 1):
        if time not in spread_at:
            continue
        # 이번 시간에 태어날 세포 후보: 빈 칸마다 가장 큰 생명력만 남긴다
        newborn = {}
        for (r, c) in spread_at[time]:
            life = cells[(r, c)][0]
            for k in range(4):
                pos = (r + DR[k], c + DC[k])
                if pos in cells:                 # 이미 세포가 있던 칸(죽은 세포 포함)
                    continue
                if pos not in newborn or newborn[pos] < life:
                    newborn[pos] = life
        for pos in newborn:
            life = newborn[pos]
            cells[pos] = (life, time)
            t = time + life + 1
            if t not in spread_at:
                spread_at[t] = []
            spread_at[t].append(pos)

    alive = 0
    for pos in cells:
        life, born = cells[pos]
        if K < born + 2 * life:                  # 아직 죽지 않음
            alive = alive + 1

    print("#" + str(tc) + " " + str(alive))
