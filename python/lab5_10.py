"""
챕터: day5
주제: lambda함수
-무명함수
-매개변수를 받을 수 있다.
-한줄 계산
-반환값이 1개, 한줄 계산의 결과가 반환 값.
문제:
작성자: 김은정
작성일: 2018. 10. 11
"""

# 합을 구하는 lambda 함수 (다른말로 무명함수)
sum = lambda x,y: x+y #람다함수의 시작 주소값을 sum에 저장. 실행되는 것은 아님.
k = sum(5,8) # lambda함수 호출
#sum을 실행.
print(sum(10,5))
print(k)