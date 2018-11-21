"""
챕터: day6
주제: 정규식
문제: 정규식 ^$[^][-]기호 연습
작성자: 김은정
작성일: 2018.11.15
"""
import re # regular expreesion 모듈 수입

# 테스트할 각종 문자열 정의
s = "teeeeest"
s2 = "tetst"
s3 = "tst"

r = re.compile('^t')#t로 시작하는 부분을 찾아서 반환
print(r.search(s))# t
print(r.search(s2))# t
print(r.search(s3))# t

r = re.compile('t$')#t로 끝나는 부분을 찾아서 반환
print(r.search(s))# t
print(r.search(s2))# t
print(r.search(s3))# t

r = re.compile('[^te]')#abc가 아닌 것 찾기
print(r.search(s))# s
print(r.search(s2))# s
print(r.search(s3))# s

r = re.compile('[a-m]')#a에서 m까지 찾기
print(r.search(s))# t
print(r.search(s2))# t
print(r.search(s3))# t