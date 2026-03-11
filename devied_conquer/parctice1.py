arr = [38, 27, 43, 3]

#  단 한 번! 원본 배열이랑 똑같은 크기의 0짜리 스페어 방을 미리 만들어 둔다!
# 이 temp 배열 하나를 merge 함수가 평생 돌려 쓰는 거야.
temp = [0] * len(arr) 


#분할과정 
def merge_sort(start,end):
#종료조건
    if start>= end:
        return
    
    mid = (start+end) //2
    merge_sort(start,mid)
    merge_sort(mid+1,end)
    merge(start, mid, end)

def merge(start, mid, end):

    l = start
    r = mid+1

    idx = start

    # 1. coloceum대결
    while l <= mid and r<= end:
        if arr[l] <= arr[r]:
            temp[idx] =arr[l]
            l+=1

        else:
            temp[idx]= arr[r]
            r+=1
        idx +=1

    while l <= mid:
        temp[idx] = arr[l]
        l+=1
        idx+=1
    while r <= end:
        temp[idx] = arr[r]
        r+=1
        idx+=1

    for i in range(start, end+1):
        arr[i] = temp[i]



merge_sort(0, len(arr) - 1)
print(arr)            