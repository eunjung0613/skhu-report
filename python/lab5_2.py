"""
챕터: day5
주제: 함수
문제: 문자열의 튜플을 매개변수로 받아서, 해당 문자열들을 ','로 한 줄에 연결하여 출력하는 함수 print_string을 정의한다.
소프트웨어공학과, 정보통신학과, 글로컬IT학과, 컴퓨터공학과를 요소로 가지는 튜플을 매개변수로 해서 print_string을 호출한다.
작성자: 김은정
작성일: 2018. 10. 2
"""

tup = ("소프트웨어공학과","정보통신공학과","글로컬IT학과","컴퓨터공학과") #tuple 정의

def print_string(a): #print_string 함수 정의 ,a를 매개변수로 받음
    b = len(tup) #tuple의 길이를 반환
    s= '' #문자열을 저장할 빈 문자열 정의
    for i in range(b-1): #b의 바로 전까지 for문
        s += a[i]+',' #문자열을 이어붙임
    return print(s+a[b-1]) #print함수를 이용해 이어붙인 문자열s 와 튜플의 마지막을 이어붙여 출력
print_string(tup) #매개변수로 튜플 넘겨주기.

"""
교수님의 풀이!
def print_string(t):
    # t:문자열의 튜플
    # 반환값 없음 
    s = "" #문자열 초기화
    for i in range(0,len(t)-1): # i 튜플 내의 요소를 가리키는 인덱스
        s = s+t[i] # i 번째 문자
        if i != len(t)-1:
        s = s+","
    print(s)
#실행코드 시작
print_string(("소프트웨어공학과","정보통신공학과","글로컬 IT","컴퓨터공학과"))
"""