"""
챕터: day6
주제: class
문제:
fraction 클래스를 정의하고
작성자: 김은정
작성일: 2018.10.23
"""

#분수 클래스 정의

class Fraction:
    def __init__(self,n,d):
        """
        :param n: 분자에 해당하는 값
        :param d: 분모에 해당하는 값
        """
        self.numer = n
        self.denom = d

    def print(self,n,m):
        return print("%d/%d 와 %d/%d 의 덧셈,뺄셈,곱셈 나눗셈의 값은 %d/%d 입니다. "%(self.numer,self.denom,n.numer,n.denom,m.numer,m.denom))

   #분자와 분모의 최대공약수를 구해 약분하는 method
    def gvd(self):

        if self.numer > self.denom:
            j = self.denom
            if j < 0:
                j = -(self.denom)
        else:
            j = self.numer
            if j < 0:
                j = -(self.numer)
        for i in range (1, j+1):
            if (self.numer %i) == 0 and (self.denom % i) ==0:
                self.numer = self.numer/i
                self.denom = self.denom/i
        return Fraction(self.numer,self.denom)


    # 분자와 분모를 반환하는 method

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    # 값을 수정하는 set method
    def setNumer(self,n):
        self.numer = n

    def setDenom(self,d):
        self.denom = d

    #분수의 더하기 정의
    def add(self,o):
        d = self.denom * o.denom #분모계산
        n = (self.numer * o.denom) + (o.numer * self.denom) #분자계산
        r = Fraction(n,d)#결과 값을 포함하는 Fraction 분수 생성
        return r


    #분수의 뺄셈 정의
    def miu(self,v):
        d = self.denom * v.denom #분모계산
        n = (self.numer * v.denom) - (v.numer * self.denom)#분자계산
        r = Fraction(n,d)#결과 값을 포함하는 Fraction 분수 생성
        return r

    #분수의 곱셈 정의
    def gob(self,c):
        d = self.denom * c.denom #분모계산
        n = self.numer * c.numer#분자계산
        r = Fraction(n,d)#결과 값을 포함하는 Fraction 분수 생성
        return r

    #분수의 나눗셈 정의
    def qua(self,b):
        d = self.denom * b.numer #분모계산
        n = self.numer * b.denom #분자계산
        r = Fraction(n,d)#결과 값을 포함하는 Fraction 분수 생성
        return r
    # 최대 공약수로 나눈 후 return
    def gcd (a,b):
        if a < b :
            (a,b) = (b,a)
        while b != 0:
            (a,b) = (b,a%b)
        return Fraction(a,b)

#실행코드 시작
f1 = Fraction(1,2)
f2 = Fraction(5,4)

#사칙연산 계산 후 약분 결과 저장
addresult = f1.add(f2).gvd()
miuresult = f1.miu(f2).gvd()
gobresult = f1.gob(f2).gvd()
quaresult = f1.qua(f2).gvd()

#결과값 프린트
f1.print(f2,addresult)
f1.print(f2,miuresult)
f1.print(f2,gobresult)
f1.print(f2,quaresult)