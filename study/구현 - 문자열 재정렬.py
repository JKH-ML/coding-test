"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 K1KA5CB7 이라는 값이 들어오면 ABCKK13을 출력합니다.


입력
첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)
입력 예시) K1KA5CB7

출력
첫째 줄에 문제에서 요구하는 정답을 출력합니다.
출력 예시) ABCKK13
"""

def solution(string):
    array = sorted(list(string))
    temp = 0
    result = []
    for i in range(len(array)):
        if ord(array[i]) - ord('A') < 0: 
            temp += int(array[i])
        else:
            result.append(array[i])
    result.append(str(temp))
    result = ''.join(result)
    return result
   
    
print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))




# isalpha() 라는 함수가 존재함!

# array.sorted() 의 반환값은 None이다.
# 즉, array2 = array.sorted() 이건 말이 안된다.
# array.sorted() 로 sort를 한 후 array2 = array 해야한다.
# 또는 array2 = sorted(array) 해도 되는데 이건 새 리스트를 반환한다.
# 다만 sorted(array) 와 같이 하면 전체 복사본을 만들기 때문에 메모리 사용량이 크다.
