from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    visited[0] = True          # 1번은 처음부터 보내는 사람
    q = deque([0])
    count = 0
    while q:
        u = q.popleft()
        for v in range(N):
            if arr[u][v] == 0:
                continue
            if v == N - 1:     # N번: 받기만 함
                count += 1
            elif not visited[v]:
                visited[v] = True
                q.append(v)
    print(f"#{tc} {count}")
