"""
챕터: day5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제: 팩토리얼 계산
작성자: 김은정
작성일: 2018. 10. 11
"""

a = int(input("구하고 싶은 팩토리얼의 수를 쓰세요. :"))

def pac (a):
        if a ==1:
            return a
        else:
            return a*pac(a-1)

print(pac(a))