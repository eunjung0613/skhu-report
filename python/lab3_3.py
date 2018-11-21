"""
챕터: day3
주제: 문자열 함수
작성자: 김은정
작성일 : 2018. 9. 6
"""

s = "   Test your Python debugging skills    "
print(s.upper()) #대문자로 변환하여 출력
print(s.lower()) #소문자로 변환하여 출력

#문자열 안의 t의 갯수를 출력
print(s.count('t'))
print(s.count('T', 1)) # 두번째 매개변수는 count 계산을 시작하는 위치

#사용자로부터 문자를 입력 받아, 대소문자 구분 없이 해당 문자의 개수를 출력
c = input("문자를 입력해주세요 : ") #사용자로부터 문자 입력 받기
s1=s.upper() #비교되는 문자열을 대문자로 변환하여 s1에 저장
#s1에 s를 대문자로 변환하여 저장하였기 때문에 s에는 영향이 없음.
print(s)
print(s1)
print(s1.count(c.upper())) #비교되는 문자를 대문자로 변환하여 개수를 계산

# t가 있는 위치를 출력
print(s.index('t'))
print(s.index('t',4)) # 두번째 매개변수는 검색 시작 위치

# index() 함수는 찾으려는 문자가 없으면 valueError 발생
#print(s.index('x'))

# 대상 문자를 찾을 수 있는 또 다른 함수
print(s.find('t'))
print(s.find('x')) # 찾고자 하는 문자가 없는 경우, -1을 반환한다.

#strip() 함수 테스트
print(s)
#왼쪽 공백 제거 후 출력
print(s.lstrip())
#오른쪽 공백 제거 후 출력
print(s.rstrip())
#양쪽 공백 제거 후 출력
print(s.strip())

# 내용 바꾸기
# 문장에서 Python을 Java로 바꾸어 출력
print(s.replace("Python","Java")) #replace가 s 자체를 변경하지는 않는다.

# 문장에서 e를 i로 모두 바꾸어 출력
print(s.replace("e","i",1))#3번째 매개변수는 변경할 최대 개수를 지정

# split 연습
# 앞뒤 공백을 제거한 후 빈칸을 기준으로 단어를 모두 나누기
print(s.strip().split(" ")) #s.strip() 이 문자열을 반환하는 함수였기 때문에 '.'이 한번 더 붙을 수 있었음.
print(s.strip().split(" ",2)) #두개만 떼어 내기
#split() 함수는 문자열의 list를 반환하지 문자열을 반환하지 않는다.

#s의 길이 출력
print(len(s))

s = "test"
s = ' kkk'
s= '''
여러줄을
한꺼번에
사용 가능!
'''

i = input("문자열: ") # i의 데이터 타입은 문자열, input은 문자열을 반환하기 때문이다.
i = int(input("문자열: ")) # int()함수를 앞에 붙이면 i의 데이터 타입은 int.

j = 100 #j는 int
s1 = str(j) #s1은 str 타입
