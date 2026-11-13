# 백준 4485 녹색 옷 입은 애가 젤다지?
# 문제: N x N 동굴의 각 칸에 도둑루피(잃는 돈)가 있다. (0,0)에서 (N-1,N-1)까지 잃는 돈의 최솟값.
#       N = 0이 나올 때까지 여러 문제가 이어진다. 출력은 "Problem 번호: 답".
# 풀이: 다익스트라. 보급로(1249)와 같지만 출발 칸의 값도 잃는다는 점이 다르다.
import sys
import heapq
input = sys.stdin.readline

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

number = 0
while True:
    N = int(input())
    if N == 0:
        break
    number = number + 1
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    INF = 999999999
    dist = []
    for i in range(N):
        dist.append([INF] * N)
    dist[0][0] = board[0][0]                 # 출발 칸에서도 돈을 잃는다

    heap = []
    heapq.heappush(heap, (board[0][0], 0, 0))
    while len(heap) > 0:
        cost, r, c = heapq.heappop(heap)
        if cost > dist[r][c]:
            continue
        for k in range(4):
            nr = r + DR[k]
            nc = c + DC[k]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + board[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))

    print("Problem " + str(number) + ": " + str(dist[N - 1][N - 1]))
