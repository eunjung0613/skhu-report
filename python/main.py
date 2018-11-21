"""
챕터: day6
주제: class 상속/ 계승
문제: 모듈
작성자: 김은정
작성일: 2018.11.15
"""
"""
실행부
A. s 변수는 도형이다.
B. 반지름이 5인 원을 정의하여 c 변수에 저장한다.
C. 가로, 세로가 5, 10인 직사각형을 정의하여 r에 저장한다.
D. 세변이 3(밑변),4,5이고, 높이가 4인 삼각형을 정의하여 t에 저장한다.
E. c의 면적과 둘레를 출력한다.
F. r의 면적과 둘레를 출력한다.
G. t의 면적과 둘레를 출력한다.
H. t의 변들을 리스트로 받아 출력한다.
l. 리스트 l을 정의하여,s,c,r,t을 요소로 추가한다.
j. l의 각 요소에 대해, 해당 요소를 출력하고, 면적과 둘레를 계산하여 출력한다.
*for문 안에서 테스트: getRadius()메쏘드를 수행한다. (오류발생, 이유 생각해보기)
"""
#필요한 모듈을 수입하기

import shape # Shape.py에 정의된 클래스, 함수 등을 수입해서 사용하겠다는 의미

s = shape.Shape() # Shape를 s변수에 저장 # shape.의 의미는 "shape.py에서 정의된" 을 의미. .py 확장자는 붙이지 않는다.
                    #Shape가 shape.py에 정의된 클래스임을 의미.
c = shape.Circle(5) # Circle을 c변수에 저장
r = shape.Rectangle(5,10) # Rectangle을 r 변수에 저장
t = shape.Triangle(3,4,5,4) # Triangle을 t 변수에 저장
print("c의 면적: %d "%(c.area())) # c의 면적과 둘레 출력
print("c의 둘레: %d "%(c.perimeter()))
print("r의 면적: %d "%(r.area())) # r의 면적과 둘레 출력
print("r의 둘레: %d "%(r.perimeter()))
print("t의 면적: %d "%(t.area())) # t의 면적과 둘레 출력
print("t의 둘레: %d "%(t.perimeter()))
print(t.getSide()) # t의 변들을 리스트로 받아 출력
l = [] # 빈 리스트 l 정의
l.append(s) # ㅣ에 차례대로 s,c,r,t를 요소로 추가
l.append(c)
l.append(r)
l.append(t)
print("==== 리스트 해당요소 출력 ====") # 리스트 해당요소 출력하기
for i in range(0,len(l)): # for문을 0부터 l의 요소만큼 돌면서
    print(l[i]) # l의 i 번째 요소를 print.
print("==== 리스트 해당요소의 면적과 둘레 출력 ====") # 리스트의 해당요소의 면적과 둘레 출력
for i in range(0,len(l)): # for문을 0부터 l의 요소만큼 돌면서
    print("면적:"+str(l[i].area())) # l의 i번째 면적의 값을 출력
for i in range(0,len(l)): # for문을 0부터 l의 요소만큼 돌면서
    print("둘레:"+str(l[i].perimeter())) # l의 i번째 면적의 값을 출력

#for i in range(0,len(l)): # for문을 0부터 l의 요소만큼 돌면서
    #print("getRadius 출력해보기:"+str(l[i].getRadius())) # getRadius 출력해 보기. 하지만 오류발생!.