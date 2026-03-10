#5명중 N명뽑기

arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []


# N명 -> depth : N
# 5명 중 하나 선택 -> branch : 5

#1. 전체 순열코드 부터 시작
#2. 직전 선택을 다음 재귀호출로 넘겨주고,
# 그 다음부터 선택하도록 구성
def recur(cnt, prev):
    if cnt == N:
        print(*path)
        return
    # 이전에 선택했던 것 다음거부터 탐색
    #중복조합 : 이전에선택했던 것부터 탐색(중복허용)
    for i in range(prev, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i) # 이전 선택을함께 전달
        path.pop()

# recur(0, -1) #중복제거호출
recur(0,0) #중복 허용