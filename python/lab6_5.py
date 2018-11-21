"""
챕터: day6
주제:class 상속 / 계승(inheritance)
문제: 정수집합 클래스
작성자: 김은정
작성일: 2018. 11. 8.
"""
"""
1. 사람 클래스를 정의한다. 이름과 나이를 (data) attribute로 가지고 있다.
A. 이름과 나이를 매개변수로 받는 생성자가 있다.
B. 나이를 1살 더하는 getOlder 메쏘드가 있다.
C. 문자열 반환, 프린트 메쏘드
"""
class People: #사람클래스 정의
    def __init__(self,name,age): #생성자함수 정의
        self. name = name #이름을 저장하고
        self. age = age #나이를 저장한다

    def getOlder(self): #나이를 한살 올리는 method
         self.age += 1 #함수 호출 시 age에 +1

    def __str__(self): #str함수 overloading
        return "이름은 "+str(self.name)+"이고, 나이는 "+str(self.age)+"살 입니다." #이름과 나이를 str타입으로 변환 후 반환

    def print(self):
        print(self)
"""
3. 사람을 계승하는 학생 클래스를 정의한다. 학교와 학년, 학번을 data attritube로 가지고 있다.
A. 이름, 나이, 학년, 학번을 받는 생성자가 있다. 생성자 내에서 사람의 생성자(People.__init__)를 호출한다.
B. 학년을 진급하는 upgrade() 메쏘드가 있다.
C. 문자열 반환(override), 프린트 메쏘드
"""
class Student(People): #Student 클래스는 People 클래스를 계승한다.
    def __init__(self,name,age,grade,snum): #이름, 나이, 학년, 학번을 받는 생성자
        """
        생성자 내에서 사람의 생성자(People.__init__)를 호출한다.
        Student도 일종의 People이다.
        People 이라서 가지고 있는 attribute면 age와 name은
        People의 생성자(__init__)를 통해 초기화한다.
        """
        People.__init__(self,name, age) #인스턴스가 아니라 클래스를 호출한 것이기 때문에 People을 빼면 안된다.
        #학번과 학년은 Student의 생성자 내에서 초기화
        self.grade = grade
        self. snum = snum
        self. school = "성공회대학교"
    def upgrade(self): #학년을 1학년 진급시키는 메쏘드
        self.grade +=1
    def __str__(self):
        """
        People 클래스에서 정의된 __str__를 overrideing 한다.
        :return: 문자열 반환
        """
        s = People.__str__(self)
        return s+" 학년은 "+str(self.grade)+"학년 이고, 학번은 "+self.snum+" 학교는 "+self.school+"입니다."
    def print(self):
        """
        People 클래스에서 정의된 print()를 overriding 한다.
        :return:
        """
        print(self)

# 실행부분
# 두명의 Person instance를 만들어서 나이를 한살 올린 후 출력한다.

p1 = People("김일수",30) #p1에 people 클래스 저장
p2 = People("김이수",40) #p2에 people 클래스 저장
p1.getOlder() #p1의 나이를 한살 올림
p2.getOlder() # p2의 나이를 한살 올림
p1.print() #p1를 프린트
p2.print() #p2를 프린트

#p1.upgrade() #p1은 Student가 아니므로, upgrade() 메쏘드를 사용할 수 없다.

#두 명의 Student instance를 만든다.
s1 = Student("김삼수", 20, 2, "203222123")
s2 = Student("김사수", 21, 3, "202232453")

s1.getOlder() # s1 은 Student인데, People을 계승했으므로 People의 메쏘드 사용이 가능하다.
s1.upgrade()
s1.print() # s1은 Student인데, People을 계승했으므로 People의 메쏘드 사용이 가능하다.

#People과 Student를 포함하는 리스트 생성
l=[p1,p2,s1,s2]
print("====리스트 출력====")
for e in l:
    e.getOlder()
    e. print()