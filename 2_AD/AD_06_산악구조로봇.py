# AD_06 산악 구조 로봇
# 풀이: 칸마다 드는 비용이 달라서 BFS가 아니라 다익스트라를 쓴다.
#       "지금까지 연료가 가장 적은 칸"부터 꺼내서 이웃을 갱신한다.
import sys
import heapq
input = sys.stdin.readline


def move_cost(now_height, next_height):
    """높이 now_height 칸에서 next_height 칸으로 갈 때 드는 연료."""
    if next_height < now_height:
        return 0                                  # 내리막
    elif next_height > now_height:
        return (next_height - now_height) * 2     # 오르막
    else:
        return 1                                  # 평지


DR = [-1, 1, 0, 0]   # 상, 하, 좌, 우
DC = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    INF = 999999999
    dist = []                         # dist[r][c] = (r, c)까지 최소 연료
    for i in range(N):
        dist.append([INF] * N)
    dist[0][0] = 0

    heap = []
    heapq.heappush(heap, (0, 0, 0))   # (연료, 행, 열) - 연료가 작은 것이 먼저 나온다

    while len(heap) > 0:
        fuel, r, c = heapq.heappop(heap)
        if fuel > dist[r][c]:
            continue                  # 이미 더 싼 길로 처리한 칸이면 건너뛴다

        for k in range(4):
            nr = r + DR[k]
            nc = c + DC[k]
            if 0 <= nr < N and 0 <= nc < N:
                new_fuel = fuel + move_cost(board[r][c], board[nr][nc])
                if new_fuel < dist[nr][nc]:          # 더 싼 길을 찾았으면
                    dist[nr][nc] = new_fuel          # 갱신하고
                    heapq.heappush(heap, (new_fuel, nr, nc))   # 다시 넣는다

    print("#" + str(tc) + " " + str(dist[N - 1][N - 1]))
