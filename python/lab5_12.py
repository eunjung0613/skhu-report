"""
챕터: day5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제: 곱하기를 더하기 반복문으로 구현한 함수 prod를 정의하여 prod(3,6)을 계산하여 출력
작성자: 김은정
작성일: 2018. 10. 11
"""
def prod(a,b):
    c = 0
    for i in range(0,b):
        c += a
    return c

#재귀함수를 이용하여 구현한 함수 r_prod
def r_prod(a,b):
    if b == 1:
        return a
    else:
        return 3+r_prod(a,b-1)
print(prod(3,6))
print(r_prod(3,6))