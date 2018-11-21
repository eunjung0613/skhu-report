"""
챕터: day5
주제: 매개변수의 전달 방식 비교
문제:
작성자: 김은정
작성일: 2018. 10. 4
"""

#매개변수의 수정 여부 확인을 위한 함수 정의
#call-by-value 방식으로 매개변수 값을 전달
#매개변수 값을 복사(copy)하여 전달
def modify(n):
    n = n+1
    return n

#실행 시작 부분
k =10 #변수 정의
print("호출 전 k=",k) #호출 전 변수값 출력
re = modify(k)#modify 호출 후 결과값을 re에 저장
print("호출 후 k=",k) #호출 후 변수 값 출력
print("re=",re)
