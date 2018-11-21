"""
챕터: day6
주제: class
문제: 분수 클래스 정의
작성자: 김은정
작성일: 2018.10.30
"""
def gcm(x,y):
    """
    최대공약수를 반환하는 함수
    :param x: 첫번째 정수
    :param y: 두번째 정수
    :return:
    """
    #두 정수 중 큰 수를 x에 저장, 작은 수를 y에 저장
    if y>x:
        temp = y
        y = x
        x = temp

    #유클리드 호제법에 의해 최대 공약수를 구함
    while (y>0):
        r=x%y
        x=y
        y=r
    return x

#분수 클래스 정의

class Fraction:
    def __init__(self,n,d):
        """
        :param n: 분자에 해당하는 값
        :param d: 분모에 해당하는 값
        """
        self.numer = n
        self.denom = d

    def add(self, o):
        r = Fraction(5,3)
        return r

    def __str__(self):
        return str(self.numer)+"/"+str(self.denom)

    def __add__(self, other):
        return Fraction((self.numer * other.denom)+(self.denom*other.numer),(self.denom*other.denom))
    def __eq__(self, o):
        """
        self와 o가 약분하여 같은 분수이면 True를 반환
        :param o: 다른 분수
        :return: 약분하여 같은 분수이면 True를 반환, 아니면 False를 반환
        """
        g1 = gcm(self.numer, self.denom)#약분을 위해 분모와 분자의 gcm 구하기
        g2 = gcm(o.numer,o.denom)
        if (self.numer//g1 == o.numer//g2) and (self.denom//g1,other.denom):
            return True
        else:
            return False
    def __ne__(self,o):
        """
        두 분수가 같으면 True, 아니면 False를 반환
        """
        if (self ==o):
            return False
        else:
            return True

#실행코드 시작
f1 = Fraction(4,5)
f2 = Fraction(3,5)
print(f1.add(f2))
print(f1 == f2)
print(f1 != f2)