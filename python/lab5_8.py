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

def modify(s):
    s += " To you"
    return s

msg = "Happy Birthday"
print("호출 전 msg = ",msg)
re = modify(msg)
print("호출 후 msg = ",msg)
print("re = ",re)