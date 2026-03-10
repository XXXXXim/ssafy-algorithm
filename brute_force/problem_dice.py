#주사위 3개를 던져서 합이 10이하인 케이스 수

# 주사위 3개 : 상태공간트리 기준 depth: 3
# - branch 수:(재귀호출수) 1~6숫자 -> 6

# path=[]

# def recur(cnt):
    
#     global result
    
#     if cnt == 3:
#     #만약경로합이 10 이하라면
#         if sum(path) <= 10: 
#             print(*path)
#             result +=1 
#         return
    
#     for num in range(1,7):
#         path.append(num)
#         recur(cnt+1)
#         path.pop()

# recur(0)
result = 0
def recur(cnt, total):
    #이미 10을 넘었으면 이 케이스는 더 볼 필요 x
    #심화: 백트래킹의 원리 
    global result
    if total > 10: #종료조건
        return
    
    if cnt == 3:    #재귀호출
    #만약경로합이 10 이하라면
        if total <= 10: 
            result +=1 
        return
    
    for num in range(1,7):
    
        recur(cnt+1, total+num)


recur(0,0)
print(result)