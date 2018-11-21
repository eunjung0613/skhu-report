"""
챕터: day6
주제: class
문제: 분수 클래스 정의
작성자: 김은정
작성일: 2018.11.1~11.6
"""

#최대공약수 구하는 함수 정의
def gcm(x,y):
    """
    최대 공약수를 반환하는 함수
    :param x: 첫번째 정수
    :param y: 두번째 정수
     """
    if y<0 : #만약 y가 0보다 작다면
        y = (-y) #y에 y의 절대값을 저장
    elif x<0: #만약 x가 0보다 작다면
        x = (-x) #x에 x의 절대값을 저장
        if y>x: #x가 y보다 작다면
            temp = y
            y = x
            x = temp #x와 y를 바꿔줌
    # 유클리드 호제법에 의해 최대 공약수를 구함
    while(y>0):
        r = x%y
        x = y
        y = r
    return x

#class Fraction 정의
class Fraction():
    def __init__(self,n,d):
        """
        생성자(초기화) 함수
        :param n: 분자
        :param d: 분모
        """
        self.n = n
        self.d = d
#분수의 더하기 오버로딩
    def __add__(self, other):
        g1 = Fraction((self.n * other.d) + (self.d * other.n),(self.d * other.d)) #g1에 약분이 안된 분수 저장
        g2 = gcm(g1.n,g1.d) #g2에 최대공약수 저장
        if (g1.n % g2 == g1.d %g2): #만약 분자와 분모를 최대공약수로 나눴을 때 나머지가 같다면
            g1.n = g1.n // g2 #g1의 분자를 최대공약수로 나눈다.
            g1.d = g1.d // g2 #g1의 분모를 최대공약수로 나눈다.
        return g1 #기약분수가 된 g1 반환
#분수의 빼기 오버로딩
    def __sub__(self, other):
        g1 = Fraction((self.n * other.d) - (self.d * other.n),(self.d * other.d)) #g1에 약분이 안된 분수 저장
        g2 = gcm(g1.n,g1.d) #g2에 최대공약수 저장
        if (g1.n % g2 == g1.d %g2): #만약 분자와 분모를 최대공약수로 나눴을 때 나머지가 같다면
            g1.n = g1.n // g2 #g1의 분자를 최대공약수로 나눈다.
            g1.d = g1.d // g2 #g1의 분모를 최대공약수로 나눈다.
        return g1 #기약분수가 된 g1 반환
#분수의 곱하기 오버로딩
    def __mul__(self, other):
        g1 = Fraction((self.n * other.n),(self.d *other.d)) #g1에 약분이 안된 분수 저장
        g2 = gcm(g1.n,g1.d) #g2에 최대공약수 저장
        if (g1.n % g2 == g1.d % g2): #만약 분자와 분모를 최대공약수로 나눴을 때 나머지가 같다면
            g1.n = g1.n // g2 #g1의 분자를 최대공약수로 나눈다.
            g1.d = g1.d //g2 #g1의 분모를 최대공약수로 나눈다.
        return g1 #기약분수가 된 g1 반환
#분수의 나누기 오버로딩
    def __truediv__(self, other):
        g1 = Fraction((self.n * other.d),(self.d *other.n)) #g1에 약분이 안된 분수 저장
        g2 = gcm(g1.n,g1.d) #g2에 최대공약수 저장
        if (g1.n % g2 == g1.d % g2): #만약 분자와 분모를 최대공약수로 나눴을 때 나머지가 같다면
            g1.n = g1.n // g2 #g1의 분자를 최대공약수로 나눈다.
            g1.d = g1.d // g2 #g1의 분모를 최대공약수로 나눈다.
        return g1 #기약분수가 된 g1 반환
# '>=' 재정의
    def __ge__(self, other): #분모는 통분하면 같으므로 분자만 비교
        g1 = self.n*other.d #self의 분자에 other의 분모를 곱한다.
        g2 = other.n*self.d #other의 분자에 self의 분모를 곱한다.
        if g1 >= g2: #g1과 g2를 비교해서 g1이 크거나 같으면
            return True #True를 반환
        else: #아니라면
            return False #False를 반환
# '<=' 재정의
    def __le__(self, other): #분모는 통분하면 같으므로 분자만 비교
        g1 = self.n*other.d #self의 분자에 other의 분모를 곱한다.
        g2 = other.n*self.d #other의 분자에 self의 분모를 곱한다.
        if g1 <= g2: #g1과 g2를 비교해서 g1이 작거나 같으면
            return True #True를 반환
        else: #아니라면
            return False #False를 반환
# '==' 재정의
    def __eq__(self, other): #분모는 통분하면 같으므로 분자만 비교
        g1 = self.n*other.d #self의 분자에 other의 분모를 곱한다.
        g2 = other.n*self.d #other의 분자에 self의 분모를 곱한다.
        if g1 == g2: #g1과 g2를 비교해서 g1이 같으면
            return True #True를 반환
        else: #아니라면
            return False #False를 반환

# '<' 재정의
    def __lt__(self, other): #분모는 통분하면 같으므로 분자만 비교
        g1 = self.n*other.d #self의 분자에 other의 분모를 곱한다.
        g2 = other.n*self.d #other의 분자에 self의 분모를 곱한다.
        if g1 < g2: #g1과 g2를 비교해서 g1이 작다면
            return True #True를 반환
        else: #아니라면
            return False #False를 반환
# '>' 재정의
    def __gt__(self, other): #분모는 통분하면 같으므로 분자만 비교
        g1 = self.n*other.d #self의 분자에 other의 분모를 곱한다.
        g2 = other.n*self.d #other의 분자에 self의 분모를 곱한다.
        if g1 > g2: #g1과 g2를 비교해서 g1이 크다면
            return True #True를 반환
        else: #아니라면
            return False #False를 반환
# '!=' 재정의
    def __ne__(self, other): #분모는 통분하면 같으므로 분자만 비교
        g1 = self.n*other.d #self의 분자에 other의 분모를 곱한다.
        g2 = other.n*self.d #other의 분자에 self의 분모를 곱한다.
        if g1 != g2: #g1과 g2를 비교해서 g1이 g2와 같지 않다면
            return True #True를 반환
        else: #아니라면
            return False #False를 반환
#__str__재정의
    def __str__(self):
        if self == Fraction.__add__(a,b): #self가 Fraction add(a,b)와 같다면
            return "("+str(a.n)+"/"+str(a.d)+")"+"+"+"("+str(b.n)+"/"+str(b.d)+")"+"="+"("+str(self.n)+"/"+str(self.d)+")" #a의 분자와 분모, b의 분자와 분모, 결과값을 sting으로 변환해 반환한다.
        elif self == Fraction.__sub__(a,b): #self가 Fraction sub(a,b)와 같다면
            return "("+str(a.n)+"/"+str(a.d)+")"+"-"+"("+str(b.n)+"/"+str(b.d)+")"+"="+"("+str(self.n)+"/"+str(self.d)+")"  #a의 분자와 분모, b의 분자와 분모, 결과값을 sting으로 변환해 반환한다.
        elif self == Fraction.__mul__(a,b): #self가 Fraction mul(a,b)와 같다면
            return "("+str(a.n)+"/"+str(a.d)+")"+"*"+"("+str(b.n)+"/"+str(b.d)+")"+"="+"("+str(self.n)+"/"+str(self.d)+")"  #a의 분자와 분모, b의 분자와 분모, 결과값을 sting으로 변환해 반환한다.
        elif self == Fraction.__truediv__(a,b): #self가 Fraction truediv(a,b)와 같다면
            return "("+str(a.n)+"/"+str(a.d)+")"+"/"+"("+str(b.n)+"/"+str(b.d)+")"+"="+"("+str(self.n)+"/"+str(self.d)+")"  #a의 분자와 분모, b의 분자와 분모, 결과값을 sting으로 변환해 반환한다.

#실행 코드

a = Fraction(3,5) #a에 값을 저장
b = Fraction(3,7) #b에 값을 저장
print(a+b) #a와 b를 더한 값을 프린트

a = Fraction(8,31) #a에 값을 저장
b = Fraction(2,3) #b에 값을 저장
print(a-b) #a와 b를 뺀 값을 프린트

a = Fraction(-4,5) #a에 값을 저장
b = Fraction(3,2) #b에 값을 저장
print(a*b) #a와 b를 곱한 값을 프린트

a = Fraction(4,8) #a에 값을 저장
b = Fraction(2,4) #b에 값을 저장
print("(%d/%d) == (%d/%d) 의 결과는 %s 입니다." %(a.n,a.d,b.n,b.d,a==b)) #a와 b가 동일한지 검사 후 값을 출력

a = Fraction(2,81) #a에 값을 저장
b = Fraction(3,9) #b에 값을 저장
print("(%d/%d) >= (%d/%d) 의 결과는 %s 입니다." %(a.n,a.d,b.n,b.d,a>=b)) #a가 b보다 크거나 같은지 검사 후 값을 출력