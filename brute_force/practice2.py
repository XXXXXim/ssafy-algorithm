# 중복순열(원상복구(pop)의 마법)
#관련코드 = arr에서 3번 선택하는 중복순열
arr = [1, 2, 3, 4, 5, 6]
N = 3
def recur(i,path):
    
    # 1. 종료조건 : 3개를 다 골랐다면 출력하고 되돌아가기
    if i == N:
        print(path)
        return
    
    # 2. 모든 숫자를 다 조합하기
    for num in arr:
        path.append(num)    #일단 주머니에 넣기
        recur(i+1,path)     #다음자리(i+1)숫자 고르러 직진 
        path.pop()          #다른 숫자 넣기위해 방금 넣은거 뺌
        
recur(0,[])