arr = [1,2,3,4,5,6]
N = 3

#재귀함수
#숫자를 3번 선택하면 끝
# 한 번 선택할 때 1~6 사이의 숫자를 선택 *3
#내가 지금까지 몇번 선택했는지 나타낼 변수 :i
# 내가 지금까지 선택한 숫자를 저장할 리스트 path

def recur(i, path):
    # 1. 종료조건
    if i == N:
        print(path)
        return
    
    # 2. 재귀호출
    # i번 단계에서 할 작업을 처리(숫자 1~6 사이에서 하나 고르기)
    # 다음단계 (i+1로) 재귀호출
    # i번 단계에서 한 번 골랐던 숫자를 빼고 다시 다른 숫자를 넣을 수 있도록 처리

    # path.append(1)
    # recur(i+1)
    # path.pop()

    # path.append(2)
    # recur(i+1)
    # path.pop()

    # path.append(3)
    # recur(i+1)
    # path.pop()
    # ..

    #arr안에 있는 숫자 골라서 i번 위치에 놓기
    for num in arr:
        #1~6사이에 있는 숫자 골라서 담기
        path.append(num)
        #담았으면 다음 숫자도 담으러 가기
        recur(i+1, path)
        #i번 위치에 다른 숫자도 놓아봐야 하니까 이번 숫자 다시 빼기
        path.pop()       
#0번 고르고 시작(고른적없음)
# 내가 고른숫자도 아직 암것도 없음 
recur(0,[])