from collections import Counter

def make_palindrome(s):
    # 문자열에서 각 문자의 개수를 계산
    char_count = Counter(s)
    
    # 팰린드롬 문자열의 절반을 초기화
    half_palindrome = []
    
    # 홀수 개수의 문자를 가진 경우 중간 문자를 저장
    middle_char = ''
    
    for char, count in sorted(char_count.items()):  # 알파벳 순으로 정렬
        # 문자의 개수가 홀수인 경우 중간 문자 설정
        if count % 2 == 1:
            # 이미 중간 문자가 설정되어 있는 경우 팰린드롬 불가능
            if middle_char:
                return "I'm Sorry Hansoo"
            middle_char = char
        
        # 문자열의 절반을 만들기 위해 절반 개수만큼 해당 문자를 추가
        half_palindrome.extend([char] * (count // 2))
    
    # 팰린드롬 문자열의 절반을 사용하여 완전한 팰린드롬 문자열 생성
    palindrome = ''.join(half_palindrome)
    
    # 중간 문자를 가운데에 추가 (홀수 개수의 문자를 가진 경우)
    if middle_char:
        palindrome = palindrome + middle_char
    
    # 반대로 뒤집어서 다시 더함
    palindrome = palindrome + ''.join(reversed(half_palindrome))
    
    return palindrome

# 입력 문자열
input_string = input()

# 팰린드롬으로 변환된 문자열 생성
output_string = make_palindrome(input_string)

# 결과 출력
if output_string == "I'm Sorry Hansoo":
    print(output_string)
else:
    print(output_string)