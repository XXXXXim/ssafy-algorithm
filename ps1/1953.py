# bFS 상세
# - 탐색: 상하좌우
# - 이동이 불가능한 케이스
#     - [델타배열 기본] 범위 밖으로 나가면 못감
#     - [방문 기록] 이미 방문한 곳은 못감
#     - [0이면 못감]
#     - [문제 조건]
#         - 현재 내위치에서 뜷려있어야 이동가능
#         - 다음 위치의 입구가 뜷려있는 곳으로만 이동가능
        # -> 델타배열과 동일한 순서로 "이동가능여부를 기록" 하면 좋음

from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

types = {
    # 상하좌우 순서
    1:[1,1,1,1],
    2:[1,1,0,0],
    3:[0,0,1,1],
    4:[1,0,0,1],
    5:[0,1,0,1],
    6:[0,1,1,0],
    7:[1,0,1,0]
}
def bfs(R,C):
    q = deque([(R,C)])
    visited[R][C] = 1

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]
        #i방향이 안뜰ㄹ리면 못감 -> 다음방향 보자
        if dirs[i] == 0:
            continue

        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
        if 
    N,M,R,C,L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]