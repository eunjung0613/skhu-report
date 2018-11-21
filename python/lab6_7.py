"""
챕터: day6
주제: 정규식
문제: 정규식 .?*+기호 연습
작성자: 김은정
작성일: 2018.11.15
"""

import re # regular expreesion 모듈 수입

# 테스트할 각종 문자열 정의
s = "teeeeest"
s2 = "tetst"
s3 = "tst"

r = re.compile('e.s')#e와 s 사이에 문자가 하나 있는 경우 찾기
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

r = re.compile('e?s')#? 앞에 문자가 존재하거나 존재하지 않는다. e가 0~1번 나타난 후 s가 나타나는 경우 찾기
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

r = re.compile('e*s')#e와 s 사이에 문자가 존재하거나 무한대로 존재, e가 0번 이상 존재한 후 s가 나타나는 경우 찾기
print(r.search(s)) # eeeees가 나올 것이다
print(r.search(s2)) #없어도 되므로 s가 나올 것이다.
print(r.search(s3)) #s가 나올 것이다.

r = re.compile('e+s')#바로 앞에 문자가 한번 이상 존재
print(r.search(s)) #eeeees
print(r.search(s2)) #None
print(r.search(s3)) #None

