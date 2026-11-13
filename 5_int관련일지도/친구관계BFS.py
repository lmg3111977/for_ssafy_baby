# 친구 관계 BFS
# 문제: 1~7번 학생의 친구 관계가 주어질 때, 한 학생에서 친구를 따라 닿을 수 있는 학생 수(자기 제외)의 최댓값.
# 풀이: 학생마다 BFS로 같은 묶음의 학생을 세고, 그중 최댓값을 출력한다.

from collections import deque

friends = [
    [],         # 0번은 사용하지 않음
    [2, 3],     # 1번의 친구
    [1, 4],     # 2번의 친구
    [1, 4],     # 3번의 친구
    [2, 3, 5],  # 4번의 친구
    [4],        # 5번의 친구
    [7],        # 6번의 친구
    [6]        # 7번의 친구
]
for el in friends:
    el.sort()
# print(friends)
def bfs(s):
    visited[s]=True
    q=deque()
    q.append(s)
    stack=[]
    while q:
        v=q.popleft()
        for n in friends[v]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                stack.append(n)
    return len(stack)

max_student=-1
visited=[False]*8
for i in range(1,len(friends)):
    student=bfs(i)
    visited=[False]*8
    max_student=max(max_student,student)
print(max_student)