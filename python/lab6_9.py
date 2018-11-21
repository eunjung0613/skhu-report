"""
챕터: day6
주제: 정규식
문제: 정규식 기호 연습
작성자: 김은정
작성일: 2018.11.15
"""
import re # regular expreesion 모듈 수입

# 테스트할 각종 문자열 정의
s = "teeeeest"
s2 = "tetst"
s3 = "tst"
s4 = "apple"
s5 = "test1234Test"
s6 = "나는 \"왕\"이다" # 진짜 더블쿼트를 출력하고 싶다면 \" \" (excape를 쿼트 앞에 써주기)

r = re.compile('\d')#숫자를 찾아서 반환 #re 라는 모듈에 정의된 함수를 호출한 것
print(r.search(s)) #regular express object에 정의된 메쏘드 호출
print(r.search(s5))

r = re.compile('\D')#숫자가 아닌 것 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('[a-zA-Z]')#알파벳만 찾아서 반환
print(r.search(s))#
print(r.search(s5))#

# 25-27 까지 코드를 함수인 serach 를 이용하여 다시 코드 쓰기
print(re.search('[a-zA-Z]',s))

#s5에서 알파벳 또는 숫자 찾기
print(re.search('[a-zA-Z0-9]',s5)) #또는 \w
#s5에서 숫자 찾기
print(re.search('[0-9]',s5)) # 또는 \d
#s5에서 대문자 찾기
print(re.search('[A-Z]',s5))
#s5에서 소문자 찾기
print(re.search('[a-z]',s5))

#s6
print(s6)
print(re.search("\"",s6))

print(re.search("\W",s6)) #문자 또는 숫자가 아닌 것을 검색