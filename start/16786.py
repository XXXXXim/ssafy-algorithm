T = int(input())

for tc in range(1, T + 1):
    # 입력이 "4 47FE" 처럼 들어오니까 N(길이)과 hex_str(16진수)로 쪼개서 받기
    N, hex_str = input().split()
    
    # 1타 강사 1줄 컷 최적화 (단어장 필요 없음!)
    # hex_str에서 글자를 하나씩 빼와서 4자리 2진수로 바꾼 뒤, 기차처럼 하나로 합치기!
    result = "".join(f"{int(char, 16):04b}" for char in hex_str)
    
    # 출력
    print(f"#{tc} {result}")