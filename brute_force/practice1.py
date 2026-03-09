#재귀함수의 기본

def recur(num):
    # 1. 종료조건
    if num > 5:
        return
    
    # 2-1 재귀 호출 전(들어가는 길)
    print(num, end=' ')
    #미래의 나를 호출(여기서현재 함수는 일시정지!)
    recur(num + 1)
    
    # 2-2 재귀 호출 후(//나오는 길 - 백트래킹)
    print(num, end=' ')
recur(0)