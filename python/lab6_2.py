"""
챕터: day6
주제: class
문제: 좌표를 표현하는 클래스 Coordinate를 정의한다.
__init__는 x,y 좌표를 받아서 self의 x,y에 배정
거리를 구하는 distance 메소드를 정의한다. self와 다른 좌표 other을 매개변수로 받는다.
거리는 (x좌표 사이의 차의 제곱(**2로 계산)과 y좌표 사이 차의 제곱의 합)의 제곱근이다. 제곱근(**0.5)로 계산)
작성자: 김은정
작성일: 2018.10.18
"""

class Coordinate:
    def __init__(self, x, y): #x와 y좌표를 받아서 self의 x,y에 배정
        #python에서는 __init__함수를 한 클래스 당 하나만 정의할 수 있음.
        #매개변수 x: X좌표 값
        #매개변수 y: y좌표 값
        self.x = x
        self.y = y
    def distance(self, other):
        #두 좌표의 거리를 계산하여 반환
        #ohter: 다른좌표
        #self와 other와의 거리를 반환
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

# 실행 코드 시작

"""
실행코드 부분
(3,4) 좌표의 점 c를 정의
원점 origin 정의
(3,4)와 원점과의 거리를 출력
"""
C = Coordinate(3,4)
origin=Coordinate(0,0)
c1 = Coordinate(10,9)
print("거리: %.2f" %C.distance(origin))
# print("거리: %.2f" %origin.distance(C)) 도 작동함 / origin이 self, c가 other에 전달됨
print("거리: %.2f" %c1.distance(C)) #c1이 self로 넘어감 c가 other에 전달됨
print("거리: %.2f" %Coordinate.distance(c1,origin)) # 클래스 이름과 함께 메소드 호출 가능.
# 이 때는 self에 해당되는 매개변수를 보내야 한다.