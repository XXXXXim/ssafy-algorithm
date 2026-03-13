# N번쏘기
# -연쇄작용
# -벽돌 숫자에 맞게 상하좌우로 폭발
# - 연쇄작용이후
# -벽돌이 떨어짐

# -최대한 많은 벽돌 제거
#     - 모든 좌표에 구슬을 떨어뜨려봐야 계산가능
# -> 완전탐색
# - N번쏜다 == depth:4
# - 1번당 구슬위치는 12종류 == bracnh:12

# - 가지치기 가능한 조건이 있나?
# - 남은 벽돌이 0개라면 종료
# --> 남은 벽돌도 변수로 관리하자

# 벽돌깨기
# 1. 최소 벽돌
# - 현재 벽돌이 다 깨지면 더이상 할 필요없다
# - 현재 벽돌 수를 관리해아한다,

# 2. N번의 구슬을 쏘자
# - 모든 케이스를 보아야 한다 (0000~ 11 11 11 11)
# - 한번 쐇을때
#   - 연쇄작용 (bfs)
#     - 델타 배열
#     - 빈칸메우기
# - 연쇄작용 하면 원본배열이 수정될 수 있다
# 1. 원본배열을 저장해두고 수정 후 원상복구
# 2. 원본배열을 복사해서 복사된 뱅병ㄹㅇ르 뱌열을 수정하고 다음 재귀로 전달하자.]
def recur(cnt,ramain_blocks, now):
    if cnt == N or ramain_blocks == 0:
        global min_answer
        min_answer = min(min_answer, ramain_blocks)
        return
    
    # 모든 열에 슈슛
    for col in range(W):
        #연쇄작용
        # -col에 구슬을 쏘기 전 상태 복사
        copy_arr = [row[:] for row in arr]







T =int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_answer = 1e9    #최소벽돌수(정답)
    
    blocks = 0