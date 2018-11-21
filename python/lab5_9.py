"""
챕터: day5
주제: 매개변수의 전달 방식 비교 (call-by-refernce)
문제: list를 받아서, 마지막 리스트의 요소의 개수를 요소로 추가하는 함수 addNum을 정의한다. 반환되는 값은 없다.
[5,9,14,3]을 저장하는 list를 변수 l을 정의한다.
l을 인수로 addNum함수를 호출한 후 l을 출력한다.
작성자: 김은정
작성일: 2018. 10. 11
"""
#매개변수의 수정 여부 확인을 위한 함수 정의
#call - by- refrence 방식으로 매개변수 값을 전달

global_v = 100 #전역변수

def addNum(a): # list를 받아
    # global global_v
    # addNum 함수를 호출하면서 global변수를 200으로 다시 수정정의
    global_v = 200# gloval함수를 200으로 다시 정의
    a.append(len(a)) # 마지막 리스트의 요소의 개수를 요소로 추가하는 함수 addNum 정의.

l = [5,9,14,3] #list 정의

# 함수 호출 및 프린트
addNum(l)
print(l)

print(global_v) #결과값 100