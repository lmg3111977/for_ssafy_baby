# SWEA 1249 [S/W 문제해결 응용] 4일차 - 보급로
# 문제: N x N 지도의 각 칸은 복구 시간(0~9). 왼쪽 위에서 오른쪽 아래까지 가는 경로의
#       복구 시간 합의 최솟값. 지도는 줄마다 공백 없이 숫자가 붙어서 주어진다.
# 풀이: 칸마다 비용이 다르므로 다익스트라. "그 칸에 들어갈 때 그 칸의 값"을 더한다.
import heapq

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        line = input().strip()               # 예: "0100"
        row = []
        for ch in line:
            row.append(int(ch))              # 글자 하나씩 숫자로
        board.append(row)

    INF = 999999999
    dist = []
    for i in range(N):
        dist.append([INF] * N)
    dist[0][0] = 0                           # 출발 칸은 복구할 필요 없음(0)

    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while len(heap) > 0:
        cost, r, c = heapq.heappop(heap)
        if cost > dist[r][c]:
            continue
        if r == N - 1 and c == N - 1:        # 도착하면 바로 끝
            break
        for k in range(4):
            nr = r + DR[k]
            nc = c + DC[k]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + board[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))

    print("#" + str(tc) + " " + str(dist[N - 1][N - 1]))
