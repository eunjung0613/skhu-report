"""
챕터: day5
주제: 함수
문제: 두 개의 정수를 매개변수로 받아서, 두 수의 차를 반환하는 함수 subtract를 정의한다.
4,8을 매개변수로 subtract를 호출한 결과를 출력한다.
작성자: 김은정
작성일: 2018. 10. 2
"""

def subtract(a,b): #두 개의 정수를 매개변수로 받는 함수 정의 a = 첫번째 수, b = 두번째 수
    return a-b #두 수의 차를 반환

# 함수 호출
print(subtract(4,8)) #위치에 의해 인수(매개변수)가 전달됨
print(subtract(b=4,a=8)) #키워드 인수(매개변수)
#파이썬의 특징 중 하나 = 키워드 인수가 가능
a = 10
b = True
c = "김치"
# type = 변수의 타입을 반환
print(type(a)) #값에 따라 type이 계속 변하기 때문에 필요함.
print(type(b))
print(type(c))