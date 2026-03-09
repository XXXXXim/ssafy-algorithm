#재귀함수: 자기자신을 호출하는 함수
# - 끝나는 지점이 필요
#  -1. 시작
#  -2. 종료 
#  -3. 누적된 값

# 0~ 10 출력
# - 0 부터 시작
# - 10에서 종료(정확하게는:10보다 커지면 종료)
# - 다음 재귀호출 : num을 1씩 증가

def recur(num):   
    if num > 3:                    #1) 종료코드 : num이 10보다 커지면
        return
    print(num, end=' ')                
    recur(num + 1)                 #2) 다음재귀호출 - num을 1씩 증가
    recur(num + 1)  
recur(0)


def recur2(num):
    if num > 3:
        return
    
    for i in range(1, 7):
        recur(num + 1)
    
    # recur(num + 1)
    # recur(num + 1)
    # recur(num + 1)
    # recur(num + 1)
    # recur(num + 1)
    # recur(num + 1)