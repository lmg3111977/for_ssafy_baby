# SWEA 1251 [S/W 문제해결 응용] 4일차 - 하나로
# 문제: N개 섬을 해저터널로 모두 잇는다. 터널 하나의 환경 부담금 = E * (길이)^2.
#       부담금 합의 최솟값을 반올림한 정수.
# 풀이: 최소 스패닝 트리(MST). 모든 섬 쌍이 연결 후보라 간선이 많으므로
#       프림 알고리즘을 배열로(O(N^2)) 돌린다.
#       길이^2만 필요하므로 제곱근을 쓰지 않는다: (x차)^2 + (y차)^2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    INF = float("inf")
    in_tree = [False] * N
    min_cost = [INF] * N        # min_cost[i] = 지금 트리에서 섬 i로 가는 가장 싼 터널(길이^2)
    min_cost[0] = 0
    total = 0

    for step in range(N):
        # 1) 트리 밖의 섬 중 가장 싸게 연결되는 섬 고르기
        pick = -1
        for i in range(N):
            if not in_tree[i] and (pick == -1 or min_cost[i] < min_cost[pick]):
                pick = i
        in_tree[pick] = True
        total = total + min_cost[pick]

        # 2) 새로 들어온 섬 기준으로 다른 섬들의 비용 갱신
        for i in range(N):
            if not in_tree[i]:
                dx = xs[pick] - xs[i]
                dy = ys[pick] - ys[i]
                d = dx * dx + dy * dy
                if d < min_cost[i]:
                    min_cost[i] = d

    answer = int(total * E + 0.5)            # 소수 첫째 자리에서 반올림
    print("#" + str(tc) + " " + str(answer))
