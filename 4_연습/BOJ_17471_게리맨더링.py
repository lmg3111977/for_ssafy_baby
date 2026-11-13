# 백준 17471 게리맨더링
# 문제: N개 구역을 두 선거구로 나눈다. 각 선거구 안의 구역은 서로 연결돼 있어야 한다.
#       두 선거구 인구 차이의 최솟값(나눌 수 없으면 -1).
# 풀이: 비트마스크로 모든 나누기 + 각 선거구 BFS 연결 확인.
#       다른 점: 입력이 인접 행렬이 아니라 "인접한 구역 수, 구역 번호들" 목록이고, 번호가 1부터.
import sys
from collections import deque
input = sys.stdin.readline


def is_connected(group):
    """group 안의 구역들이 group 안의 길만으로 모두 이어지면 True."""
    in_group = [False] * (N + 1)
    for v in group:
        in_group[v] = True
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(group[0])
    visited[group[0]] = True
    count = 1
    while len(queue) > 0:
        v = queue.popleft()
        for u in adj[v]:
            if in_group[u] and not visited[u]:
                visited[u] = True
                count = count + 1
                queue.append(u)
    return count == len(group)


N = int(input())
people = [0] + list(map(int, input().split()))      # 1번부터 쓰려고 앞에 0
adj = [[]]
for i in range(N):
    line = list(map(int, input().split()))
    adj.append(line[1:])                             # 첫 숫자는 개수라서 뺀다

best = -1
for mask in range(1, (1 << N) - 1):
    group_a = []
    group_b = []
    for i in range(N):
        if mask & (1 << i):
            group_a.append(i + 1)
        else:
            group_b.append(i + 1)
    if is_connected(group_a) and is_connected(group_b):
        sum_a = 0
        for v in group_a:
            sum_a = sum_a + people[v]
        sum_b = 0
        for v in group_b:
            sum_b = sum_b + people[v]
        diff = abs(sum_a - sum_b)
        if best == -1 or diff < best:
            best = diff

print(best)
