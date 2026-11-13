# AD_04 지역구 나누기
# 풀이: 마을이 최대 8개라 나누는 방법이 2^8 = 256가지뿐 -> 전부 해 본다.
#       나누는 방법은 "비트마스크"로 표현: i번째 비트가 1이면 마을 i는 A, 0이면 B
import sys
from collections import deque
input = sys.stdin.readline


def is_connected(group):
    """group(마을 번호 목록) 안의 마을들이 group 안의 길만으로 모두 이어지면 True."""
    in_group = [False] * N
    for v in group:
        in_group[v] = True

    visited = [False] * N
    queue = deque()
    queue.append(group[0])          # 아무 마을 하나에서 출발
    visited[group[0]] = True
    count = 1                       # 방문한 마을 수

    while len(queue) > 0:
        v = queue.popleft()
        for u in range(N):
            # 길이 있고(adj=1), 같은 지역구이고, 아직 안 간 마을
            if adj[v][u] == 1 and in_group[u] and not visited[u]:
                visited[u] = True
                count = count + 1
                queue.append(u)

    return count == len(group)      # 모두 방문했으면 연결된 것


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    adj = []
    for i in range(N):
        row = list(map(int, input().split()))
        adj.append(row)
    people = list(map(int, input().split()))

    best = 999999
    # mask = 1 ~ 2^N - 2 (전부 A나 전부 B는 지역구가 하나뿐이라 제외)
    for mask in range(1, (1 << N) - 1):
        group_a = []
        group_b = []
        for i in range(N):
            if mask & (1 << i):     # i번째 비트가 1 -> A
                group_a.append(i)
            else:                   # 0 -> B
                group_b.append(i)

        if is_connected(group_a) and is_connected(group_b):
            sum_a = 0
            for v in group_a:
                sum_a = sum_a + people[v]
            sum_b = 0
            for v in group_b:
                sum_b = sum_b + people[v]
            diff = abs(sum_a - sum_b)
            if diff < best:
                best = diff

    print("#" + str(tc) + " " + str(best))
