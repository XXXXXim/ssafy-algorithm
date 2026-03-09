arr = [1,2,3,4,5,6]
N = 3

selected = [0] * len(arr)
# selected[1] =0 => 1번 위치에 있는 숫자(숫자2)는 쓴 적 없다

# selected[2] =1 => 2번 위치에 있는 숫자(숫자3)는 쓴 적 있다
#재귀함수
#숫자를 3번 선택하면 끝
# 한 번 선택할 때 1~6 사이의 숫자를 선택 *3
#내가 지금까지 몇번 선택했는지 나타낼 변수 :i
# 내가 지금까지 선택한 숫자를 저장할 리스트 path
#이전에 골랐던 숫자는 다시 못고른다
#내가 이전에 어떤 숫자를 골랐었는지 아닌지 체크 = selected 
def perm(i,path,selected):
    # 1. 종료조건
    if i == N:
        print(path)
        return
    
    #2.재귀호출
    # i번 단계에서 할 작업을 처리(숫자 1~6 사이에서 하나 고르기)
    # 단, 0~(i-1)단계에서 고른적 없는 숫자여야 가능


    # 다음단계 (i+1로) 재귀호출
    # i번 단계에서 한 번 골랐던 숫자를 빼고 다시 다른 숫자를 넣을 수 있도록 처리
    for j in range(len(arr)):
        #arr 안에서 j번 인덱스에 있는 숫자를 i번 위치에 놓겠다.
        #j번 인덱스에 있는 숫자는 이전 단게에서 쓴적 없어야함.
        if not selected[j]:
            # j번 인덱스에 있는 숫자 선택
            path.append(arr[j])
            #선택했다고 표시
            selected[j] = 1
            perm(i+1, path, selected)
            #순열의 i번위치에 arr의 j번 인덱스에 있던 숫자를 빽 다른숫자 넣기 위한 처리
            path.pop()
            selected[j] = 0

perm(0,[],selected)