"""
챕터: day6
주제: class
문제:
숫자를 하나씩 발생시키는 Counter 클래스 정의
작성자: 김은정
작성일: 2018.10.18
"""

# Counter 클래스 정의
class Counter:
    def __init__(self):
        # instance를 생성할 때 초기화하는 메소드. instance를 생성할 때 자동 호출 됨.
        self.count = 0
    def __init__(self, start=0):
        # instance를 생성할 때 초기화하는 메소드. instance를 생성할 때 자동 호출됨.
        self.count = start
    def reset(self): # self: method가 수행되는 instance 자신을 의미.
        #count를 초기화하는 method
        self.count = 0 #counter는 instance variable(member)

    def increment(self):
        #카운터를 하나 증가시킴
        self.count += 1 #count를 1 증가시킴

    def get(self):
        #count 값을 반환
        return self.count

#실행 코드 시작
#class Counter의 instance를 생성해서 변수 a에 저장
a = Counter() #Counter는 클래스 이름. ()가 있어야 한다. start가 디폴드값 0으로 전달됨
#class Counter의 instance를 새성해서 변수 b에 저장. 매개변수를 포함흐는__init함수가 호출됨
b = Counter(10)

a.reset() #변수에 .을 이용하여 메소드 호출. self 매개변수값이 되어 넘어감.
a.increment()
a.increment()
a.increment()
print("a = %d" %a.get())
print("b = %d" %b.get())

