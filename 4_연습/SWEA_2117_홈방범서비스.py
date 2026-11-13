# SWEA 2117 홈 방범 서비스
# 문제: 마름모 영역(크기 K)의 운영 비용 = K*K + (K-1)*(K-1). 집 한 채당 M원을 낸다.
#       손해를 보지 않으면서 가장 많은 집에 서비스할 때 그 집의 수.
# 풀이: 모든 중심 칸 x 모든 K(1 ~ N+1)를 해 본다.
#       (r, c)가 크기 K 마름모 안에 있다 = |r - 중심r| + |c - 중심c| < K
#       K = N+1이면 어디가 중심이든 도시 전체를 덮으므로 거기까지만 보면 된다.

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    houses = []                       # 집 좌표 목록
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                houses.append((r, c))

    best = 0
    for cr in range(N):
        for cc in range(N):
            # 중심에서 각 집까지 거리(맨해튼)를 센다: count_at[d] = 거리가 d인 집 수
            count_at = [0] * (2 * N + 1)
            for (r, c) in houses:
                d = abs(r - cr) + abs(c - cc)
                count_at[d] = count_at[d] + 1

            covered = 0               # 크기 K 마름모 안의 집 수 (거리 < K)
            for K in range(1, N + 2):
                covered = covered + count_at[K - 1]     # 거리 K-1인 집이 새로 들어온다
                cost = K * K + (K - 1) * (K - 1)
                if covered * M >= cost and covered > best:   # 손해가 아니면 기록
                    best = covered

    print("#" + str(tc) + " " + str(best))
