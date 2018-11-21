"""
챕터: da3
주제: 데이터형 연습
작성자: 김은정
작성일: 2018. 9.4
"""
f = 3.4 #f의 데이터타입은 float. 왜냐하면, 실수인 3.4가 f에 저장되었기 때문이다.
print(f)
i = 3 # i의 데이터타입은 int. 왜냐하면, i에 정수인 3이 저장되었기 때문이다.
print(i)
b = True #b는 boolean type. 왜냐하면, b에 True가 저장되었기 때문이다. (boolean type은 True 또는 False를 저장한다.)
print(b)
s = "안녕하세요."#s 의 데이터 타입은 str.  문자열은 ""(더블쿼트)로 묶는다. 또는 ' ' (싱글쿼트)로 묶는다.
print(s)
s = '1'#s 의 데이터타입은 str.
print(s)


#f와 i를 더해서 출력 i 가 float으로 자동 변화되어 계산함.
print(f+i)

# s와 i를 더해서 출력
# 오류 발생. 왜냐하면 문자열은 자동으로 변환되지는 않는다.
# print(s+i)

#s를 int로 형 변환하여 i와 더하기.
print(int(s)+i)

#i를 str로 형 변환하여 s와 더하기. 문자열 이어주기 연산이 실행됨.
print(s+str(i))

#정수계산
print("정수계산")
i = 57
j = 28

#i를 j로 나눈 값 출력
print(i/j)
#i로 j를 나눈 몫 출력
print(i//j)
#i를 j 로 나누었을 때 나머지 출력
print(i%j)
#j의 제곱 출력
print(j**2)
#j의 세제곱 출력
print(j**3)

# or 연산자
print(b or False) #or 연산자는 boolean type 에 대한 연산자이다.

# and 연산자#  print(b and False)
print(b and False)#and 연산자는 boolean type에 대한 연산자이다.

# 복소수(실수부와 허수부로 구성된 숫자) 타입 변수 k
k = 5+7j
print(k) #복소수를 직접 표현. 허수부인 i를 j로 표현.
print(k.real) # 복소수의 실수부분만 표현
print(k.imag) # 복소수의 허수부분만 표현
print(k.conjugate())# 켤레 복소수를 가져오는 함수 호출

# 8진수 표현
o = 0o16 # 10진수로는 14를 의미. 데이터 타입은 int.
print(o) # 기본 출력은 십진수.
print("%o" %o) # 8진수로 출력됨.
print("%x" %o) # 16진수로 출력됨. 소문자 %x는 소문자로 출력, %X는 대문자로 출력

#16진수 표현
x = 0xA5
# 십진수 출력
print(x)
# 8진수 출력
print("%o" %x)
# 16진수 출력
print("%X" %x)

#실수계산
print("실수 계산")
i = 57.0
j = 28.0

#i를 j로 나눈 값 출력
print(i/j)
#i로 j를 나눈 몫 출력
print(i//j)
#i를 j 로 나누었을 때 나머지 출력
print(i%j)
#j의 제곱 출력
print(j**2)
#j의 세제곱 출력
print(j**3)
