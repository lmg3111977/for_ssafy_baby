# SWEA 5643 키 순서
# 문제: "a번이 b번보다 작다" 비교 결과 일부가 주어진다. 자기 키 순서를 확실히 아는 학생 수
# 풀이: 학생 x보다 "확실히 큰 학생 수 + 확실히 작은 학생 수 = n - 1"이면 x의 순서가 정해진다.
#       화살표 a -> b (a가 b보다 작다)를 따라가며 BFS로 닿는 학생 수를 센다.
#         - 정방향 그래프에서 x로부터 닿는 학생 = x보다 큰 학생
#         - 역방향 그래프에서 x로부터 닿는 학생 = x보다 작은 학생
from collections import deque


def count_reachable(start, graph):
    """start에서 화살표를 따라 닿을 수 있는 학생 수(자기 자신 제외)."""
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque()
    queue.append(start)
    count = 0
    while len(queue) > 0:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                count = count + 1
                queue.append(u)
    return count


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    m = int(input())

    taller = []                 # taller[a] = a보다 크다고 직접 주어진 학생들
    shorter = []                # shorter[b] = b보다 작다고 직접 주어진 학생들
    for i in range(n + 1):
        taller.append([])
        shorter.append([])
    for i in range(m):
        a, b = map(int, input().split())
        taller[a].append(b)
        shorter[b].append(a)

    answer = 0
    for x in range(1, n + 1):
        big = count_reachable(x, taller)      # 나보다 큰 학생 수
        small = count_reachable(x, shorter)   # 나보다 작은 학생 수
        if big + small == n - 1:
            answer = answer + 1

    print("#" + str(tc) + " " + str(answer))
