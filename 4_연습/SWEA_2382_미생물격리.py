# SWEA 2382 미생물 격리
# 문제: N x N 판의 가장자리는 약품 칸. 미생물 군집이 매시간 자기 방향으로 한 칸 이동한다.
#       약품 칸에 닿으면 수가 절반(나머지 버림)이 되고 방향이 반대로 바뀐다.
#       같은 칸에 모이면 합쳐지고, 방향은 수가 가장 많았던 군집의 방향을 따른다.
#       M시간 뒤 남은 미생물 수의 합.
# 풀이: 군집 목록을 그대로 시뮬레이션한다. 한 시간마다
#       ① 모두 이동(약품 처리) ② 같은 칸끼리 합치기

# 방향: 1 위, 2 아래, 3 왼쪽, 4 오른쪽 (0번은 비워 둠)
DR = [0, -1, 1, 0, 0]
DC = [0, 0, 0, -1, 1]
REVERSE = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    groups = []                              # [행, 열, 미생물 수, 방향]
    for i in range(K):
        r, c, count, d = map(int, input().split())
        groups.append([r, c, count, d])

    for hour in range(M):
        # ① 이동
        for g in groups:
            g[0] = g[0] + DR[g[3]]
            g[1] = g[1] + DC[g[3]]
            if g[0] == 0 or g[0] == N - 1 or g[1] == 0 or g[1] == N - 1:   # 약품 칸
                g[2] = g[2] // 2
                g[3] = REVERSE[g[3]]

        # ② 같은 칸끼리 합치기: 칸 -> [합계, 가장 큰 군집 수, 그 방향]
        merged = {}
        for g in groups:
            if g[2] == 0:                    # 다 죽은 군집은 버린다
                continue
            pos = (g[0], g[1])
            if pos not in merged:
                merged[pos] = [g[2], g[2], g[3]]
            else:
                info = merged[pos]
                info[0] = info[0] + g[2]
                if g[2] > info[1]:           # 더 큰 군집의 방향을 따른다
                    info[1] = g[2]
                    info[2] = g[3]

        groups = []
        for pos in merged:
            info = merged[pos]
            groups.append([pos[0], pos[1], info[0], info[2]])

    total = 0
    for g in groups:
        total = total + g[2]
    print("#" + str(tc) + " " + str(total))
