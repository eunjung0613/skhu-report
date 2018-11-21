"""
챕터: day6
주제: class 상속/ 계승
문제: shape, circle, rectangle 클래스 정의
작성자: 김은정
작성일: 2018.11.13
"""
"""
1. Shape 클래스를 정의한다. 메쏘드로 area(), perimeter()를 가지고 있다.
A. area는() 면적, perimeter()는 둘레를 반환한다. 하지만, shape 클래스는 0을 반환한다.
B.__str__()을 정의한다. "도형"을 반환
"""
class Shape (): # Shape 클래스 정의
    def area(self): # 면적을 반환하지만 shpae클래스에서는 0을 반환
        return 0
    def perimeter(self): # 둘레를 반환하지만 shape클래스에서는 0을 반환
        return 0
    def __str__(self): # print시 string형으로 도형 출력하기.
        return "도형"
"""
2. Shape를 계승하는, Circle클래스, Rectangle 클래스, Triangle 클래스 를 정의한다. __init__(),area(),perimeter(),__str()__를 정의한다.
   Triangle의 __init__는 세변과 높이를 매개변수로 받는다.
A. Circle 클래스에는 getRadius()메쏘드를 정의한다.(반지름).클래스 변수 PI=3.1415로 정의한다.
B. Triangle, Rectangle 클래스에는 getHeight()메쏘드를 정의한다.(높이)
C. Triangle, Rectangle 클래스에는 getWidth()메쏘드를 정의한다.(밑변)
D. Triangle, Rectangle 클래스에는 변의 길이를 시계방향으로 list 형태로 반환하는 getSides()메쏘드를 정의한다.
(변들을 반환, 삼각형 세변, 직사각형 4변)
"""
class Circle(Shape): # Shape를 계승하는 원의 면적과 둘레를 구하는 Circle 클래스 정의
    PI = 3.1415 # 변수 PI 정의
    def __init__(self,r): # 생성자 초기화 및 반지름 r 설정
        self.r = r
    def getRadius(self): # 반지름을 반환하는 getRadius 메쏘드 정의
        return self.r
    def area(self): # 면적을 구하는 area 메쏘드 정의
        totalarea = self.r *self.r * Circle.PI # 원의 면적을 구하는 공식에 따라 totalarea에 PI*반지름*반지름 저장
        return totalarea # 구한 면적 값을 반환
    def perimeter(self): # 둘레를 구하는 perimeter 메쏘드 정의
        total = self.r*2*Circle.PI # 원의 둘레를 구하는 공식에 따라 total에 2*PI*반지름을 저장
        return total # 구한 둘레 값을 반환
    def __str__(self): # 프린트 시 string 형으로 변환 후 출력을 위한 특수 메쏘드 정의
        return "원은 반지름: "+str(self.r) # 반지름 값을 반환
class Rectangle(Shape): # Shape를 계승하는 직사각형의 면적과 둘레를 구하는 Rectangle 클래스 정의
    def __init__(self,w,h): # 생성자 초기화 및 가로의 길이와 세로의 길이를 설정
        self.w = w # 가로의 길이
        self.h = h # 세로의 길이
    def getHeight(self): # 세로의 길이를 반환하는 getHeight 메쏘드 정의
        return self.h # 세로의 길이 반환
    def getWidth(self): # 가로의 길이를 반환하는 getWidth 메쏘드 정의
        return self.w # 가로의 길이 반환
    def area(self): # 면적을 구하는 area 메쏘드 정의
        totlaarea = self.w *self.h # 직사각형의 면적을 구하는 공식에 따라 totalarea에 면적 값을 저장
        return totlaarea # totalarea 값을 반환
    def perimeter(self): # 둘레를 구하는 perimeter 메쏘드 정의
        total = (self.h*2)+(self.w*2) # 직사각형의 둘레를 구하는 공식에 따라 total에 둘레 값을 저장
        return total # total 값을 반환
    def getSides(self): # 변의 길이를 시계방향으로 list 형태로 반환하는 getSides()메쏘드를 정의
        list1 = [] # 빈리스트 list1 정의
        list1.append(self.h) # 리스트 안에 시작하는 높이 추가
        list1.append(self.w) # 리스트 안에 가로값 추가
        list1.append(self.h) # 리스트 안에 반대 높이 추가
        list1.append(self.w) # 리스트 안에 반대 가로값 추가
        return list1 # list1을 반환
    def __str__(self): # 프린트 시 string 형으로 변환 후 출력을 위한 특수 메쏘드 정의
        return "직사각형의 밑변:"+str(self.w)+"\n"+"직사각형의 높이:"+str(self.h) # 밑변과 높이를 string 형으로 반환
class Triangle(Shape): # Shape를 계승하는 삼각형의 면적과 둘레를 구하는 Triangle 클래스 정의
    def __init__(self,w1,w2,w3,h): #생성자 초기화 및 세 변과 높이 설정
        self.w1 = w1 # 밑변
        self.w2 = w2 # 두번째 변
        self.h = h # 높이
        self.w3 = w3 # 세번째 변
    def area(self): # 면적을 구하는 area 메쏘드 정의
        totalarea = self.w1*self.h*0.5 # 삼각형의 면적을 구하는 공식에 따라 totalarea에 면적 값을 저장
        return totalarea # totalarea 값을 반환
    def perimeter(self): # 둘레를 구하는 perimeter 메쏘드 정의
        total = self.w1+self.w2+self.w3 # 삼각형의 둘레를 구하는 공식에 따라 total에 둘레 값을 저장
        return total # total 값을 반환
    def getHeight(self): # 높이를 반환하는 getHeight 메쏘드 정의
        return self.h
    def getWidth(self): # 밑변의 길이를 반환하는 getWidth 메쏘드 정의
        return self.w1
    def getSide(self): # 변의 길이를 시계방향으로 list 형태로 반환하는 getSides()메쏘드를 정의
        list2 = [] # 빈리스트인 list2 정의
        list2.append(self.w3) # 시계방향으로 처음 w3을 추가
        list2.append(self.w1) # 다음 밑변인 w1을 추가
        list2.append(self.w2) # 마지막으로 w2을 추가
        return list2 # list2 반환
    def __str__(self): # 프린트 시 string 형으로 변환 후 출력을 위한 특수 메쏘드 정의
        return "삼각형의 밑변:"+str(self.w1)+"\n"+"삼각형의 높이:"+str(self.h) #밑변과 높이를 string 형으로 반환

