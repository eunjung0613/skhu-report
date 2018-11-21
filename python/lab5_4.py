"""
챕터: day5
주제: 함수
문제: 이름, 학번, 학과를 매개변수로 받아서 이를 출력하는 함수 print_string을 정의한다. 이때, 학과가 매개변수로 넘어오지 않으면, "소프트웨어공학과"
를 디폴트 값으로 한다.
작성자: 김은정
작성일: 2018. 10. 4
"""

#매개변수를 받는 함수 print_string 정의
#단, 학과의 디폴트 값을 "소프트웨어공학과"로 설정
def print_string(name,num,grade = '소프트웨어공학과'):
    return print(name,num,grade) #retrun 값으로 넘어온 매개변수 출력

#실행함수 호출
print_string("김은정","201814003")
print_string("김은정","201814003","IT자율융합학부")