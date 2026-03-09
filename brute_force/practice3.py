# 순열

arr = [1, 2, 3, 4, 5, 6]
N = 3

#방명록 만들기 : arr의길이만큼 0*6
selected = [0] * len(arr)

def perm(i, path, selected):
    # 1. 종료조건
    if i == N:
        print(path)
        return
    
    #2 재귀호출
    for j in range(len(arr)):
        # 핵심1: 방명록 확인(안쓴=0카드면 통과 쓴=1카드면 컷)
        if not selected[j]:
            
            #핵심2: 체크인
            path.append(arr[j])
            selected[j] = 1
            
            #직진(다음 자리 숫자 고르러 가기)
            perm(i +1, path, selected)
            
            #핵심 3:원상복구 $ 체크아웃 (다씀)
            path.pop()
            selected[j] = 0
            
perm(0, [], selected)