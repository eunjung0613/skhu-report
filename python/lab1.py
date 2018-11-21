number = "hi" #number의 타입이 문자열
print(number) #문자열 number 출력
number = 10  # number의 타입이 정수형으로 바뀜
print(number) #정수형 number 출력

#변수 a,b에  값을 저장한 후, 합을 c 변수에 저장 후 c를 출력

a = 4
b = 5
c = a+b
# 4+5 = 9와같이 출력하라
print("%d + %d = %d"%(a,b,c)) #서식문자를 여럿 사용할 때 ,없이 %를 사용 후 (괄호)안에 변수이름을 써 넣는다.
msg = "%d +%d  %d" #출력하려는 문자열을 변수로 지정할 수 있다.
print(msg%(a,b,c))

#문자열 출력

money = 10000
print("나는 현재 %d 원이 있습니다." %money) #서식문자를 이용할 수 있다. ,없이 변수이름 앞에 %를 붙인다.

#입력받기

money = input("얼마를 가지고 계세요?") #input의 결과값은 문자열이 넘어온다.
print("입력하신 값은 %s 입니다." %money) #money의 타입이 문자열이므로 %s를 사용한다.
